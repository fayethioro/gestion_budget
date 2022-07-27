import sys
#on importe le paquetage database et ses modules
import database 
Menu = """
    Choississez parmi les 3 options suivantes :
    1: ajouter des donnes a la base
    2: voir toute la base 
    3: Quitter le programme
    👉 Votre choix svp : """
Choix_menu=["1", "2", "3"]

def  menu() :
    connection = database.connect()
    database.create_tables(connection)
    
    while True :
        mon_choix="" 
        while mon_choix not in Choix_menu :
              mon_choix=input(Menu)
              if mon_choix not in Choix_menu :
                 print("votre choix est incorrecte")
            
        if mon_choix == "1" :
                name = input ("saisir votre nom : ")

                #categorie depense
                print("*****Taper entre et saisie vos de type de depense*****")
                loyer = int (input("Entrer vos depenses pour le Loyer : "))

                manger = int (input("Entrer vos depenses pour la nourriture : "))

                transport = int (input("Entrer vos depenses pour le transport : "))

                autresdepense = int (input("Entrer vos autres depenses : "))

                #depense egal sommes des depenses
                
                depense= loyer + manger + transport + autresdepense

                #categorie revenues
                print("*****Taper entrer et saisie vos de type de depense*****")

                bussiness = int (input("Entrer vos revenues sur votre bussiness : "))

                salaire = int (input("Entrer votre salaire : "))

                autrerevenue = int (input("Entrer vos autres sources de revenue : "))

                #revenue egal a la somme des revenues
                revenue = bussiness + salaire + autrerevenue

                #ecart entre depense et revenue #
                ecart = revenue - depense
                database.ajouter_Donnees(connection ,name,depense,revenue,ecart)
              
        elif mon_choix == "2" :
            Ma_base = database.afficher_base(connection)
            for Donnee in Ma_base :
                print(f"{Donnee[0]}: Prenoms et nom :{Donnee[1]} ,RevenueTotal ={Donnee[3]}, DepenseTotal ={Donnee[2]}, Ecart ={Donnee[4]} ")

        elif mon_choix == "3" :
            print("A bientot")
            sys.exit()
    
    print("-" *50)

menu()