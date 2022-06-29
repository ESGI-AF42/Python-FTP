from asyncio.windows_events import NULL
import os,sys,time
from sqlite3 import connect
from ftplib import FTP
from shutil import unregister_unpack_format

username = ""

try:
        ftp = FTP('127.0.0.1')   # connect to host, default port
except:
        print('serveur eteint')
        exit()

#debut
def main ():

    connected = False
    while not connected:
        try:
            global username 
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



#debut
def app_start():
    clearConsole()
    print("Vous etes dans : " + ftp.pwd())
    slow_print("0 : naviguer")
    slow_print("1 : Voir repertoire")
    slow_print("2 : créer un dossier")
    slow_print("3 : supprimer un dossier/fichier") 
    slow_print("4 : upload un fichier")
    slow_print("5 : download un fichier")
    slow_print("6 : Quit")
    if username == "admin":
        slow_print("7 : bruteforce")
        slow_print("8 : Forcer sauvegarde fichier d'Audit")
    print(" ")
    time.sleep(0.25)

    i = int(input("Veuillez choisir : "))

    if username == "admin":
        if i < 0 or i > 8 :
            slow_print("Valeur incorrect, veuillez choisir un chiffre entre 0 et 8")
            time.sleep(2)
            clearConsole()
            app_start()
            
    else:
        if i < 0 or i > 6 :
            slow_print("Valeur incorrect, veuillez choisir un chiffre entre 0 et 6")
            time.sleep(2)
            clearConsole()
            app_start()
        
            
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

    if i == 6:
        clearConsole()
        slow_print("Vous allez être déconnecté")
        time.sleep(2)
        ftp.close()
        quit()

    if i == 7:
        start_brut()

    if i == 8:
        force_audit_save()
    
 
#debut
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
    ftp.cwd(filename[j])

#debut
def list_rep():
    clearConsole()
    ftp.retrlines('LIST') 
    input("Presser entrer pour continuer")


#debut
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
    

#debut
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


#debut
def upload_file():
    slow_print("écrivez le chemin exact du dossier contenant le fichier que vous souhaitez envoyer (sans \\ à la fin)")
    file_path = input()
    slow_print("Quel fichier voulez-vous charger ?")
    file_name = input()
    file_join = file_path+"\\"+file_name
    
    try:
        file = open(file_join,'rb')
        slow_print("Fichier chargé")
        while True:
            clearConsole()
            print("Voulez-vous vraiment uploader le fichier"+ file_name+" dans "+ ftp.pwd())
            upload_file = input("(y/n) : ")
            if upload_file == "y" or upload_file == "Y" or upload_file == "yes":
                command = "STOR "+file_name    
                try:
                    ftp.storbinary(command, file)     
                    slow_print("le fichier a été uploadé")
                except:
                    slow_print("le fichier n'a pas pu être uploadé")
                time.sleep(2)
                break
            
            elif upload_file == "n" or upload_file == "N" or upload_file == "no":
                slow_print("le fichier ne sera pas uploadé")
                time.sleep(2)
                break
            
            else:
                slow_print("réponse incorrect")
                time.sleep(0.25)
                slow_print("veuillez réessayer")
                time.sleep(1)
        file.close()
    except:
        slow_print("Le fichier " + file_join + " n'existe pas")   
        slow_print("annulation de l'upload, retour au menu principal") 
        time.sleep(1)

     


#debut
def download_file():
    clearConsole()
    print("Quel fichier voulez-vous download")
    files,filename , cpt = list_file_folder()
    correct_numbers = []
    for i in range(0,cpt):
        if not files[i].startswith("d"):
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
        print("Quel fichier voulez-vous download")
        for i in range(0,cpt):
            if not files[i].startswith("d"):
                to_print = str(i) + " : " + filename[i]
                print(to_print)
        print(" ")
        j = int(input("Veuillez choisir : "))

    try:
        path = os.getcwd()
        local_filename = os.path.join(r""+path, "Local\\Download")
        local_filename = os.path.join(r""+local_filename, filename[j])
        lf = open(local_filename, "wb")
        
        while True:
            clearConsole()
            print("Voulez-vous vraiment download le fichier"+ filename[j])
            down_file = input("(y/n) : ")
            if down_file == "y" or down_file == "Y" or down_file == "yes":
                command = "RETR "+filename[j]    
                try:
                    ftp.retrbinary(command , lf.write, 8*1024)  
                    slow_print("le fichier a été download")
                except:
                    slow_print("le fichier n'a pas pu être download")
                time.sleep(2)
                break
            
            elif down_file == "n" or down_file == "N" or down_file == "no":
                slow_print("le fichier ne sera pas download")
                time.sleep(2)
                break
            
            else:
                slow_print("réponse incorrect")
                time.sleep(0.25)
                slow_print("veuillez réessayer")
                time.sleep(1)
        local_filename.close()
    except:
        slow_print("Le fichier " + local_filename + " ne peux pas être créé")   
        slow_print("annulation du download, retour au menu principal") 
        time.sleep(1)


def start_brut():
    print("brute")

def force_audit_save():
    print("save_audit")

#debut
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)



#debut
def slow_print(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
    print('')



#debut
def list_file_folder():
    file = []
    filename = []
    ftp.dir(file.append)
    cpt = 0   
    for name in ftp.nlst():
        filename.append(name)
        cpt = cpt + 1

    return file, filename , cpt


#lancement du programme
main()