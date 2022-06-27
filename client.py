from asyncio.windows_events import NULL
import os,sys,time
from sqlite3 import connect
from ftplib import FTP
from shutil import unregister_unpack_format


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
    slow_print("5 : download un fichier")
    print(" ")
    time.sleep(0.25)

    i = int(input("Veuillez choisir : "))

    while i < 0 or i > 5:
        slow_print("Valeur incorrect, veuillez choisir un chiffre entre 0 et 5")
        time.sleep(2)
        clearConsole()
        print("Vous etes dans : " + ftp.pwd())
        print("0 : naviguer")
        print("1 : Voir repertoire")
        print("2 : créer un dossier")
        print("3 : supprimer un dossier/fichier") 
        print("4 : upload un fichier")
        print("5 : download un fichier")
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
    if i == 5:
        download_file()
 

def navigate():
    clearConsole()
    print("Dans quel dossier voulez-vous aller")
    file,filename , cpt = list_file_folder()
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

def create_rep():
    path = ftp.pwd()
    print("créer un dossier")
    newdir = input(path)
    pathjoin = os.path.join(path, newdir)
    try:
        ftp.mkd(pathjoin)
        slow_print("le dossier a été créé avec succès")
    except:
        slow_print("le dossier existe déjà")
        time.sleep(0.25)
        slow_print("il n'a pas pu être créer")      
        time.sleep(2)
    clearConsole()
    

def delete():
    clearConsole()
    print("Quel fichier/dossier voulez-vous supprimer")
    print("ATTENTION")
    print("s'il s'agit d'un dossier, tous les fichiers et sous dossiers seront suprimmés")
    file,filename , cpt = list_file_folder()
    for i in range(0,cpt):
        to_print = str(i) + " : " + filename[i]
        slow_print(to_print)
    print(" ")
    time.sleep(0.25)
    j = int(input("Veuillez choisir : "))
    while j not in range (0,cpt):
        slow_print("Valeur incorrect, veuillez choisir un chiffre dans la liste")
        time.sleep(2)
        clearConsole()
        print("Quel fichier/dossier voulez-vous supprimer")
        print("ATTENTION")
        print("s'il s'agit d'un dossier, tous les fichiers et sous dossiers seront suprimmés")
        for i in range(0,cpt):
            to_print = str(i) + " : " + filename[i]
            slow_print(to_print)
        print(" ")
        j = int(input("Veuillez choisir : "))

    while True:
        clearConsole()
        print("voulez-vous vraiment supprimer le fichier/dossier", filename[i])
        delete_file = input("(y/n) : ")
        if delete_file == "y" or delete_file == "Y" or delete_file == "yes":
            try:
                ftp.rmd(filename[i])
                slow_print("le dossier/fichier a été supprimé")
            except:
                slow_print("le dossier/fichier n'a pas pu être supprimé")
            time.sleep(2)
            break
        
        elif delete_file == "n" or delete_file == "N" or delete_file == "no":
            slow_print("le dossier/fichier ne sera pas supprimé")
            time.sleep(2)
            break
        
        else:
            slow_print("réponse incorrect")
            time.sleep(0.25)
            slow_print("veuillez réessayer")
            time.sleep(1)

def upload_file():
    clearConsole()
    print("up un fichier")

def download_file():
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

def list_file_folder():
    file = []
    filename = []
    ftp.dir(file.append)
    cpt = 0   
    for name in ftp.nlst():
        filename.append(name)
        cpt = cpt + 1

    return file, filename , cpt





   
main()