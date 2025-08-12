tcompte=[]
client=[]
out = True
num=True

while out == True :
    print("----------bienvenue sur orange money senegal !!!----------")
    print("1-Créer un compte (nom, numéro, PIN, solde initial)")
    print("2-Afficher tous les comptes")
    print("3-Lister les comptes d’un client")
    print("4-Recharger un compte")
    print("5-Transférer de l’argent")
    print("6-Afficher l’historique des transferts")
    print("7-Quitter")
    choix=input("choisissez une option entre 1 et 7 : ")
    while not (choix.isdigit()) or int(choix)<1 or int(choix)>7 :
        choix=input("valeur saisi non valide veuillez retaper une valeur : ")
    choix=int(choix)
    if choix == 1:
        # 1-Créer un compte (nom, numéro, PIN, solde initial)
        client=[]
        nomclient=input("saissisez un nom : ")
        while (not nomclient.isalpha()) or len(nomclient) ==1:
            nomclient=input("valeur saisi non valide veuillez retaper un nom valide d'au moins deux carateres et contenant que des lettres : ")
        client.append(nomclient)

        prenomclient=input("saissisez un prenom : ")
        while (not prenomclient.isalpha()) or len(prenomclient) ==1:
            prenomclient=input("valeur saisi non valide veuillez retaper un nom valide d'au moins deux carateres et contenant que des lettres : ")
        client.append(prenomclient)

        # numero de telephone...
        numeroclient=input("saissisez votre numero de telephone : ")
        while (not numeroclient.isdigit()) or int(numeroclient)<770000000 or int(numeroclient)>=790000000:
            numeroclient=input("numero de telephone saisi non valide veuillez retaper un numero valide : ")
        client.append(numeroclient)

        # mot de passe
        num=True
        while num==True:
            # premiere saisi
            mdpclient=input("enregistrer un mot de passe (uniquement des chiffres) : ")
            while not(mdpclient.isdigit()) or len(mdpclient)<4:
                mdpclient=input("mot de passe saisi non valide, retapez un mot de passe : ")
            mdpclient=int(mdpclient)
            # deuxieme saisi
            mdp2client=input("saisissez une deuxieme fois votre mot de passe : ")
            while not(mdp2client.isdigit()):
                mdp2client=input("retapez le mot de passe : ")
            mdp2client=int(mdp2client)
            if mdpclient != mdp2client :
                print("les mots de passe saisi ne correspondent pas !!!")
                num=True
            else:
                print("mot de passe enregistrer !!!")
                client.append(mdpclient)
                num=False
        
        # solde initial
        soldeinclient=0
        client.append(soldeinclient)
        tcompte.append(client)
    if choix == 2 :
        # 2-Afficher tous les comptes
        v=1
        for i in tcompte :
            print(v,"-",i)
            v+=1
    
    # if choix == 3 :
        # 3-Lister les comptes d’un client
    
    if choix == 4 :
        # 4-Recharger un compte
        nom_client_recharge=input("saisissez le nom du client a recharger : ")
        while not(nom_client_recharge.isalpha()):
            nom_client_recharge=input("resaisissez le nom du client : ")
        for i in tcompte:
            if nom_client_recharge == client[0]:
                print(i)
            else:
                print("compte non trouver !")

    if choix == 7 :
        # 7-quitter le service orange money
        print("---merci d'avoir utiliser orange money et a bientot sur notre plate-forme !!!---")
        out = False