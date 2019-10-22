import bluetooth
import threading

class BtConnection(threading.Thread):

    def __init__(self, q, *args, **kwargs):
        self.mServerSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        wPort = 1
        self.mServerSocket.bind(("",wPort)) # not important which port we bind for Bluetooth
        self.mServerSocket.listen(5) # Allow 5 failed connection attempts before blocking
        self.mQueue = q
        self.mData = []
        super().__init__(*args, **kwargs)
    
    def run(self):
        wClientSocket,wAddress = self.mServerSocket.accept()
        print("BtConnection accepted connection from ", wAddress)

        wClientSocket.settimeout(5) #seconds

        while 1:
            try:
                data = wClientSocket.recv(256)
                #print("Received: ", data)
                if data == b'\r\n' or data == b'\n':
                    self.mQueue.put(''.join(self.mData.copy()))
                    self.mData.clear()
                else:
                    self.mData.append(data.decode())
            except:
                pass # timeout

    