from SharedServices import AddService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = AddService.Client(protocol)

    # Connect!
    transport.open()

    client.ping(1)
    client.ping(2)
    client.ping(3)

    out = client.add(1, 1)
    print 'Result: %d' % out

    # Close!
    transport.close()

main()
