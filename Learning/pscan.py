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


def getInterface():
    networkCard = netifaces.interfaces()
    addressDictionary = {}
    for netActive in networkCard:
        a = netifaces.ifaddresses(netActive)
        if a.__len__() != 0:
            if a.has_key(2) and a[2][0].has_key('broadcast'):
                value = a[2][0]['addr'] + " - " + a[2][0]['netmask']
                addressDictionary[netActive] = value
    return addressDictionary


def retrieveNetwork(subnet, address):
    subnetField = str.split(subnet, '.')
    addressFiled = str.split(address, '.')
    listSubnetBlocks = list()

    if bin(int(subnetField[1])).count("1") < 8:
        subnetOnes = bin(int(subnetField[3])).count("1")
        subnetZeros = 8 - subnetOnes
        nSubnet = int(math.pow(2, subnetOnes))
        nBlocks = int(math.pow(2, 8 - subnetOnes))

        for i in range(0, nSubnet):
            listSubnetBlocks.append(i * nBlocks)
            print "list ", listSubnetBlocks
        if listSubnetBlocks  == True:
            a = 0
        else:
            a = min(x for x in listSubnetBlocks if int(addressFiled[1]) < x)
        subnetNetwork = [a, a + nBlocks - 1]
        addressNetwork = [addressFiled[0], addressFiled[1], addressFiled[2], subnetNetwork[0]]
        addressBroadcast = [addressFiled[0], addressFiled[1], addressFiled[2], subnetNetwork[1]]
        return addressNetwork, addressBroadcast


    # if subnetOnes < 8:
    #     nSubnet = int(math.pow(2, subnetOnes))
    #     nBlocks = int(math.pow(2, 8 - subnetOnes))
    #     for i in range(0, nSubnet):
    #         listSubnetBlocks.append(i * nBlocks)
    #         print "list ", listSubnetBlocks
    #
    #     isempty = (listSubnetBlocks and True) or False
    #     if isempty == True:
    #         a = 0
    #     else:
    #         a = min(x for x in listSubnetBlocks if int(addressFiled[3]) < x)
    # subnetNetwork = [a, a + nBlocks - 1]
    # addressNetwork = [addressFiled[0], addressFiled[1], addressFiled[2], subnetNetwork[0]]
    # addressBroadcast = [addressFiled[0], addressFiled[1], addressFiled[2], subnetNetwork[1]]
    # return addressNetwork, addressBroadcast

    # n4=int(math.log((256-int(subnetField[3])),2))
    # n3=int(math.log((256-int(subnetField[2])),2))
    # n2=int(math.log((256-int(subnetField[1])),2))
    # print n2 ,n3 ,n4

    # Consideriamo quindi il 3 Ottetto quindi indirizzi di classe B







    numhost = math.pow(2, (n2 + n3 + n4))
    print bin(int(subnetField[3])).count("1")


def getActiveIntIPandNetwork():
    networkInt = getInterface()
    for k, v in networkInt.iteritems():
        address, subnet = str.split(v, '-')
        print address, subnet
        retrieveNetwork("255.0.0.0", "192.168.10.15")


print getActiveIntIPandNetwork()

# print netifaces.ifaddresses(networkInt[0])[2][0]['addr']
# print netifaces.ifaddresses(networkInt[0])[2][0]['netmask']




# networkCardLen=networkCard.__len__()
# print networkCard
# #print networkCardLen
#
# for active in networkCard:
#     a=netifaces.ifaddresses(active)
#     if a.__len__()!=0:
#         for key in a.iteritems():
#             skey=key[1]
#             print  active, skey[0]['peer']


# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print socket.gethostbyname(socket.gethostname())
# print socket.inet_ntoa(fcntl.ioctl(sock.fileno(), 0x891b, struct.pack('256s','eth0'))[20:24])

# host="172.31.4.25"
# port= 1
# name= socket.gethostbyaddr(host)
# for port in range(1,1025):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     result = sock.connect_ex((host,port))
#     if result == 0:
#         print "Port "+str(port)+" of server "+str(name[0])+" is open"
#         sock.close()



print "Finished"
