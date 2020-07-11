#python 3
# Assignment 3
# An HTTP(hypertext transfer protocol) Request in Python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # make a socket
mysock.connect(('data.pr4e.org', 80))    # socket connected
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()    # http command
mysock.send(cmd)  # it's http, so we are making a send request to server first

while True:
    data = mysock.recv(512) # we are receiving request from server.
    if (len(data) < 1):
        break
    print(data.decode())    # if we did get data, we decode it.
mysock.close()    # close the socket.
