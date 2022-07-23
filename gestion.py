""" plateforme de gestion de budget en sqlite 3 """
import sqlite3

name = input ("saisir votre nom : ")

#categorie depense
print("*****Taper entre et saisie vos de type de depense*****")
loyer         = int(input("Entrer vos depenses pour le Loyer : "))
manger        = int(input("Entrer vos depenses pour la nourriture : "))
transport     = int(input("Entrer vos depenses pour le transport : "))
autresdepense = int(input("Entrer vos autres depenses : "))

#depense egal sommes des depenses

depense= loyer + manger + transport + autresdepense

#categorie revenues
print("*****Taper entrer et saisie vos de type de depense*****")
bussiness      = int (input("Entrer vos revenues sur votre bussiness : "))
salaire        = int (input("Entrer votre salaire : "))
autrerevemue   = int (input("Entrer vos autres sources de revenue : "))

#revenue egal a la somme des revenues
revenue = bussiness + salaire + autrerevemue

#ecart entre depense et revenue #

ecart = revenue - depense
#connexion a la base de donne sqlite 3#
conn = sqlite3.connect('Mon_Gestion_Budget.db')
cur  = conn.cursor()
"""
#creation table budget
req = "create table gestion (id integer primary key autoincrement,name text not null,depense integer not null, revenue integer not null,ecart integer not null)"

#executer la table
cur.execute(req)
"""

#insertion une ligne de donnee #
#cur.execute("Insert into gestion (`name` , `depense` , `revenue`,`ecart`)  values (?, ?, ?,?)" ,(name, depense,revenue,ecart))

"""base=cur.execute("select * from gestion;")
input(base)
for c in base :
    input(c[0],c[1])"""

#sauvegarde la connexion 
conn.commit()

#fermer la connextion
conn.close()


