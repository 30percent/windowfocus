#! /usr/bin/env python
#coding=utf-8

import threading, socket, time
import errno

def StopServ():
    ip = '127.0.0.1'
    port = 50004
    buffer = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    excp = s.connect_ex((ip, port))
    print excp
    print "Sending: stop"
    try:
        s.send("stop")
    except socket.error, e:
        print "Not sent"
    data = s.recv(buffer)
    print "Received: ", data
    s.close()   

class ClientSocket(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print "Made"
    def run(self):
        print "Here"
        ip = '127.0.0.1'
        port = 50004
        buffer = 1024

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        i = 10
        while (i > -2):
            message = str(i)
            print "Send: ", message
            s.send(message)
            data = s.recv(buffer)
            print "Received: ", data
            i = i - 1
        s.close()

class ServerSocket(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        ip = '127.0.0.1'
        port = 50004
        buffer = 1024

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen(1)
        data = "GLOBALINT"
        running = True
        while running:
            conn, addr = s.accept()
            print 'Connection address:', addr

            while 1:
                data = conn.recv(buffer)
                if not data: break
                print "recv: ", data
                if data == "stop": running = False
                conn.send(data) #echo
            conn.close()


backgroundCli = ClientSocket()
backgroundServ = ServerSocket()
backgroundCli.start()
backgroundServ.start()
print 'The main program continues to run in foreground.'

backgroundCli.join()    # Wait for the background task to finish

print 'First Client has ended. Sending stop command'
StopServ()
backgroundServ.join()

print 'Main program waited until background was done.'
