import re


def demander_infos():
    mois, anne, test = "", "", False
    message = "Entrer au clavier un mois et une année au format MM AAAA (par exemple 03 2008): \n"
    while test == False:  # va tester si le code  a reussie de faire se qu'il doit faire dans le try temps qu'il a pas resusie test restera = false

        try:  # fonction qui dis que tu vas esseyé d'executer le code
            mois, m, anne = re.findall("([0-1][0-9])([ ])([0-9][0-9][0-9][0-9])", input(message))[0]

            test = True

        except:  # quand il a une erreur dans ton conde dans la partie qui dans le try
            print("ERREUR: Vous devez entrer les données demandées dans le format MM AAAA.")
        finally:  # fonction qui dis de tout les fasont tu va excuter la ligne en dessous
            pass
    return int(mois), int(anne)
