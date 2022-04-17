import socket
import struct
import sys
import os
import logging

FORMAT = '%(process)d %(processName)s %(asctime)s : %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

def mrecv():
   multicast_group = '224.3.29.71'
   server_address = ('', 10000)
   
   # Create UDP socket
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
   # Bind to the server address
   sock.bind(server_address)
   
   # Tell the operating system to add the socket to the multicast group
   # on all interfaces.
   group = socket.inet_aton(multicast_group)
   mreq = struct.pack('4sL', group, socket.INADDR_ANY)
   sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
   
   # Receive/respond loop
   while True:
       logging.info('waiting to receive message')
       data, address = sock.recvfrom(1024)
       
       print('received %s bytes from %s' % (len(data), address) )
       print(data)
   
       print ('sending acknowledgement to', address )
       sock.sendto('ack'.encode(), address)


if __name__ == '__main__':
    mrecv()