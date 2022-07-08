import os,pathlib,time
actual_path= pathlib.Path(__file__ )
parent_path = actual_path.parent.__str__()
fic = os.path.join(parent_path,"mdp_plus_probable.txt")
mdp = ''


def bruteforce(word, length):
    taille = len(mdp)
    if taille > 8:
        print("Votre mot de passe est trop long pour être testé avec du bruteforce.")
    if length <= taille:
        for i in range(34,128):
            if mdp == word + chr(i):
                password = word + chr(i)
                print('votre mot de passe est ', password)
                print('Veuillez patienter pendant le chargement')
                break
            else:
                bruteforce(word + chr(i), length + 1)



def dico_atk(fic,mdp):
        with open(fic, newline='') as file:
            data = file.read().splitlines()
            for pwd in data:
                if mdp == pwd:
                    print("Le mot de passe a été trouvé dans le dictionnaire. Il n'est donc pas sécurisé")
                    time.sleep(2)
                    break
                else:
                    continue

def main():
    global mdp
    mdp = str(input("Veuillez saisir votre mot de passe : "))
    chx = int(input("Veuillez sélectionner le type d'attaque voulu (saisissez 1 ou 2):\n1) Bruteforce\n2) Dictionnaire\n"))
    try:
        if chx == 1:

            start = time.time()
            bruteforce('',1)
            end = time.time()
            print('Total time: %.2f seconds' % (end - start))
            time.sleep(2)
            
            
        elif chx == 2:
            dico_atk(fic,mdp)
            print("si aucun message n'est apparu, votre mot de passe ne ce situe pas dans le dictionnaire")
            
        else:
            print("Vous n'avez pas choisi parmis Bruteforce ou Dictionnaire. Veuillez recommencer.")
            main()
    except ValueError:
        print("La valeur rentrée n'est pas correcte. Veuillez saisir uniquement 1 ou 2.")
        main()
