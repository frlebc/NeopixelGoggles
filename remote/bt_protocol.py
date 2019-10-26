from queue import Queue
from remote.bt_protocol_handlers import *
from remote.bt_connection import BtConnection

class BtProto:
    def __init__(self, q, connection):
        self.mQueue = q
        self.mBtConnection = connection

    def read(self):
        while not self.mQueue.empty():
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

    def writeTemperature(self, temp):
        self.mBtConnection.write("temp.%.2f"%temp)

