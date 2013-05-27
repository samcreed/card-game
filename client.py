
from optparse import OptionParser
import socket

usage = "usage: %prog [options] arg"
parser = OptionParser(usage)

parser.add_option("-x", "--host", dest="host", default="localhost", help="host IP to connect to")
parser.add_option("-p", "--port", dest="port", default="50000", help="port to connect to")
parser.add_option("-n", "--name", dest="name", default="noname", help="player's display name")

(options, args) = parser.parse_args()




#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((options.host, options.port))



#s.send('Hello, world')

#data = s.recv(size)
#s.close()

#print 'Received:', data
