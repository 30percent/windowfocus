#! /usr/bin/env python
#coding=utf-8

import threading, socket, select, time
import errno, random, collections

MAXLEN=20
glob = 1
deq = collections.deque(maxlen=MAXLEN)
deq.extend([random.randint(0,5) for r in xrange(20)])

class ClientSocket(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        ip = '127.0.0.1'
        port = 50004
        buffer = 1024

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        i = 50
        while (i > -2):
            data = s.recv(buffer)
            int_lst = [int(x) for x in filter(None, data.split("_"))]
            deq.extend(int_lst)
            i -= 1
        s.close()

class HandleStream(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop = threading.Event()

    def run(self):
        global deq
        while not self._stop.is_set():
            self.compute()
            time.sleep(2)

    def compute(self):
        s = sum(deq)
        av = s/20
        count = collections.Counter(deq)
        it = next(iter(count.most_common(1)))
        if(it[1] > (len(deq)/2)):
            print "\nMode: ", it[0]
        ##
    def stop(self):
        self._stop.set()    

class StreamChange(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global glob
        for x in range (0,100):
            glob = random.randint(0,5)
            time.sleep(.1)
        
class ServerSocket(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._stop = threading.Event()
        
    def run(self):
        global glob
        ip = '127.0.0.1'
        port = 50004
        buffer = 1024
        s = self.s
        s.bind((ip, port))
        s.listen(1)
        
        self._stop.clear()
        t = self._stop.is_set()
        while not self._stop.is_set():
            t = self._stop.is_set()
            rr, rw, err = select.select([s],[],[],1)
            if rr:
                conn, addr = s.accept()
                print '\nConnection address:', addr
                while 1:
                    try:
                        conn.send(str(glob) + "_") #sending stream
                        time.sleep(.01)
                    except socket.error, e:
                        break
                conn.close()
    def stop(self):
        print "Server asked to stop"
        self._stop.set()


backgroundServ = ServerSocket()
backgroundServ.start()
st = StreamChange()
st.start()
hst = HandleStream()
hst.start()


backgroundCli = ClientSocket()
backgroundCli.start()
#print 'The main program continues to run in foreground.'

backgroundCli.join()    # Wait for the background task to finish
backgroundCli = ClientSocket()
backgroundCli.start()
backgroundCli.join()
#print 'First Client has ended. Sending stop command'
time.sleep(2)
b = ClientSocket()
b.start()
b.join()
backgroundServ.stop()
hst.compute()
hst.stop()

print 'Main program waited until background was done.'
