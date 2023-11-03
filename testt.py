# Imports
from fltk import *

# Variables globales
taille_fenetre = 600

#Definitions de fonctions
def dessiner_plateau():
    taille_case = taille_fenetre / 7
    for i in range(7):
        y = i * taille_case
        for j in range(7):
            x = j * taille_case
            rectangle(x, y, x + taille_case, y + taille_case, couleur='black')
            
def clic_vers_case(x, y, taille_case):
    return int(y // taille_case), int(x // taille_case)


def affiche_pion(zone9pion):
    i, j = clic_vers_case(x, y, taille_case)
    if (i,j) in zone9pion:
        cercle(x, y,25,remplissage='red')
        print("cercle posé:")
        

def carre():
    rectangle(taille_fenetre//15 , taille_fenetre//15 , taille_fenetre - taille_fenetre//15 , taille_fenetre - taille_fenetre//15 , epaisseur = 3)
    rectangle(taille_fenetre//5 , taille_fenetre//5 , taille_fenetre - taille_fenetre//5 , taille_fenetre - taille_fenetre//5,epaisseur = 3)
    rectangle(taille_fenetre//3 , taille_fenetre//3 , taille_fenetre - taille_fenetre//3 , taille_fenetre - taille_fenetre//3,epaisseur = 3)


def trait():
    ligne(taille_fenetre//2 , taille_fenetre//15 , taille_fenetre//2 , taille_fenetre//3 , couleur='black' , epaisseur = 3)
    ligne(taille_fenetre//15 , taille_fenetre//2 , taille_fenetre//3 , taille_fenetre//2 , couleur='black' , epaisseur = 3)
    ligne(taille_fenetre - taille_fenetre//15 , taille_fenetre//2 , taille_fenetre - taille_fenetre//3 , taille_fenetre//2 , couleur='black' , epaisseur = 3)
    ligne(taille_fenetre//2 , taille_fenetre - taille_fenetre//15 , taille_fenetre - taille_fenetre//2 , taille_fenetre - taille_fenetre//3 , couleur='black' , epaisseur = 3)

def zone_pion():
    cercle(taille_fenetre//15 , taille_fenetre//15,4,remplissage='black')
    cercle(taille_fenetre - taille_fenetre//15 , taille_fenetre - taille_fenetre//15,3,remplissage='black')
    cercle(taille_fenetre//5 , taille_fenetre//5,4,remplissage='black')
    cercle(taille_fenetre - taille_fenetre//5 , taille_fenetre - taille_fenetre//5,4,remplissage='black')
    cercle(taille_fenetre//3 , taille_fenetre//3,4,remplissage='black')
    cercle(taille_fenetre - taille_fenetre//3 , taille_fenetre - taille_fenetre//3,4,remplissage='black')
    cercle(taille_fenetre//2 , taille_fenetre//15,4,remplissage='black')
    cercle(taille_fenetre//2 , taille_fenetre//3,4,remplissage='black')
    cercle(taille_fenetre//15 , taille_fenetre//2,4,remplissage='black')
    cercle(taille_fenetre//3 , taille_fenetre//2,4,remplissage='black')
    cercle(taille_fenetre - taille_fenetre//15 , taille_fenetre//2,4,remplissage='black')
    cercle(taille_fenetre - taille_fenetre//3 , taille_fenetre//2,4,remplissage='black')
    cercle(taille_fenetre//2 , taille_fenetre - taille_fenetre//15,4,remplissage='black')
    cercle(taille_fenetre - taille_fenetre//2 , taille_fenetre - taille_fenetre//3,4,remplissage='black')
    cercle(taille_fenetre - taille_fenetre//3 , taille_fenetre//3,4,remplissage='black')
    cercle(taille_fenetre//3 , taille_fenetre - taille_fenetre//3,4,remplissage='black')
    cercle(taille_fenetre - taille_fenetre//5 , taille_fenetre//5,4,remplissage='black')
    cercle(taille_fenetre - taille_fenetre//5 , taille_fenetre//2,4,remplissage='black')
    cercle(taille_fenetre//2 , taille_fenetre - taille_fenetre//5,4,remplissage='black')
    cercle(taille_fenetre//5 ,taille_fenetre - taille_fenetre//5,4,remplissage='black')
    cercle(taille_fenetre//15 , taille_fenetre - taille_fenetre//15,4,remplissage='black')
    cercle(taille_fenetre//5 , taille_fenetre//2,4,remplissage='black')
    cercle(taille_fenetre//2 , taille_fenetre//5,4,remplissage='black')
    cercle(taille_fenetre - taille_fenetre//15 , taille_fenetre//15,4,remplissage='black')

# Programme principal
if __name__ == '__main__':
    
    #Initialisation
    cree_fenetre(taille_fenetre,taille_fenetre)
    taille_plateau = 7
    taille_case = taille_fenetre / taille_plateau
    zone9pion = [(0,0),(3,0),(6,0),(1,1)
                 ,(3,1),(5,1),(2,2),(3,2)
                 ,(4,2),(0,3),(1,3),(2,3)
                 ,(4,3),(5,3),(6,3),(2,4)
                 ,(3,4),(4,4),(1,5),(3,5)
                 ,(5,5),(0,6),(3,6),(6,6)]
    
    # Boucle principale du jeu
    while True:
        #efface_tout()
        dessiner_plateau()
        carre()
        trait()
        zone_pion()
        mise_a_jour()
        
        # Détection de victoire
        #if gagne(taille_plateau):
            #texte(taille_fenetre/2, taille_fenetre/2, 'Gagné !',
                       #ancrage='c', taille='40')
            #attend_fermeture()
            #break

        
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'Quitte':
            ferme_fenetre()
            break
        elif ty == 'ClicGauche':
            x, y = abscisse(ev), ordonnee(ev)
            
#             print('Clic gauche :', abscisse(ev), ordonnee(ev))
            
            i, j = clic_vers_case(x, y, taille_case)
            print(i, j)
            affiche_pion(zone9pion)
            mise_a_jour()
            #inverse(plateau, i, j)