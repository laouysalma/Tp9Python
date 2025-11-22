from mysql_dao import MySQLDao

dao = MySQLDao()

print("Application de gestion – Produits et Clients\n")

while True:
    print("\nMenu principal")
    print("1. Ajouter un produit")
    print("2. Afficher tous les produits")
    print("3. Modifier le prix d’un produit")
    print("4. Ajouter un client")
    print("5. Afficher tous les clients")
    print("6. Rechercher un client par email")
    print("0. Quitter l’application")

    choix = input("veuillez saisir votre  choix (1/2/3/4/5/6/0) : ")

    if choix == "1":
        nom = input("Nom du produit : ")
        prix = float(input("Prix du produit : "))
        dao.ajouter_produit(nom, prix)

    elif choix == "2":
        print("\nListe des produits :")
        dao.lister_produits()

    elif choix == "3":
        idp = int(input("Identifiant du produit : "))
        newp = float(input("Nouveau prix : "))
        dao.modifier_prix(idp, newp)

    elif choix == "4":
        nom = input("Nom du client : ")
        email = input("Adresse email : ")
        dao.ajouter_client(nom, email)

    elif choix == "5":
        print("\nListe des clients :")
        dao.lister_clients()

    elif choix == "6":
        email = input("Email a rechercher : ")
        dao.chercher_client_email(email)

    elif choix == "0":
        dao.close()
        print("Fermeture de l’application.")
        break

    else:
        print("Choix inavlie veuillez saisir le numero de choix  .")
