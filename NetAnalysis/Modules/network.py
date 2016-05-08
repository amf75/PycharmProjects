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

address=0
subnet=0
broadcast=0
network=0
nhost=[]

def getInterface():
    networkCard = netifaces.interfaces()
    addressDictionary = {}
    for netActive in networkCard:
        a = netifaces.ifaddresses(netActive)
        if a.__len__() != 0:
            if a.has_key(2) and a[2][0].has_key('broadcast'):
                value = a[2][0]['addr'] + " - " + a[2][0]['netmask']+"-"+a[2][0]['broadcast']
                addressDictionary[netActive] = value
    return addressDictionary

def netBlocks(sfield, afield):
    subnetOnes = bin(int(sfield)).count("1")
    nSubnet = int(math.pow(2, subnetOnes))
    nBlocks = int(math.pow(2, 8 - subnetOnes))
    listSubnetBlocks=[]
    for i in range(0, nSubnet+1):
        listSubnetBlocks.append(i * nBlocks)

    isempty = (listSubnetBlocks and True) or False
    a = min(x for x in listSubnetBlocks if x > int(afield))

    subnetNetwork = [a-nBlocks, a - 1]
    return subnetNetwork

def retrieveNetwork(subnet, address):
    global subnetNetwork
    subnetField = str.split(subnet, '.')
    addressField = str.split(address, '.')
    listSubnetBlocks = list()
    nbit=bin(int(subnetField[1])).count("1")
    networkID=[]
    if nbit < 8:
        if nbit !=0:
            subnetNetwork=netBlocks(subnetField[1],addressField[1])
            networkID = [str(addressField[0]) + "." + str(subnetNetwork[0]) + ".0.0"]
        else:
            networkID = [str(addressField[0]) + ".0.0.0"]
            subnetNetwork=[0,255]
    else:
        nbit = bin(int(subnetField[2])).count("1")
        if nbit<8:
            if nbit!=0:
                subnetNetwork =netBlocks(subnetField[2],addressField[2])
                networkID = [str(addressField[0]) + "." + str(addressField[1])+"."+ str(subnetNetwork[0]) + ".0"]
            else:
                networkID = [str(addressField[0]) +"."+ str(addressField[1])+".0.0"]
                subnetNetwork = [0, 255]
        else:
            nbit = bin(int(subnetField[3])).count("1")
            if nbit<8:
                if nbit!=0:
                    subnetNetwork = netBlocks(subnetField[3], addressField[3])
                    networkID = [str(addressField[0]) + "." + str(addressField[1]) + "." + str(addressField[2]) +"."+ str(subnetNetwork[0])]
                else:
                    networkID = [str(addressField[0]) + "." + str(addressField[1]) + "." + str(addressField[2]) + ".0"]
                    subnetNetwork = [0, 255]


    return networkID,subnetNetwork



def getNetHostAddressFromNetId(netID,subnet):
    subnetField = str.split(subnet, '.')
    a=netID[0]
    hostBase=str.split(str(netID[0][0]),'.')
    hostInTheSubnet=[]

    for x in range(netID[1][0],netID[1][1]+1):
        if int(subnetField[1])!= 255:
            for y in range (0,255):
                for z in range (0,255):
                    hostInTheSubnet.append(hostBase[0]+"."+str(x)+"."+str(y)+"."+str(z))
        elif int(subnetField[2])!= 255:
            for z in range(0, 255):
                hostInTheSubnet.append(hostBase[0] + "." + hostBase[1] + "." + str(x) + "." + str(z))
        else:
            hostInTheSubnet.append(hostBase[0] + "." + hostBase[1] + "." + hostBase[2] + "." + str(x))

    return hostInTheSubnet



