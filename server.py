
from twisted.internet import protocol
from twisted.internet import reactor

class Echo(protocol.Protocol):
    def dataRecieved(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(1234, EchoFactory())
reactor.run()
