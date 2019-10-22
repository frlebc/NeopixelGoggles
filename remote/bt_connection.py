import bluetooth
import threading

class BtConnection(threading.Thread):

    def __init__(self, q, *args, **kwargs):
        self.mServerSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        wPort = 1
        self.mServerSocket.bind(("",wPort)) # not important which port we bind for Bluetooth
        self.mServerSocket.listen(5) # Allow 5 failed connection attempts before blocking
        self.mQueue = q
        super().__init__(*args, **kwargs)
    
    def run(self):
        wClientSocket,wAddress = self.mServerSocket.accept()
        print("BtConnection accepted connection from ", wAddress)

        wClientSocket.settimeout(5) #seconds

        while 1:
            try:
                data = wClientSocket.recv(256) #TODO Timeout?
                print("Received: ", data)
            except:
                print("Timeout")
                pass # timeout

    