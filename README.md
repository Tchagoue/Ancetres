
# Ancetres
workshop
# En considérant l'hypothèse que les mariages ne se faisaient pas entre personnes parentes :
  - Cet algorithme permet de calculer le nombre théorique d'ancêtres que vous avez eu à une génération donnée.
  - Il permet également d'obtenir le nombre total d'ancêtres de votre arbre tronqué à une génération donnée.
# l'algorithme prend les variables suivantes :
  - date_origine : votre date de naissance
  - age_gap : écart moyen entre les parents et leurs enfants dans votre arbre généalogique
  - date_generation : la date de naissance de la génération de votre arbre généalogique que vous souhaitez investiguer
  - n : le numéro de la génération que vous souhaitez investiguer, renseignez n à défaut de la date_generation, et inversement
  - renseignez |choix = 'date'| pour considérer date_generation et, |choix = 'position'| pour considérer n
# Analyse
  Cette suite géométrique croît extrêmement vite, et met en évidence que dans une communauté (pays, village, clan...)
  pseudo fermée (avec une population étrangère de moins de 0.3%/an ), il serait a priori difficile de croire que les mariages entre cousins plus ou moins éloignés
  n'aient pas eu lieu dans le passé.
# Task
  Pour vérifier cette Analyse, pouvez-vous calculer la probabilité que deux personnes n'étant pas de la même famille nucléaire, prises aléatoirement en 2024
  dans une population pseudo-fermée de taille **P**, avec un apport d'étranger de **e**% de la population total par an, aient eu **q** ancêtres communs **x** siècles plutot.
  - Sachant que la population **P** croit de **c**%/an avec un écart d'age moyen entre génération de **eg**
  - On defini un étranger comme étant, tout individu n'ayant aucune ascendance dans la population P

# Appliquer avec les valeurs des Bamilekes du Cameroun et conclure:
  - apport d'étranger de 0.02%/an | **e** = 0.022
  - croissance de la population de 2,6%/an | **c**=2,6
  - population **P** = 2,77 millions
  - Sur 5, puis 10 siècles| **x** =10
  - 1,5,10 ancetres communs | **q** = 1
  - écart d'age moyen entre génération de 30 ans | **eg** = 30
# Illustration
  - illustration modèle théorique pour un jeune camerounais né en 2000 avec écart d'age moyen parent-enfant : 30 ans.
  - Lien Google Colab  https://colab.research.google.com/drive/1VHuOksjXrub1nWqJBNxOgB_pNNnH6hzV?usp=sharing
![image](https://github.com/user-attachments/assets/8da6beba-ff11-4431-bf6a-578e940563c9)



