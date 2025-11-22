import mysql.connector
from models import Produit, Client

class MySQLDao:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="boutique"
            )
            self.cursor = self.conn.cursor()
            print("Connexion MySQL reussie ")
        except Exception as e:
            print("Erreur connexion MySQL :", e)


    def ajouter_produit(self, nom, prix):
        self.cursor.execute(
            "INSERT INTO produit (nom, prix) VALUES (%s, %s)", (nom, prix)
        )
        self.conn.commit()
        print("Produit ajoute  avec succes")

    def lister_produits(self):
        self.cursor.execute("SELECT * FROM produit")
        for id, nom, prix in self.cursor.fetchall():
            print(Produit(id, nom, prix))

    def modifier_prix(self, id_prod, nouveau_prix):
        self.cursor.execute(
            "UPDATE produit SET prix=%s WHERE id=%s",
            (nouveau_prix, id_prod)
        )
        self.conn.commit()
        print("Prix modifie avec succes ")


    def ajouter_client(self, nom, email):
        try:
            self.cursor.execute(
                "INSERT INTO client (nom, email) VALUES (%s, %s)",
                (nom, email)
            )
            self.conn.commit()
            print("Client ajoute  avec succes")
        except mysql.connector.IntegrityError:
            print("Email deja utilise !")

    def lister_clients(self):
        self.cursor.execute("SELECT * FROM client")
        for id, nom, email in self.cursor.fetchall():
            print(Client(id, nom, email))

    def chercher_client_email(self, email):
        self.cursor.execute(
            "SELECT * FROM client WHERE email=%s", (email,)
        )
        row = self.cursor.fetchone()
        if row:
            print(Client(*row))
        else:
            print("Aucun client trouve.")


    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Connexion MySQL fermee ")
