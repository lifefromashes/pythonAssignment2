'''
BLACK HAT PYTHON
SNIFFER EXPERIMENT WITH MODIFICATIONS
Professor Hosmer
October 2021

STRUCT UNPACK FORMATTING NOTES
Format	C Type	            Python type	     Standard size
x	pad byte            no value
c	char	            bytes of length 	1
b	signed char         integer	        1
B	unsigned char       integer	        1
?	_Bool	            bool	        1
h	short	            integer	        2
H	unsigned short	    integer	        2
i	int	            integer	        4
I	unsigned int	    integer	        4
l	long	            integer	        4
L	unsigned long	    integer	        4
q	long long	    integer	        8
Q	unsigned long long  integer	        8
n	ssize_t	            integer
N	size_t	            integer
e	(6)	            float	       2
f	float	            float	       4
d	double	            float	       8
s	char[]	            bytes
p	char[]	            bytes
P	void*	            integer

ENCODING
Character  Byte order	            Size	Alignment
<	   little-endian	    standard	none
>	   big-endian	            standard	none
!	   network (= big-endian)   standard	none

IP Packet

'''
import socket
import os

from prettytable import PrettyTable

# Get the HOST to Sniff From
hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)

# HOST = 'localhost'

import ipaddress
import struct


class IP:
    def __init__(self, buff=None):
        header = struct.unpack('<BBHHHBBH4s4s', buff)
        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xF

        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]

        # human readable IP addresses
        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)

        # map protocol constants to their names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}


def main():
    socket_protocol = socket.IPPROTO_IP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))

    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    captureDict = {}

    for i in range(1, 10000):

        packet = sniffer.recvfrom(65565)  # Wait for Packet
        basePacket = packet[0]  # Extract Packet Data from tuple
        pckHeader = basePacket[0:20]  # Extract the packet header

        ipOBJ = IP(pckHeader)  # Create the IP Object

        # Lookup the protocol name
        try:
            protocolName = ipOBJ.protocol_map[ipOBJ.protocol_num]
        except:
            protocolName = "Unknown"

        print("SRC-IP  :", ipOBJ.src_address)
        print("DST-IP  :", ipOBJ.dst_address)
        print("Protocol:", protocolName)

        '''
        YOUR CODE GOES HERE 
        You will create a dictionary entry for each unique packet observered
        Unique Packets combination of SRC-IP, DST-IP, Protocol
        you will keep track of the count of each unique packet in the dictionary

        Note: Before executing your script, launch Chrome and access one or more
              of the CyberApolis web-sites to generate network traffic

        Once you have processed 10,000 packets update load your results
        into the prettytable and display.
        '''

    tbl = PrettyTable(["Occurs", "SRC", "DST", "Protocol"])
    print(tbl.get_string(reversesort=True))

    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


if __name__ == '__main__':
    main()