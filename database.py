import sqlite3

#creation table budget
create_table_Gestion = """CREATE TABLE IF NOT EXISTS gestions (
                                id integer primary key autoincrement,
                                name text not null,
                                depense integer not null, 
                                revenue integer not null
                                ,ecart integer not null
                            );"""

insertion_table = "INSERT INTO gestions ('name' ,'depense', 'revenue' , 'ecart' ) values (?, ?, ?, ?); "

#lister tous les elements
AFFICHER_BASE = "select * from gestions;"
#lister tous les elements par rapport a leur nom

#connexion et creation de la base
def connect() :
    return  sqlite3.connect("Mabase.db")

#creation de la table graine et execution
def create_tables(connection) :
     with connection :
          connection.execute (create_table_Gestion)

def ajouter_Donnees( connection, name, depense,revenue,ecart) :
    with connection :
          connection.execute (insertion_table , (name, depense, revenue, ecart))

def afficher_base( connection) :
    with connection :
         return connection.execute (AFFICHER_BASE).fetchall()
