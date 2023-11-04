
import random
import re
import math

argent = 0


# Fonction pour enregistrer un étudiant
def enregistrer_joueur():
    nomprenom = input("Entrez le nom et le prenom au format (noprenom) : ")
    while True:

        email = input(f"Entrez l'adresse e-mail au format 'nomprenom@gmail.com' : ")

        if email == f"{nomprenom}@gmail.com":
            print("Adresse e-mail valide.")
            break
        else:
            print("L'adresse e-mail n'est pas au format attendu ('nomprenom@gmail.com'). Veuillez réessayer.")

    while True:
        mot_de_passe = input(
            "Entrez un mot de passe (8 à 12 caractères, au moins une minuscule, une majuscule, un chiffre et un caractère spécial) : ")
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,12}$", mot_de_passe):
            break
        else:
            print("Le mot de passe ne respecte pas les critères. Veuillez réessayer.")

    with open("Enregistrement.txt", "a") as file:
        file.write(f"{nomprenom}:{email}:{mot_de_passe}\n")
    print(f"Inscription de {nomprenom} réussie.")


# Fonction pour authentifier un utilisateur
def authentifier():
    email = input("Entrez votre adresse e-mail : ")
    mot_de_passe = input("Entrez votre mot de passe : ")

    with open("Enregistrement.txt", "r") as file:
        credentials = [line.strip().split(':') for line in file]

    for user_data in credentials:
        if len(user_data) == 3:
            user, saved_email, saved_pwd = user_data
            if email == saved_email and mot_de_passe == saved_pwd:
                return user
    return None


# Fonction pour afficher le menu
def afficher_menu_principal():
    if utilisateur is not None:
        print(f"Bonjour, {utilisateur}!")
        print("Menu :")
        print("A- Jouer à la Roulette")
        print("B- Décalage par CESAR")
    else:
        print("Utilisateur non authentifié. Veuillez vous enregistrer.")
    print("0- Quitter")


def menu_roulette():
    while True:
        print("Menu Roulette:")
        print("a- Commencer à jouer")
        print("b- Revenir au menu principal")
        choix_roulette = input("Sélectionnez une option (a, b) : ").lower()

        if choix_roulette == "a":
            jouer_roulette()
        elif choix_roulette == "b":
            break
        else:
            print("Option invalide.")


def jouer_roulette():
    argent = int(input("donner votre solde : "))
    while argent > 0:
        mise = 0
        numero_joueur = -1
        numero_gagnant = random.randint(0, 36)

        print(f"Argent restant : {argent}")

        while True:
            try:
                mise = int(input("Combien voulez-vous miser (0 pour quitter) ? "))
                if mise == 0:
                    return argent  # Le joueur quitte le jeu
                elif mise > argent:
                    print("Vous ne pouvez pas miser plus que ce que vous avez.")
                else:
                    break
            except ValueError:
                print("Veuillez saisir un nombre entier.")

        while numero_joueur < 0 or numero_joueur > 36:
            try:
                numero_joueur = int(input("Choisissez un numéro entre 0 et 36 : "))
            except ValueError:
                print("Veuillez saisir un nombre entier.")

        print(f"Numéro joueur : {numero_joueur}")
        print(f"Numéro gagnant : {numero_gagnant}")

        if numero_joueur == numero_gagnant:
            gains = 36 * mise
        else:
            gains = -mise

        argent += gains

        if gains > 0:
            print(f"Vous avez gagné {gains} jetons!")
        else:
            print(f"Vous avez perdu {abs(gains)} jetons.")

    print("Vous n'avez plus d'argent. Fin de la partie.")
    return argent


# Fonction pour le menu César avec sous-menus
def menu_cesar():
    while True:
        print("Menu César:")
        print("A- Commencer à jouer ")
        print("B- Retour au menu principal")
        choix_cesar = input("Sélectionnez une option (A, B) : ").upper()

        if choix_cesar == "A":
            text = str(input("Entrez le texte à chiffrer : "))
            shift = int(input("Entrez le décalage (entier) : "))
            menu_chiffrement_cesar(text, shift)
        elif choix_cesar == "B":
            break
        else:
            print("Option invalide.")


# Fonction pour le sous-menu de chiffrement César
def menu_chiffrement_cesar(text, shift):
    while True:
        print("Menu Chiffrement César:")
        print("1- Cesar avec code ASCII")
        print("2- Cesar avec 26 lettres")
        print("W- Revenir au menu César")
        choix_chiffrement = input("Sélectionnez une option (1, 2, W) : ")

        if choix_chiffrement == "1":
            cesar_code_ascii(text, shift)

        elif choix_chiffrement == "2":
            cesar_26_lettres(text, shift)

        elif choix_chiffrement == "W":
            break
        else:
            print("Option invalide.")


def cesar_code_ascii(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            # Modifiez cette partie pour gérer les chiffres
            if char.isdigit():
                result += str((int(char) + shift) % 10)
            else:
                result += char
    print(f"Texte chiffré : {result}")
    try:
        choix = int(input("  1-pour rejouer ou 0- pour quitter : "))
        if choix == 0:
            return
        elif choix == 1:
            cesar_code_ascii(text, shift)
        else:
            print("choix invalide")
    except ValueError:
        print("Entrez un choix valide (0 ou 1)")


# Fonction pour le chiffrement César dans les 26 lettres
def cesar_26_lettres(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += char
    print(f"Texte chiffré : {result}")
    try:
        choixx = int(input("  1-pour rejouer ou 0- pour quitter : "))
        if choixx == 0:
            return
        elif choixx == 1:
            cesar_26_lettres()
        else:
            print("choix invalide")
    except ValueError:
        print("Entrez un choix valide (0 ou 1)")


# Programme principal
while True:

    while True:
        while True:
            print("1- Enregistrement")
            print("2- Authentification")
            choix = input("Choisissez une option (1/2) : ")

            if choix == "1":
                enregistrer_joueur()
            elif choix == "2":
                utilisateur = authentifier()
                if utilisateur is not None:
                    while True:
                        afficher_menu_principal()
                        choix_menu = input("Sélectionnez une option du menu (A, B, 0) : ").upper()
                        if choix_menu == "A":
                            menu_roulette()
                        elif choix_menu == "B":
                            menu_cesar()
                        elif choix_menu == "0":
                            break  # Quitter le menu principal
                        else:
                            print("Option invalide.")
                else:
                    print("Authentification échouée")
            else:
                print("Option invalide. Veuillez choisir 1 ou 2.")
