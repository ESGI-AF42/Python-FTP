from pickle import TRUE
import socket
from sqlite3 import connect
import threading
from threading import Thread
from datetime import datetime
import random


nickname = input("Choisissez votre Pseudo: ")
if nickname == 'admin':
    password = input("Enter Password for Admin:")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',21))

stop_thread = False

# Test connection 
def try_connect():
    a_socket = socket.socket()
    try :
        a_socket.connect(("127.0.0.1", 21)) # Tente de se connecter à l'adresse IP et au port suivant
        a_socket.shutdown(socket.SHUT_RDWR) # Essaye de se deconnecter du client ? verif que ça marche côté serveur 
        a_socket.close()
    except : 
        print("Le serveur ne répond pas")
        return False  


def client_connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1',21))


def receive():
    while True:
        global stop_thread
        if stop_thread:
            break    
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
                next_message = client.recv(1024).decode('utf-8')
                if next_message == 'PASS':
                    client.send(password.encode('utf-8'))
                    if client.recv(1024).decode('utf-8') == 'REFUSE':
                        print("Connection is Refused !! Wrong Password")
                        stop_thread = True
            else:
                split_message= message.split(': ')
                if split_message[0]!=nickname:
                    print(message)
        except:
            print('Error Occured while Connecting')
            client.close()
            break
        
def write(): 
    while True:
        if stop_thread:
            break
        #Getting Messages
        message = f'{nickname}: {input("")}'
        if message[len(nickname)+2:].startswith('/'):
            if nickname == 'admin':
                if message[len(nickname)+2:].startswith('/kick'):
                    # 2 for : and whitespace and 6 for /KICK_
                    client.send(f'KICK {message[len(nickname)+2+6:]}'.encode('utf-8'))
            else:
                print("Commands can be executed by Admins only !!")
        else:
            client.send(message.encode('utf-8'))

recieve_thread = threading.Thread(target=receive)
recieve_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()