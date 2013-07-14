
# main client for the game

# from optparse import OptionParser
# import socket
# import protocol

# usage = "usage: %prog [options] arg"
# parser = OptionParser(usage)

# parser.add_option("-x", "--host", dest="host", default="localhost", help="host IP to connect to")
# parser.add_option("-p", "--port", dest="port", default="50000", help="port to connect to")
# parser.add_option("-n", "--name", dest="name", default="NONAME", help="player's display name")

# (options, args) = parser.parse_args()


from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint

class Greeter(Protocol):
    def sendMessage(self, msg):
        self.transport.write("MESSAGE %s\n" % msg)

class GreeterFactory(Factory):
    def buildProtocol(self, addr):
        return Greeter()

def gotProtocol(p):
    p.sendMessage("Hello")
    reactor.callLater(1, p.sendMessage, "This is sent in a second")
    reactor.callLater(2, p.transport.loseConnection)

point = TCP4ClientEndpoint(reactor, "localhost", 1234)
d = point.connect(GreeterFactory())
d.addCallback(gotProtocol)
reactor.run()
