from ftplib import FTP
from datetime import datetime
import tempfile
  

def main ():

    try:
            ftp = FTP('127.0.0.1')   # connect to host, default port
            ftp.login("admin","12345")
    except:
            print('serveur eteint')
            exit()

    curDT = datetime.now()
    date = curDT.strftime("%m-%d-%Y_%H-%M-%S")
    new_file = "Audit_"+date
    root = ftp.pwd()
    filename = ["Rennes","Grenoble","Strasbourg"]




    ftp.cwd("Paris")
    ftp.cwd("Save")

    ftp.mkd(new_file)
    ftp.cwd(new_file)
    for name in filename:
        ftp.mkd(name)

    for name in filename:
        ftp.cwd(root)
        try:
            ftp.cwd(name)
            ftp.cwd("Audit")
            for name2 in ftp.nlst():
                command = "RETR "+name2
                temp = tempfile.TemporaryFile()
                try:
                    ftp.retrbinary(command , temp.write, 8*1024)  
                    command = "STOR "+name2
                    ftp.cwd(root)
                    ftp.cwd("Paris")
                    ftp.cwd("Save")
                    ftp.cwd(new_file)
                    ftp.cwd(name)
                    ftp.storbinary(command, temp) 
                    temp.close()
                    ftp.cwd(root)
                    ftp.cwd(name)
                    ftp.cwd("Audit")
                except:
                    continue
        except:
            continue

    return new_file

    
