import network
import socket
import math
import time
import os
import fcntl
import struct
import sys
import netifaces
import subprocess
import bisect



print " LAN Analizing Started ........Please wait!"
networkInt = network.getInterface()

for k, v in networkInt.iteritems():
    address, subnet, broadcast = str.split(v, '-')

####  FOR TEST  PORPOUSE ####
#subnet="255.255.0.0"
#address="172.16.3.19"
##############################
netID=network.retrieveNetwork(subnet, address)
netHostAddr=network.getNetHostAddressFromNetId(netID,subnet)


if os.path.exists("./results/subnetaddresses.dat"):
    os.remove("./results/subnetaddresses.dat")
else:
    outfile = open("./results/subnetaddresses.dat", "w")
    for h in range (0,netHostAddr.__len__()):
        outfile.write(str(netHostAddr[h])+"\n")
    outfile.close()


#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Print socket.gethostbyname(socket.gethostname())
#a= socket.inet_ntoa(fcntl.ioctl(sock.fileno(), 0x891b, struct.pack('256s','eth0'))[20:24])


fw = open("./results/portfound.dat", "w")
listOpenedPorts=[]
for host in netHostAddr[1:netHostAddr.__len__()-1]:
    for port in range(1,1025):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((host,port))
            listOpenedPorts.append(port)
        except Exception, e:
            continue
        finally:
            sock.close()
    try:
        hostname=socket.gethostbyaddr(host)
    except Exception, e:
        hostname= "unknown"
    finally:
        sock.close()


    if listOpenedPorts.__len__()!=0:
        print "Server " +host +"--> Hostname: "+ hostname + str(listOpenedPorts)
        listOpenedPorts = []
    else:
        print host+ " Not Rechable"
        listOpenedPorts = []



    # if result == 0:
    #     fw.write("Port "+str(port)+" of server "+host+" is open" + "\n")
    #     print "Port " + str(port) + " of server " + host + " is open" + "\n"
    # sock.close()





