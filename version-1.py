tcompte=[]
out = True
num=True
historique=[]
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
                print("mot de passe enregistrer et compte creer !!!")
                num=False
        
        # solde initial
        client = {
            "numero":numero,
            "nom":nom.lower(),
            "prenom":prenom.lower(),
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
            print(f"{v} - {i['prenom'].capitalize()} {i['nom'].capitalize()} | Numéro: {i['numero']} | Solde: {i['solde']} F CFA")
            v += 1

    if choix == 3 :
        # 3-Lister les comptes d’un client
        v=1
        compteur=0
        client_nom=input("saisissez le nom du client a afficher les comptes : ").lower()
        while not client_nom.isalpha() or len(client_nom) ==1:
            client_nom=input("resaisissez le nom : ").lower()

        client_prenom=input("saisissez le prenom : ").lower()
        while not client_prenom.isalpha()  or len(client_prenom) ==1:
            client_prenom=input("resaisissez le prenom: ").lower()

        for client in tcompte :
            if client_nom == client["nom"] and client_prenom == client["prenom"]:
                print(v,"-",client)
                v += 1
                compteur += 1
        if compteur == 0:
            print("aucun compte trouver a ce nom !!! ")
    
    if choix == 4 :
        # 4-Recharger un compte
        compteur=0
        solde_recharge=0
        numero_client=input("saisissez le numero du client a recharger : ")
        while not(numero_client.isdigit()) or int(numero_client)<770000000 or int(numero_client)>=790000000:
            numero_client=input("resaisissez le numero du client : ")

        for client in tcompte:
            if numero_client == client["numero"]:
                solde_recharge=input("saisissez le montant de recharge : ")
                while not solde_recharge.isdigit() or int(solde_recharge)<=0 :
                    solde_recharge=input("saisissez un montant de recharge valide : ")
                solde_recharge=int(solde_recharge)
                client["solde"] += solde_recharge
                compteur = 1
        if compteur == 0:
            print("aucun compte trouver a ce numero!!! ")

    if choix == 5 :
        # 5-Transférer de l’argent
        sorti=False
        # verification des numeros
        while sorti == False :
            numero_expediteur=input("saisissez le numero de l'expediteur : ")
            while not(numero_expediteur.isdigit()) or int(numero_expediteur)<770000000 or int(numero_expediteur)>=790000000:
                numero_expediteur=input("resaisissez le numero de l'expediteur : ")

            # recherche du compte
            compteur=0
            for client in tcompte :
                if numero_expediteur == client["numero"]:
                    compteur += 1
                    sorti=True
            if compteur == 0:
                print(f"--- le numero : {numero_expediteur} ne possede pas de compte ---")
                sorti=False

        asake=False
        while asake == False :
            numero_receveur=input("saisissez le numero du receveur : ")
            while not(numero_receveur.isdigit()) or int(numero_receveur)<770000000 or int(numero_receveur)>=790000000:
                numero_receveur=input("resaisissez le numero du receveur : ")

            # recherche du compte
            compteur = 0
            for client in tcompte :
                if numero_receveur == client["numero"]:
                    compteur += 1
                    asake=True
            if compteur == 0:
                print(f"--- le numero : {numero_receveur} ne possede pas de compte ---")
                asake=False
        
        # transfert d'argent de l'expediteur vers le receveur
        montant_transfert=input("saisissez le montant du transfert : ")
        while not montant_transfert.isdigit() or int(montant_transfert)<=0:
            montant_transfert=input("montant invalide resaisissez le montant : ")
        montant_transfert=int(montant_transfert)
        
        # test du solde de l'expediteur ...
        tompant=0
        for client in tcompte :
            if numero_expediteur == client["numero"]:
                if montant_transfert <= client["solde"]:
                    tompant=montant_transfert
                    client["solde"]=client["solde"] - montant_transfert
                    client["transfert"].append({
                        "type":"envoi",
                        "montant": montant_transfert,
                        "vers":numero_receveur
                    })
                    for client in tcompte:
                        if numero_receveur== client["numero"]:
                            client["solde"] += montant_transfert
                            client["transfert"].append( {
                                "type":"reception",
                                "montant": montant_transfert,
                                "de":numero_expediteur
                            })
                            print("transfert effectuer !!!")
                else:
                    print("solde insufisant")

    if choix == 6 :
        # 6-Afficher l’historique des transferts
        for client in tcompte :
            historique+=client["transfert"]
        print(f"voici l´historique des trasnferts : {historique}")

    if choix == 7 :
        # 7-quitter le service orange money
        print("---merci d'avoir utiliser orange money et a bientot sur notre plate-forme !!!---")
        out = False
