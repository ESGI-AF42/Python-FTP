from asyncio.windows_events import NULL
import os,sys,time
from sqlite3 import connect
from ftplib import FTP
from shutil import unregister_unpack_format
from threading import Thread
import server

try:
        ftp = FTP('127.0.0.1')   # connect to host, default port
except:
        print('serveur eteint')
        exit()


def main ():

    connected = False
    while not connected:
        try:
            username = input("Username : ")
            password = input("Password : ")
            ftp.login(username,password)
            connected = True
        except:
            print(" ")
            slow_print("mauvais credential, veuillez réessayer")
            time.sleep(1)
            clearConsole()


    while True:
        app_start()




def app_start():
    clearConsole()
    print("Vous etes dans : " + ftp.pwd())
    slow_print("0 : naviguer")
    slow_print("1 : Voir repertoire")
    slow_print("2 : créer un dossier")
    slow_print("3 : supprimer un dossier/fichier") 
    slow_print("4 : upload un fichier")
    print(" ")
    time.sleep(0.25)
    i = int(input("Veuillez choisir : "))

    while i < 0 or i > 4:
        slow_print("Valeur incorrect, veuillez choisir un chiffre entre 1 et 5")
        time.sleep(2)
        clearConsole()
        print("Vous etes dans : " + ftp.pwd())
        print("0 : naviguer")
        print("1 : Voir repertoire")
        print("2 : créer un dossier")
        print("3 : supprimer un dossier/fichier") 
        print("4 : upload un fichier")
        print(" ")
        i = int(input("Veuillez choisir : "))
            
    if i == 0:
        navigate()
    if i == 1:
        list_rep()
    if i == 2:
        create_rep()
    if i == 3:
        delete()
    if i == 4:
        upload_file()
 

def navigate():
    clearConsole()
    print("Dans quel fichier voulez-vous aller")
    file,filename , cpt = list_file_with_number()
    correct_numbers = []
    for i in range(0,cpt):
        if file[i].startswith("d"):
            correct_numbers.append(i)
            to_print = str(i) + " : " + filename[i]
            slow_print(to_print)
    print(" ")
    time.sleep(0.25)
    j = int(input("Veuillez choisir : "))
    while j not in correct_numbers:
        slow_print("Valeur incorrect, veuillez choisir un chiffre dans la liste")
        time.sleep(2)
        clearConsole()
        print("Dans quel fichier voulez-vous aller")
        for i in range(0,cpt):
            if file[i].startswith("d"):
                to_print = str(i) + " : " + filename[i]
                print(to_print)
        print(" ")
        j = int(input("Veuillez choisir : "))
    ftp.cwd(filename[i])

def list_rep():
    clearConsole()
    ftp.retrlines('LIST') 
    input("Presser entrer pour continuer")
    Thread.start_new_thread(server.this_ftp.add_user,('userA','12345',".",'elradfmwM'))

def create_rep():
    clearConsole()
    print("cré un dossier")

def delete():
    clearConsole()
    print("suppr un dossier/fichier")

def upload_file():
    clearConsole()
    print("up un fichier")

def upload_file():
    clearConsole()
    print("down un fichier")


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

def slow_print(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
    print('')

def list_file_with_number():
    file = []
    file_name = []
    ftp.dir(file.append)
    cpt = 0   
    for name in ftp.nlst():
        file_name.append(name)
        cpt = cpt + 1

    return file, file_name , cpt



   
main()