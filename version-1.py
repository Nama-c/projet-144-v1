tcompte=[]
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
        nom=input("saissisez un nom : ")
        while (not nom.isalpha()) or len(nom) ==1:
            nom=input("valeur saisi non valide veuillez retaper un nom valide d'au moins deux carateres et contenant que des lettres : ")

        prenom=input("saissisez un prenom : ")
        while (not prenom.isalpha()) or len(prenom) ==1:
            prenom=input("valeur saisi non valide veuillez retaper un nom valide d'au moins deux carateres et contenant que des lettres : ")

        # numero de telephone...
        numero=input("saissisez votre numero de telephone : ")
        while (not numero.isdigit()) or int(numero)<770000000 or int(numero)>=790000000:
            numero=input("numero de telephone saisi non valide veuillez retaper un numero valide : ")

        # mot de passe
        num=True
        while num==True:
            # premiere saisi
            mdp=input("enregistrer un mot de passe (uniquement des chiffres) : ")
            while not(mdp.isdigit()) or len(mdp)<4:
                mdp=input("mot de passe saisi non valide, retapez un mot de passe : ")
            mdp=int(mdp)
            # deuxieme saisi
            mdp2=input("saisissez une deuxieme fois votre mot de passe : ")
            while not(mdp2.isdigit()):
                mdp2=input("retapez le mot de passe : ")
            mdp2=int(mdp2)
            if mdp != mdp2 :
                print("les mots de passe saisi ne correspondent pas !!!")
                num=True
            else:
                print("mot de passe enregistrer !!!")
                num=False
        
        # solde initial
        client = {
            "numero":numero,
            "nom":nom,
            "prenom":prenom,
            "mot de passe":mdp,
            "solde":0,
            "transfert":[]
        }
        tcompte.append(client)
    if choix == 2 :
        # 2-Afficher tous les comptes
        v=1
        print("-----voici la liste des comptes orange money-----")
        for i in tcompte :
            print(v,"-",i)
            v += 1

    # if choix == 3 :
        # 3-Lister les comptes d’un client
    
    if choix == 4 :
        # 4-Recharger un compte
        soldeclient=0
        num_client_recharge=input("saisissez le numero d'identification du client a recharger : ")
        while not(num_client_recharge.isdigit()):
            num_client_recharge=input("resaisissez le numero d'identification du client : ")
        for i in tcompte:
            if num_client_recharge == num_identification:
                soldeclient=input("saisissez le montant de recharge : ")
                while not soldeclient.isdigit() or int(soldeclient)<=0 :
                    soldeclient=input("saisissez le montant de recharge : ")
                soldeclient=int(soldeclient)
                soldeinclient.append(soldeclient)
            else:
                print("compte non trouver !")

    if choix == 7 :
        # 7-quitter le service orange money
        print("---merci d'avoir utiliser orange money et a bientot sur notre plate-forme !!!---")
        out = False
