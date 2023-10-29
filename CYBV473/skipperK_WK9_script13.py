'''

WK-9 PCAP STARTER SCRIPT
Written exclusively for Python 3.4.x or above

Overview:

The script ingests a standard PCAP File and creates a passive
asset map based on the observed UNIQUE activity and stores the
resultng map as a serialzed python object.  In addition, an html
file is generated that depicts the observed asset map.

'''
# Python Standard Library Module Imports

import sys  # System specifics
import platform  # Platform specifics
import os  # Operating/Filesystem Module
import pickle  # Object serialization
import time  # Basic Time Module
import re  # regular expression library
from binascii import unhexlify

# 3rd Party Libraries

from prettytable import PrettyTable  # pip install prettytable

'''


Simple PCAP File 3rd Party Library 
to process pcap file contents

To install the Library
pip install pypcapfile 

'''

from pcapfile import savefile
from pcapfile.protocols.linklayer import ethernet
from pcapfile.protocols.network import ip
from pcapfile.protocols.transport import tcp
from pcapfile.protocols.transport import udp

# Script Constants

NAME = "PYTHON PCAP PROCESSOR"
VERSION = "VERSION 1.0 AUGUST 2021"
AUTHOR = "C. Hosmer"
DEBUG = True

# Script Constants

DEBUG = True


# Script Local Functions


class ETH:
    '''LOOKUP ETH TYPE'''

    def __init__(self):

        self.ethTypes = {}

        self.ethTypes[2048] = "IPv4"
        self.ethTypes[2054] = "ARP"
        self.ethTypes[34525] = "IPv6"

    def lookup(self, ethType):

        try:
            result = self.ethTypes[ethType]
        except:
            result = "not-supported"

        return result


# MAC Address Lookup Class
class MAC:
    ''' OUI TRANSLATION MAC TO MFG'''

    def __init__(self):

        # Open the MAC Address OUI Dictionary
        with open('oui.pickle', 'rb') as pickleFile:
            self.macDict = pickle.load(pickleFile)

    def lookup(self, macAddress):
        try:
            result = self.macDict[macAddress]
            cc = result[0]
            oui = result[1]
            return cc + "," + oui
        except:
            return "Unknown"


# Transport Lookup Class

class TRANSPORT:
    ''' PROTOCOL TO NAME LOOKUP'''

    def __init__(self):

        # Open the transport protocol Address OUI Dictionary
        with open('protocol.pickle', 'rb') as pickleFile:
            self.proDict = pickle.load(pickleFile)

    def lookup(self, protocol):
        try:
            result = self.proDict[protocol]
            return result
        except:
            return ["unknown", "unknown", "unknown"]


# PORTS Lookup Class

class PORTS:
    ''' PORT NUMBER TO PORT NAME LOOKUP'''

    def __init__(self):

        # Open the MAC Address OUI Dictionary
        with open('ports.pickle', 'rb') as pickleFile:
            self.portDict = pickle.load(pickleFile)

    def lookup(self, port, portType):
        try:
            result = self.portDict[(port, portType)]
            return result
        except:
            return "EPH"


