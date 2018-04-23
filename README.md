# DHCP-starvation-using-Python
DHCP Starvation Attack is when an attacker bind all usable IP addresses on a DHCP
server and perform a Denial of Service on the network. Performed this attack
on the External Router rtr. 

Rather than completing the entire DHCP handshake/protocol, stepped in to
the last portion by sending a request from a spoofed MAC address and recieved a DHCP
ACK back from the router confirming a 24hr binding to a bogus MAC address. This was done per IP address in the range of 10.10.111.100 - 10.10.111.200 
