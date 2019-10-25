import bluetooth
import threading
import time

class ClientThread(threading.Thread):
    def __init__(self, q, socket):
        threading.Thread.__init__(self)
        self.mQueue = q
        self.mSocket = socket
        self.shutdown_flag = threading.Event()

    def run(self):
        while not self.shutdown_flag.is_set():
            try:
                data = self.mSocket.recv(256)
                print("Received: ", data)
                self.mQueue.put(data.decode())
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
        self.mClientThread = None
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            wClientSocket,wAddress = self.mServerSocket.accept()
            print("BtConnection accepted connection from ", wAddress)

            if self.mClientThread != None:
                self.mClientThread.shutdown_flag.set()
                self.mClientThread.join()

            wClientSocket.settimeout(5) #seconds
            self.mClientThread = ClientThread(self.mQueue, wClientSocket)
            self.mClientThread.start()

            time.sleep(0.1)

