import pathlib
from user import User
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer

actual_path= pathlib.Path(__file__ )
parent_path = actual_path.parent.__str__()
FTP_path = parent_path+'\\FTP\\'
HOST = "127.0.0.1"
PORT = 21
      
authorizer = DummyAuthorizer()
handler = FTPHandler
user_list=User.load_user_from_csv()# permet de charger tous les utilisateurs de la base de donnée lors du lancement du serveur
#uniquement pour faciliter le lancement du serveur ftp en python pour les tests, n'a pas pour but d'être une solution valable en entreprise
for user in user_list:
    if user.get_user_status() == 'admin':
        authorizer.add_user(user.get_user_nickname(), user.get_user_password(), homedir=FTP_path, perm='elradfmwMT')

    elif user.get_user_site() == 'P':
        authorizer.add_user(user.get_user_nickname(), user.get_user_password(), homedir=FTP_path+'\\Paris\\', perm='elradfmwMT')

    elif user.get_user_site() == 'R':
        authorizer.add_user(user.get_user_nickname(), user.get_user_password(), homedir=FTP_path+'\\Rennes\\', perm='elradfmwMT')

    elif user.get_user_site() == 'S':
        authorizer.add_user(user.get_user_nickname(), user.get_user_password(), homedir=FTP_path+'\\Strasbourg\\', perm='elradfmwMT')

    elif user.get_user_site() == 'G':
        authorizer.add_user(user.get_user_nickname(), user.get_user_password(), homedir=FTP_path+'\\Grenoble\\', perm='elradfmwMT')

handler.authorizer = authorizer
address = (HOST, PORT)
server = FTPServer(address, handler)
server.serve_forever()

