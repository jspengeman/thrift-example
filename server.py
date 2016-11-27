from SharedServices import AddService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class AddHandler:
    def __init__(self):
        self.log = {}

    def add(self, n1, n2):
        print 'add(%d,%d)' % (n1, n2)
        return n1 + n2

    def ping(self, num):
        print "PING! %d" % num

handler = AddHandler()
processor = AddService.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
server.serve()
