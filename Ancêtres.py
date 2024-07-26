# ------------------------------------------------Ancêtres-------------------------------------------------------------------
# En considérant l'hypothèse que les mariages ne se faisaient pas entre personnes parentes :
# Cet algorithme permet de calculer le nombre théorique d'ancêtres que vous avez eu à une génération donnée.
# Il permet également d'obtenir le nombre total d'ancêtres de votre arbre tronqué à une génération donnée.
# Il prend les variables suivantes :
# date_origine : votre date de naissance
# age_gap : écart moyen entre les parents et leurs enfants dans votre arbre généalogique
# date_generation : la date de naissance de la génération de votre arbre généalogique que vous souhaitez investiguer
# n : le numéro de la génération que vous souhaitez investiguer, renseignez n à défaut de la date_generation, et inversement
# renseignez |choix = 'date'| pour considérer date_generation et, |choix = 'position'| pour considérer n
#----------------------------------------------------------------------------------------------------------------------------

def Nombre_Ancêtres(date_origine,age_gap,date_generation,n,choix):

    if choix=='date':
        n= int(abs((date_origine-date_generation)/age_gap)+1)
    else:
        n=int(n)
    Nbr_A_génération_n = int(2**n)
    Nbr_A_arbre_généalogique_tronqué_n = int((2**(n+1))-2)

    return Nbr_A_génération_n, Nbr_A_arbre_généalogique_tronqué_n, n

#--------------------------------------------------------Paramètres-----------------------------------------------------------
date_origine = 1995
age_gap = 30
date_generation = 1771
n = 17
choix = 'date' # remplacer par 'position' pour considérer la valeur n
#----------------------------------------------------------------------------------------------------------------------------`
Nbr_A, Nbr_A_arbre,n  = Nombre_Ancêtres(date_origine,age_gap,date_generation,n,choix)

print("Il y a de cela près de {} ans (années {}),\n "
      "vos {} ièmes ancêtres étaient au nombre de {},\n"
      " et la totalité théorique d'individus ayant vécu à partir de ce moment\n "
      "pour que vous existiez est de {}".format(n*age_gap,date_origine-n*age_gap,n,Nbr_A,Nbr_A_arbre))

# Cette suite géométrique croît extrêmement vite, et met en évidence que dans une communauté
# (village, clan) pseudo fermée (avec une population étrangère <10%), il est presque impossible que les mariages entre cousins plus ou moins éloignés
# n'aient pas eu lieu dans le passé.
# Pour vérifier cette nouvelle considération, pouvez-vous calculer la probabilité que deux personnes prises aléatoirement
# dans le clan aient un ancêtre commun ?
#----------------------------------------------------------------------------------------------------------------------------
