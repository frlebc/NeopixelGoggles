from queue import Queue
from remote.bt_protocol_handlers import *

class BtProto:
    def __init__(self, q):
        self.mQueue = q

    def read(self):
        if self.mQueue.empty():
            return None

        cmd = self.mQueue.get(False)
        #print("Command: ", cmd)

        if self.isValidCommandSyntax(cmd):
            dotIndex = cmd.index(".")
            opcode = cmd[:dotIndex]
            value = cmd[dotIndex+1:]
            #print("Opcode: ", opcode)
            #print("Value: ", value)
            if opcode in BtProtocolHandlers:
                BtProtocolHandlers[opcode](value)

    def isValidCommandSyntax(self, cmd):
        return "." in cmd #Only restriction in syntax for now

