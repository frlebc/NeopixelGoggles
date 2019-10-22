from queue import Queue

class BtProto:
    def __init__(self, q):
        self.mQueue = q

    def getQueue(self):
        return self.mQueue