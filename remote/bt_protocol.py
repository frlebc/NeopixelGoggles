from queue import Queue

class BtProto:
    def __init__(self, q):
        self.mQueue = q

    def read(self):
        if self.mQueue.empty():
            return None

        cmd = self.mQueue.get(False)
        print("Command: ", cmd)
