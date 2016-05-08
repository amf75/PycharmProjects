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