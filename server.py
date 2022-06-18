from collections import UserList
import socket
from threading import Thread
from user import User
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer

HOST = "127.0.0.1"
PORT = 21
authorizer = DummyAuthorizer()
address = (HOST, PORT)  # listen on every IP on my machine on port 21

server = servers.FTPServer(address, FTPHandler)
user_list=User.load_user_from_csv()# récupère la liste de tous les utilisateurs qui se sont une fois connecté
print(user_list)
authorizer.add_user('user', '12345', '.', perm='elradfmwMT')
for user in user_list:
    authorizer.add_user(user.get_user_nickname(), user.get_user_password(), '.', perm=user.get_user_status())

server.serve_forever()
