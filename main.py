#This module contains the socket connection
import socket
import threading #for multiple process


host = '127.0.0.1' #localhost
port = 55555  #do not use 0 to 40000, as they are reserved

#starting the server
#AF_INET is for the type of addresses that makes connection (Internet) and SOCK_STREAM is for tcp connections
#AF_INET is for the type of addresses that makes connection (Internet) and SOCK_STREAM is for tcp connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port)) #server is binding
server.listen() #now its in listening mode

               
instructions = '\nList of commands:\n' \
               '1.$list to list all the rooms\n' \
               '2.$join roomname to join or create the room\n' \
               '3.$personal name message to send personal message\n' \
               '4.$help to list all the commands\n' \
               '5.$quit to quit\n' \
               '6.$leave to leave the room'
               #'7.$switch roomname to switch room'

#now create a empty list and dict for data storage
clients = []
nicknames = []
roomdetails = {}
users = {}
users_in_room = {}

#to broadcast the message
def broadcast(message, roomname):
    for client in roomdetails[roomname].peoples:
        msg = '['+roomname+'] '+message
        client.send(msg.encode('utf-8'))