if __name__ == '__main__':

    print("PCAP PROCESSOR v 1.0 AUGUST 2021")

    # Create Lookup Objects
    macOBJ = MAC()
    traOBJ = TRANSPORT()
    portOBJ = PORTS()
    ethOBJ = ETH()

    ''' Attemp to open a PCAP '''
    while True:
        targetPCAP = input("Target PCAP File: ")
        if not os.path.isfile(targetPCAP):
            print("Invalid File: Please enter valid path\n")
            continue
        try:
            pcapCapture = open(targetPCAP, 'rb')
            capture = savefile.load_savefile(pcapCapture, layers=0, verbose=False)
            print("PCAP Ready for Processing")
            break
        except:
            # Unable to ingest pcap
            print("!! Unsupported PCAP File Format !! ")
            continue

    totPackets = 0
    pktCnt = 0

    # Now process each packet
    for pkt in capture.packets:
        pktCnt += 1

        # extract the hour the packet was captured
        timeStruct = time.gmtime(pkt.timestamp)
        capHour = timeStruct.tm_hour - 1

        # Get the raw ethernet frame
        ethFrame = ethernet.Ethernet(pkt.raw())

        '''
        Ethernet Header
        0                   1                   2                   3                   4              
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |                                      Destination Address                                      |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |                                         Source Address                                        |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |           EtherType           |                                                               |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                                               +
        |                                                                                               |
        +                                            Payload                                            +
        |                                                                                               |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

        '''

        ''' ---- Extract the source mac address ---- '''
        srcMAC = "".join(map(chr, ethFrame.src))
        srcMACLookup = srcMAC[0:8].upper()
        # remove the colon seperators
        # note the variable names starting with fld, we will use these later
        srcMACLookup = re.sub(':', '', srcMACLookup)

        # Attempt to lookup the mfg in our lookup table
        # Country Code and Organization
        srcMFG = macOBJ.lookup(srcMACLookup)

        ''' Extract the destination mac address ---'''
        dstMAC = "".join(map(chr, ethFrame.dst))
        dstMACLookup = dstMAC[0:8].upper()
        # remove the colon seperators
        # note the variable names starting with fld, we will use these later
        dstMACLookup = re.sub(':', '', dstMACLookup)

        # Attempt to lookup the mfg in our lookup table
        # Country Code and Organization
        dstMFG = macOBJ.lookup(dstMACLookup)

        ''' Lookup the Frame Type '''
        frameType = ethOBJ.lookup(ethFrame.type)

        print("====== ETHERNET LAYER =====\n")
        print("TIMESTAMP:", timeStruct)
        print("SRC MAC:  ", srcMAC)
        print("DST MAC:  ", dstMAC)
        print("SRC MFG:  ", srcMFG)
        print("DST MFG:  ", dstMFG)
        print("FRAME TYP:", frameType)
        print("=" * 40, "\n")

        ''' Process any IPv4 Frames '''

        if frameType == "IPv4":
            '''
            ipV4 Header
            0                   1                   2                   3  
            0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |Version|  IHL  |Type of Service|          Total Length         |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |         Identification        |Flags|     Fragment Offset     |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |  Time to Live |    Protocol   |        Header Checksum        |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |                         Source Address                        |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |                      Destination Address                      |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |                    Options                    |    Padding    |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+   
            '''

            ''' Extract the payload '''
            ipPacket = ip.IP(unhexlify(ethFrame.payload))
            ttl = ipPacket.ttl

            ''' Extract the source and destination ip addresses '''
            srcIP = "".join(map(chr, ipPacket.src))
            dstIP = "".join(map(chr, ipPacket.dst))

            ''' Extract the protocol in use '''
            protocol = str(ipPacket.p)

            ''' Lookup the transport protocol in use '''
            transport = traOBJ.lookup(protocol)[0]

            print("====== IPv4 Transport LAYER =====\n")
            print("TTL:   ", ttl)
            print("SRC-IP:", srcIP)
            print("DST-IP:", dstIP)
            print("Protocol:", protocol)
            print("=" * 40, "\n")

            if transport == "TCP":

                '''
                TCP HEADER
                0                   1                   2                   3  
                0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                |          Source Port          |        Destination Port       |
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                |                        Sequence Number                        |
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                |                     Acknowledgment Number                     |
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                | Offset|  Res. |     Flags     |             Window            |
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                |            Checksum           |         Urgent Pointer        |
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                |                    Options                    |    Padding    |
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                '''

                ''' 
                **** YOUR CODE HERE ****

                '''

            elif transport == "UDP":
                '''
                 0                   1                   2                   3  
                 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
                 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                 |          Source Port          |        Destination Port       |
                 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                 |             Length            |            Checksum           |
                 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                 '''

                ''' 
                **** YOUR CODE HERE ****

                '''

            elif transport == "ICMP":
                '''
                 0                   1                   2                   3  
                 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
                 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                 |      Type     |      Code     |            Checksum           |
                 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                 |                                                               |
                 +                          Message Body                         +
                 |                                                               |
                 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                 '''
                ''' 
                **** YOUR CODE HERE ****

                '''

        elif frameType == "ARP":
            '''
            0                   1      
            0 1 2 3 4 5 6 7 8 9 0 1 2 3
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |  Dst-MAC  |  Src-MAC  |TYP|
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |                           |
            +       Request-Reply       +
            |                           |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |        PAD        |  CRC  |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            '''

            ''' 
            **** YOUR CODE HERE ****

            '''


        else:
            continue

    print("\n\nScript End")
