from time import time
import socket  
import os

def main():
    nbPortToScan = 65536
    nbPortToScanporcent = int(nbPortToScan/100)
    port_dict = dict()
    os.system('cls')
    print("SCAN EN COURS:")
    print("0%")
    start = time()
    for i in range(nbPortToScan):
        value=""

        test = i/nbPortToScanporcent

        if (test).is_integer():
            os.system('cls')
            print("SCAN EN COURS:")
            print(int(test),"%")
            
        try:
            value = socket.getservbyport(i)
        except:
            IndexError
            pass

        if value != "":
            port_dict[i]=value


    end = time() 
    duration =  end - start      
    os.system('cls')
    print("SCAN TERMINE: ",len(port_dict), " ports ouverts")
    print("100%")
    print(f'Le process a durée : {duration}s')
    print("")
    input("Presser entrer pour continuer")


    print ("{:<5} {:<13}".format('Port','Service'))
    for key, value in port_dict.items():
        Serv = value
        print ("{:<5} {:<13}".format(key, Serv))
        
    input("Presser entrer pour continuer")