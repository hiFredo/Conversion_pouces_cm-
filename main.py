PC = "pouces vers cm"
CP = "cm vers pouces"

POUCE_EN_CM = 2.54
CM_EN_POUCE = 0.394
def demander_utilisateur():  
    while True :
        print() 
        reponse_str= input("Quelle conversion souhaite vous faire : \n1-pouces vers cm\n2-cm vers pouces \nVotre choix (1 ou 2 ) :")
        try : 
            reponse_int = int(reponse_str)
            if reponse_int== 1 or reponse_int ==2 :
                return reponse_int
            else:
                print( "Veuiller entre 1 ou 2")
        except:      
            print("ERREUR : Veuiller renter un nombre valide( 1 ou 2 )")

def demander_valeur(conversion_type):
    print(f"Vous voulez convertir {conversion_type}")
    while True:
        valeur_str = input("Entrez la valeur à convertir : ")
        try:
            valeur_float = float(valeur_str)
            return valeur_float
        except ValueError:
            print("ERREUR : Veuillez entrer un nombre valide.")


def conversion_pouces_cm(valeur):
    return valeur * POUCE_EN_CM
  
def conversion_cm_pouces(valeur):
    return valeur * CM_EN_POUCE
   
     


choix = demander_utilisateur()
if choix == 1 :
    valeur= demander_valeur(PC)
    resultas = conversion_pouces_cm(valeur)    
    print(f"La resultats du conversion de {valeur} pouces = {resultas} cm  ")
elif choix == 2  :
    valeur= demander_valeur(CP)
    resultas = conversion_cm_pouces(valeur)
    print(f"La resultats du conversion de {valeur} cm =  {resultas} pouces  ")
