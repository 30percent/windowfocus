import socket, thread, time
#client
def client():
    ip = '127.0.0.1'
    port = 120007
    buffer = 1024
    message = '1,2,3,4,5'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(message)
    data = s.recv(buffer)
    s.close()

    print data

#server
def server():
    ip = '127.0.0.1'
    port = 120007
    buffer = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    
    conn, addr = s.accept()
    print 'Connection address:', addr

    while 1:
        data = conn.recv(buffer)
        if not data: break
        print "recv d: ", data
        conn.send(data) #echo
    conn.close()

def thr(tName):
    print "I'm ", tName
    i = 0
    while i < 10:
        print i, " ", tName

try:
    thread.start_new_thread( thr, args["Thread 1", kwargs] )
    thread.start_new_thread( thr, args["Thread 2", kwargs] )
except:
    print "Lol"

time.sleep(2)