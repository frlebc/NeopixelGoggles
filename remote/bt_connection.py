import bluetooth
import threading
import time

def clientThread(q, socket):
    while True:
        try:
            data = socket.recv(256)
            print("Received: ", data)
            q.put(data.decode())
        except:
            pass # timeout

class BtConnection(threading.Thread):

    def __init__(self, q, *args, **kwargs):
        self.mServerSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        wPort = 1
        self.mServerSocket.bind(("",wPort)) # not important which port we bind for Bluetooth
        self.mServerSocket.listen(5) # Allow 5 failed connection attempts before blocking
        self.mQueue = q
        self.mData = []
        self.mClientThreads = []
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            wClientSocket,wAddress = self.mServerSocket.accept()
            print("BtConnection accepted connection from ", wAddress)
            wClientSocket.settimeout(5) #seconds
            wThread = threading.Thread(target=clientThread, args=(self.mQueue, wClientSocket, ))
            self.mClientThreads.append(wThread)
            wThread.start()
            time.sleep(0.1)

