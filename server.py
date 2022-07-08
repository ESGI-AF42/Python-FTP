import pathlib, logging, os,threading
from user import User
from datetime import datetime
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import save


def Scheduled_Task(): 
    save.main()
    t = threading.Timer(86400,Scheduled_Task).start()



actual_path= pathlib.Path(__file__ )
parent_path = actual_path.parent.__str__()
path_log = os.path.join(parent_path,"FTP\\Paris\\Logs")
FTP_path = parent_path+'\\FTP\\'


HOST = "127.0.0.1"
PORT = 21


authorizer = DummyAuthorizer()
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

handler = FTPHandler
handler.authorizer = authorizer
curDT = datetime.now()
date = curDT.strftime("%m-%d-%Y_%H-%M-%S")
new_file = "Logs_"+date+".log"
join_log = os.path.join(path_log, new_file)
logging.basicConfig(filename=join_log, level=logging.INFO)
address = (HOST, PORT)
Scheduled_Task()
server = ThreadedFTPServer(address, handler)
print('serveur lancé')
server.serve_forever()










    

   