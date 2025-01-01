PC = "pouces vers cm"
CP = "cm vers pouces"
def demander_utilisateur():
    reponse_int = 0  
    while reponse_int==0 :
        print() 
        reponse_str= input("Quelle conversion souhaite vous faire : \n1-pouces vers cm\n2-cm vers pouces \nVotre choix (1 ou 2 ) :")
        try : 
            reponse_int = int(reponse_str)
            if reponse_int== 1 or reponse_int ==2 :
                return reponse_int
            else:
                reponse_int=0  
        except:      
            print("ERREUR : Veuiller choisir entre 1 ou 2 ")
            reponse_int = 0
    return reponse_int

def conversion_pouces_cm():
    print(f"Vous voule convertir {PC} ")
    reponse_int = 0 
    while reponse_int == 0 :  
        reponse_str= input("Renter la valeur a convertir :")
        try : 
            reponse_int= int(reponse_str)
            #conversion 
            resultats = reponse_int * 2.54
            return resultats
        
        except : 
            print("Erreur veuille rentre un nombre ")
            reponse_int= 0 
        return resultats 

def conversion_cm_pouces():
    print(f"Vous voule convertir {CP} ")
    reponse_int = 0 
    while reponse_int == 0 :  
        reponse_str= input("Renter la valeur a convertir :")
        try : 
            reponse_int= int(reponse_str)
            #conversion 
            resultats = reponse_int * 0.394
            return resultats
        
        except : 
            print("Erreur veuille rentre un nombre ")
            reponse_int= 0 
        return resultats 



choix = demander_utilisateur()
if choix == 1 :
    resultas = conversion_pouces_cm()    
    print(f"La resultats du conversion de {PC} est : {resultas} cm  ")
elif choix == 2  :
    resultas = conversion_cm_pouces()
    print(f"La resultats du conversion de {PC} est : {resultas} pouces  ")
else :
    print("Errorrrrr")
