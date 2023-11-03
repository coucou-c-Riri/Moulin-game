from fltk import *
from playsound import *
import time 

def main_menu(wallpaper, joueur1):
    """Cette fonction permet d afficher le menu principal avec 3 boutons qui dirigent chacun vers une fonction:
    le "PLAY GAME" qui permet de rentrer dans le jeu, les "SETTINGS" qui permet d acceder au paramere et le "EXIT GAME"
    qui ferme le jeu tout simplement """
        
    start = 'Blanc'
    rectangle(0, 0, taille, taille,couleur='black', remplissage='#410000', epaisseur=epaisseur, tag='')
    image(taille//2, taille//2, f"Ognjen_Riyane_Enzo-main.png", ancrage='center', tag='')
    rectangle(taille//5, taille//1.45, taille - taille//5,  taille - taille//8.5,couleur='black', remplissage='dark green', epaisseur=epaisseur, tag='') #3er
    rectangle(taille//5, taille//5, taille - taille//5, taille - taille//1.65,couleur='black', remplissage='dark blue', epaisseur=epaisseur, tag='') #1eme
    rectangle(taille//5, taille//2.25, taille - taille//5, taille - taille//2.85,couleur='black', remplissage='dark blue', epaisseur=epaisseur, tag='') #2eme
    texte(taille//2.5, taille//3.5, "PLAY GAME",couleur='red', ancrage='nw', police='Helvetica', taille=24, tag='')
    texte(taille//2.5, taille//1.9, "SETTINGS",couleur='red', ancrage='nw', police='Helvetica', taille=24, tag='')
    texte(taille//2.5, taille//1.3, "EXIT GAME",couleur='red', ancrage='nw', police='Helvetica', taille=24, tag='')
    texte(taille//2.9, taille//10, "JEU DU MOULIN !",couleur='red', ancrage='nw', police='Helvetica', taille=24, tag='')
    while True:
        x, y = attend_clic_gauche()
        if taille//5 <= x <= taille - taille//5 and taille//5 <= y <= taille - taille//1.65 :
            print(f"The {couleurs[joueur1]} player starts the game by placing a pawn!")
            print(x, y)
            return True, False
            
        if taille//5 <= x <= taille - taille//5 and taille//2.25 <= y <= taille - taille//2.85 :
            return True, True
        
        if taille//5 <= x <= taille - taille//5 and taille//1.45 <= y <= taille - taille//8.5 :
            ferme_fenetre()
            return False, False
        
    



def options(t, n, joueur1, joueur2, epaisseur, wallpaper, couleurs, fde):
    """Cette fonction permet d afficher les parametres du jeu afin de modifier les variable pour jouer avec un esthetique
    a votre gout ! il est possible de modifier la taille allant de 500 a 1000, le nombre de pion et leur couleur avec,
    l epaisseur des traits ainsi que le fond d ecran !"""

    rectangle(0, 0, taille, taille, remplissage ='black')
    image(taille//2, taille//2, f"Ognjen_Riyane_Enzo-settings.png", ancrage='center', tag='')
    
    rectangle(taille//3.5, taille//20, taille//2.65, taille//8, couleur="cyan")
    rectangle(taille//1.6, taille//20, taille//1.4, taille//8, couleur="cyan")
    
    texte(taille//2, taille//20, "Taille",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    texte(taille//2, taille//10, f"{t}",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    
    texte(taille//1.5, taille//10.5, "+",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
    texte(taille//3, taille//10.5, "-",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
        
    texte(taille//2, taille//6, "Nombre pions",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    texte(taille//2, taille//4, f"{nbpion[n]}",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    
    rectangle(taille//3.5, taille//5, taille//2.65, taille//3.5, couleur="cyan")
    rectangle(taille//1.6, taille//5, taille//1.4, taille//3.5, couleur="cyan")
    
    texte(taille//1.5, taille//4, "+",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
    texte(taille//3, taille//4, "-",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
    
    texte(taille//4, taille//2.5, f"{couleurs[joueur1]}",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    
    texte(taille//2.7, taille//2.5, "+",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
    texte(taille//7, taille//2.5, "-",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
    
    rectangle(taille//10, taille//2.8, taille//5.5, taille//2.3, couleur="cyan")
    rectangle(taille//3.1, taille//2.8, taille//2.4, taille//2.3, couleur="cyan")
    
    texte(taille//1.35, taille//2.5, f"{couleurs[joueur2]}",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    
    texte(taille//1.15, taille//2.5, "+",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
    texte(taille//1.6, taille//2.5, "-",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
    
    rectangle(taille//1.73, taille//2.8, taille//1.5, taille//2.3, couleur="cyan")
    rectangle(taille//1.21, taille//2.8, taille//1.1, taille//2.3, couleur="cyan")
        
    texte(taille//2, taille//3, "Joueur1      couleur pion      Joueur2",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    
    texte(taille//2, taille//2, "epaisseur",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    texte(taille//2, taille//1.71, f"{epaisseur}",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    
    rectangle(taille//3.5, taille//1.85, taille//2.65, taille//1.6, couleur="cyan")
    rectangle(taille//1.6, taille//1.85, taille//1.4, taille//1.6, couleur="cyan")
    
    texte(taille//1.5, taille//1.71, "+",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
    texte(taille//3, taille//1.71, "-",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
    
    texte(taille//2, taille//1.5, "fond d'ecran",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    texte(taille//2, taille//1.325, f"{fde[wallpaper]}",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    
    rectangle(taille//3.5, taille//1.4, taille//2.65, taille//1.25, couleur="cyan")
    rectangle(taille//1.6, taille//1.4, taille//1.4, taille//1.25, couleur="cyan")
    
    texte(taille//1.5, taille//1.325, "+",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
    texte(taille//3, taille//1.325, "-",couleur='red', ancrage='center', police='Helvetica', taille=50, tag='')
    
    texte(taille//2, taille//1.15, "BACK MENU",couleur='red', ancrage='center', police='Helvetica', taille=24, tag='')
    
    rectangle(taille//3, taille//1.225, taille//1.5, taille//1.1, couleur="cyan")


def modif_taille(t, signe):
    """Cette fonction permet de modifier la taille de la fenetre depuis la fenetre options()"""
    if signe == -1 and t > 500:
        t -= 50 
    elif signe == 1 and t < 1000:
        t += 50
    return t


def modif_pions(nb, signe):
    """Cette fonction permet de modifier le nombre de pion dans la partie depuis la fenetre options()"""
    if signe == -1 and nb > 0:
        nb -= 1
    elif signe == 1 and nb < 6:
        nb += 1
    return nb


def modif_epaisseur(e, signe):
    """Cette fonction permet de modifier l'epaisseur des traits des lignes et rectangles depuis la fenetre options()"""
    if signe == -1 and e > 1:
        e -= 1
    elif signe == 1 and e < 20:
        e += 1
    return e

        
def modif_joueur(joueur1, signe):
    """Cette fonction permet de modifier la couleur des pions du joueur1 depuis la fenetre options() """
    if signe == -1 and joueur1 > 0:
        joueur1 -= 1
    elif signe == 1 and joueur1 < 6:
        joueur1 += 1
    return joueur1


def modif_joueur(joueur2, signe):
    """Cette fonction permet de modifier la couleur des pions du joueur2 depuis la fenetre options() """
    if signe == -1 and joueur2 > 0:
        joueur2 -= 1
    elif signe == 1 and joueur2 < 6:
        joueur2 += 1
    return joueur2


def modif_fde(f, signe):
    """Cette fonction permet de modifier le fond d'ecran de la fenetre depuis la fenetre options() """
    if signe == -1 and f > 0:
        f -= 1
    elif signe == 1 and f < 8:
        f += 1
    return f


def modif(nbpion, joueur1, joueur2, epaisseur, wallpaper, n, taille):
    """Cette fonction permet de faire les modication, notemment :
    nombre de pions et sa couleur, epaisseur et fond  """

    t = taille 

    while True:
        
        x, y = attend_clic_gauche()
        if taille//3.5 <= x <= taille//2.65  and taille//5 <= y <= taille//3.5 : #- DU "NOMBRE PION"
            signe = -1
            n = modif_pions(n, signe)

        if taille//1.6 <= x <= taille//1.4  and taille//5 <= y <= taille//3.5 : #- DU "NOMBRE PION"
            signe = 1
            n = modif_pions(n, signe)
            
        if taille//3.5 <= x <= taille//2.65  and taille//20 <= y <= taille//8 : #- DU "TAILLE MAP"
            signe = -1
            t = modif_taille(t, signe)

            
        if taille//1.6 <= x <= taille//1.4  and taille//20 <= y <= taille//8 : #+ DU "TAILLE MAP"
            signe = 1
            t = modif_taille(t, signe)
       
        if taille//10 <= x <= taille//5.5  and taille//2.8 <= y <= taille//2.3 : #+ DU "TAILLE MAP"
            signe = -1
            joueur1 = modif_joueur(joueur1, signe)
            
        if taille//3.1 <= x <= taille//2.4  and taille//2.8 <= y <= taille//2.3 : #+ DU "TAILLE MAP"
            signe = 1
            joueur1 = modif_joueur(joueur1, signe)
                  
        if taille//1.73 <= x <= taille//1.5  and taille//2.8 <= y <= taille//2.3 : #+ DU "TAILLE MAP"
            signe = -1
            joueur2 = modif_joueur(joueur2, signe)
            
        if taille//1.21 <= x <= taille//1.1  and taille//2.8 <= y <= taille//2.3 : #+ DU "TAILLE MAP"
            signe = 1
            joueur2 = modif_joueur(joueur2, signe)
            
        if taille//3.5 <= x <= taille//2.65  and taille//1.85 <= y <= taille//1.6 : #+ DU "TAILLE MAP"
            signe = -1
            epaisseur = modif_epaisseur(epaisseur, signe)
            
        if taille//1.6 <= x <= taille//1.4  and taille//1.85 <= y <= taille//1.6 : #+ DU "TAILLE MAP"
            signe = 1
            epaisseur = modif_epaisseur(epaisseur, signe)
             
        if taille//3.5 <= x <= taille//2.65  and taille//1.4 <= y <= taille//1.25 : #+ DU "TAILLE MAP"
            signe = -1
            wallpaper = modif_fde(wallpaper, signe)
            
        if taille//1.6 <= x <= taille//1.4  and taille//1.4 <= y <= taille//1.25 : #+ DU "TAILLE MAP"
            signe = 1
            wallpaper = modif_fde(wallpaper, signe)
        

        
        if taille//3 <= x <= taille//1.5 and taille//1.225 <= y <= taille//1.1 :
            return t, n, joueur1, joueur2, epaisseur, wallpaper, True
        
        efface_tout()
        options(t, n, joueur1, joueur2, epaisseur, wallpaper, couleurs, fde)




    
def fin_menu(pions_sup_blanc, pions_sup_noir, score1, score2, gagnant):
    """Cette fonction permet d'afficher le menu de fin avec la possibilité de voir le score, les pions détruits par joueur, un bouton 'Play again' ainsi qu'un
    bouon 'Exit Game'"""
    gagnant = str.upper(gagnant) #Permet de mettre le string en majuscule 
    p1 = str.upper(couleurs[joueur1])
    p2 = str.upper(couleurs[joueur2])
    rectangle(0, 0, taille, taille,couleur='black', remplissage='#410000', epaisseur=epaisseur, tag='')
    image(taille//2, taille//2, f"Ognjen_Riyane_Enzo-end.png", ancrage='center', tag='')
    rectangle(taille//20, taille//5, taille - taille//1.5, taille - taille//1.65,couleur='black', remplissage='dark blue', epaisseur=epaisseur, tag='') #1eme
    texte(taille//5.2, taille//4, f"{p1} SCORE", couleur = 'red', ancrage = 'center', police= 'Helvetica', taille=taille//33, tag='')
    texte(taille//5.2, taille//3, f"{score1}", couleur = 'red', ancrage = 'center', police= 'Helvetica', taille=taille//33, tag='')
    
    rectangle(taille//1.55, taille//5, taille//1.05, taille - taille//1.65,couleur='black', remplissage='dark blue', epaisseur=epaisseur, tag='') #1eme

    rectangle(taille//20, taille//2.2, taille - taille//1.5, taille//1.5,couleur='black', remplissage='dark blue', epaisseur=epaisseur, tag='') #1eme
    rectangle(taille//1.55, taille//2.2, taille//1.05, taille//1.5,couleur='black', remplissage='dark blue', epaisseur=epaisseur, tag='') #1eme
    
    texte(taille//1.25, taille//4, f"{p2} SCORE", couleur = 'red', ancrage = 'center', police= 'Helvetica', taille=taille//33, tag='')
    texte(taille//1.25, taille//3, f"{score2}", couleur = 'red', ancrage = 'center', police= 'Helvetica', taille=taille//33, tag='')

    
    texte(taille//2.05, taille//2.4, "PAWNS REMOVED BY :", couleur = 'red', ancrage = 'center', police= 'Helvetica', taille=taille//33, tag='')
            
    rectangle(taille//15, taille//1.45, taille//2.5,  taille - taille//8.5,couleur='black', remplissage='purple', epaisseur=epaisseur, tag='') #3er
    
    texte(taille//5.2, taille//1.8, f"{pions_sup_blanc}", couleur = 'red', ancrage = 'center', police= 'Helvetica', taille=taille//33, tag='')
    
    texte(taille//1.25, taille//1.8, f"{pions_sup_noir}", couleur = 'red', ancrage = 'center', police= 'Helvetica', taille=taille//33, tag='')
    
    rectangle(taille//1.8, taille//1.45, taille//1.1,  taille - taille//8.5,couleur='black', remplissage='purple', epaisseur=epaisseur, tag='') #3er

    texte(taille//2, taille//10, f"{gagnant} WON THE GAME!",couleur='red', ancrage='center', police='Helvetica', taille=taille//33, tag='')
    texte(taille//1.6, taille//1.3, "EXIT GAME",couleur='red', ancrage='nw', police='Helvetica', taille=taille//33, tag='')
    texte(taille//8, taille//1.3, "PLAY AGAIN",couleur='red', ancrage='nw', police='Helvetica', taille=taille//33, tag='')

    while True:
        x, y = attend_clic_gauche()
        taille//1.8, taille//1.45, taille//1.1,  taille - taille//8.5,
        if taille//1.8 <= x <= taille//1.1 and taille//1.45 <= y <= taille - taille//8.5 :
            ferme_fenetre()
            return False
        
        if taille//15 <= x <= taille//2.5 and taille//1.45 <= y <= taille - taille//8.5 :
            return True


def zone9_10pions(taille):
    """Cette fonction permet d afficher le plateau pour 9 et 10 pions"""
    image(taille//2, taille//2, f"{wallpaper}.png", ancrage='center', tag='') #carre de fond 
    rectangle (taille//10.2,taille//10.2,taille  - (taille//10.2),taille - (taille//10.2),couleur='black', epaisseur = epaisseur) #premier carre 
    rectangle (taille//4.3, taille//4.3,taille  - (taille//4.3),taille - (taille//4.3),couleur='black', epaisseur = epaisseur) # deuxieme carre
    rectangle (taille//2.72,taille//2.72,taille  - (taille//2.72),taille - (taille//2.72),couleur='black', epaisseur = epaisseur)
    ligne (taille//10.2,taille//2,taille//2.72,taille//2,couleur='black', epaisseur = epaisseur)
    ligne( taille//2,taille//10.2,taille//2,taille//2.72,couleur='black', epaisseur = epaisseur )
    ligne( taille - taille//10.2,taille - taille//2,taille - taille//2.72,taille - taille//2,couleur='black', epaisseur = epaisseur )
    ligne( taille - taille//2,taille - taille//10.2,taille - taille//2,taille - taille//2.72,couleur='black', epaisseur = epaisseur)
    
    


def zone12pions(taille):
    """Cette fonction permet d afficher le plateau pour 12 pions"""
    image(taille//2, taille//2, f"{wallpaper}.png", ancrage='center', tag='') #carre de fond 
    rectangle (taille//10.2,taille//10.2,taille  - (taille//10.2),taille - (taille//10.2),couleur='black', epaisseur = epaisseur) #premier carre 
    rectangle (taille//4.3, taille//4.3,taille  - (taille//4.3),taille - (taille//4.3),couleur='black', epaisseur = epaisseur) # deuxieme carre
    rectangle (taille//2.72,taille//2.72,taille  - (taille//2.72),taille - (taille//2.72),couleur='black', epaisseur = epaisseur)
    
    ligne (taille//10.2,taille//2,taille//2.72,taille//2,couleur='black', epaisseur = epaisseur)
    ligne( taille//2,taille//10.2,taille//2,taille//2.72,couleur='black', epaisseur = epaisseur )
    ligne( taille - taille//10.2,taille - taille//2,taille - taille//2.72,taille - taille//2,couleur='black', epaisseur = epaisseur )
    ligne( taille - taille//2,taille - taille//10.2,taille - taille//2,taille - taille//2.72,couleur='black', epaisseur = epaisseur)
    
    ligne( taille - taille//10.2,taille - taille//10.2,taille - taille//2.75,taille - taille//2.75,couleur='black', epaisseur = epaisseur)
    ligne( taille - taille//10.2, taille//10.2,taille - taille//2.75, taille//2.75, couleur='black', epaisseur = epaisseur)
    ligne( taille//10.2 , taille//10.2, taille//2.75, taille//2.75, couleur='black', epaisseur=epaisseur)
    
    ligne( taille//10.2, taille - taille//10.2, taille//2.75, taille - taille//2.75, couleur = 'black', epaisseur=epaisseur)

def affiche_9_10_12(taille):
    """Cette fonction permet d afficher les cercles placés sur les intersectons du plateau"""
    x = taille//13
    z = taille//2
    
    for j in range (3):
        if j == 0:
            x = taille//10.2
        elif j == 1:
            x = taille//4.3
        elif j == 2:
            x = taille//2.72
        space = 0
        for i in range (3):
            cercle(x + space,x,10,couleur = 'black',remplissage='red',epaisseur=2)
            cercle(x,x + space,10,couleur = 'black',remplissage='red',epaisseur=2)            
            cercle(taille - x - space,taille - x,10,couleur = 'black',remplissage='red',epaisseur=2)
            cercle(taille - x,taille - x - space,10,couleur = 'black',remplissage='red',epaisseur=2)
            
            space += z - x
            
def zone3pions(taille):
    """Cette fonction permet d afficher le plateau pour 3 pions"""
    image(taille//2, taille//2, f"{wallpaper}.png", ancrage='center', tag='') #carre de fond 
    rectangle (taille//6.2,taille//6.2,taille  - (taille//6.2),taille - (taille//6.2),couleur='black', epaisseur = epaisseur) #premier carre 

    ligne (taille//6.2,taille//2, taille - taille//6.2, taille - taille//2,couleur='black', epaisseur = epaisseur)
    ligne( taille//2,taille//6.2,taille//2,taille - taille//6.2,couleur='black', epaisseur = epaisseur )
    ligne( taille//6.2 , taille//6.2, taille - taille//6.2, taille - taille//6.2, couleur='black', epaisseur=epaisseur)
    ligne( taille - taille//6.2, taille//6.2, taille//6.2, taille - taille//6.2, couleur = 'black', epaisseur=epaisseur)

def affiche_3(taille):
    """Cette fonction permet d afficher les cercles placés sur les intersectons du plateau"""
    x = 0.
    z = taille//2
    y = 0.
    for j in range (3):
        if j == 0:
            
            x = taille//6.2
            
        else:
            y = taille//6.2

        space = 0
        haut = 0
        for i in range (3):
            cercle(x + space,x  ,10,couleur = 'black',remplissage='red',epaisseur=2)
            cercle(x,x + space,10,couleur = 'black',remplissage='red',epaisseur=2)
            cercle(taille - x - space,taille - x,10,couleur = 'black',remplissage='red',epaisseur=2)
            cercle(taille - x,taille - x - space,10,couleur = 'black',remplissage='red',epaisseur=2)
            space += z - x
            haut += z - x
        cercle(taille//2,taille//2,10,couleur = 'black',remplissage='red',epaisseur=2)

def zone5_6pions(taille):
    """Cette fonction permet d afficher le plateau pour 6 pions"""
    image(taille//2, taille//2, f"{wallpaper}.png", ancrage='center', tag='') #carre de fond 
    rectangle (taille//6, taille//6,taille  - (taille//6),taille - (taille//6),couleur='black', epaisseur = epaisseur) # deuxieme carre
    rectangle (taille//2.75,taille//2.75,taille  - (taille//2.75),taille - (taille//2.75),couleur='black', epaisseur = epaisseur)
    ligne (taille//6,taille//2,taille//2.75,taille//2,couleur='black', epaisseur = epaisseur)
    ligne( taille//2,taille//6,taille//2,taille//2.75,couleur='black', epaisseur = epaisseur )
    ligne( taille - taille//6,taille - taille//2,taille - taille//2.75,taille - taille//2,couleur='black', epaisseur = epaisseur )
    ligne( taille - taille//2,taille - taille//6,taille - taille//2,taille - taille//2.75,couleur='black', epaisseur = epaisseur)

def affiche5_6(taille):
    """Cette fonction permet d afficher les cercles placés sur les intersectons du plateau"""
    x = taille//13
    z = taille//2
    
    for j in range (2):
        if j == 0:
            x = taille//6
        elif j == 1:
            x = taille//2.75
        space = 0
        for i in range (3):
            cercle(x + space,x,10,couleur = 'black',remplissage='red',epaisseur=2)
            cercle(x,x + space,10,couleur = 'black',remplissage='red',epaisseur=2)            
            cercle(taille - x - space,taille - x,10,couleur = 'black',remplissage='red',epaisseur=2)
            cercle(taille - x,taille - x - space,10,couleur = 'black',remplissage='red',epaisseur=2)
            
            space += z - x

def zone7pions(taille):
    """Cette fonction permet d afficher le plateau pour 7 pions"""
    image(taille//2, taille//2, f"{wallpaper}.png", ancrage='center', tag='') #carre de fond 
    rectangle (taille//6, taille//6,taille  - (taille//6),taille - (taille//6),couleur='black', epaisseur = epaisseur) # deuxieme carre
    rectangle (taille//2.75,taille//2.75,taille  - (taille//2.75),taille - (taille//2.75),couleur='black', epaisseur = epaisseur)
    ligne (taille//6,taille//2,taille//2.75,taille//2,couleur='black', epaisseur = epaisseur)
    ligne( taille//2,taille//6,taille//2,taille//2.75,couleur='black', epaisseur = epaisseur )
    ligne( taille - taille//6,taille - taille//2,taille - taille//2.75,taille - taille//2,couleur='black', epaisseur = epaisseur )
    ligne( taille - taille//2,taille - taille//6,taille - taille//2,taille - taille//2.75,couleur='black', epaisseur = epaisseur)
        
    ligne(taille//2.75, taille//2.75, taille - taille//2.75, taille - taille//2.75, couleur='black', epaisseur=epaisseur)
    ligne(taille - taille//2.75, taille//2.75, taille//2.75, taille - taille//2.75, couleur='black', epaisseur=epaisseur)
    
def affiche_7(taille):
    """Cette fonction permet d afficher les cercles placés sur les intersectons du plateau"""
    x = taille//13
    z = taille//2
    
    for j in range (2):
        if j == 0:
            x = taille//6
        elif j == 1:
            x = taille//2.75
        space = 0
        for i in range (3):
            cercle(x + space,x,10,couleur = 'black',remplissage='red',epaisseur=2)
            cercle(x,x + space,10,couleur = 'black',remplissage='red',epaisseur=2)            
            cercle(taille - x - space,taille - x,10,couleur = 'black',remplissage='red',epaisseur=2)
            cercle(taille - x,taille - x - space,10,couleur = 'black',remplissage='red',epaisseur=2)
            
            space += z - x
            
def dessiner_plateau(taille):
    """Cette fonction permet de faire un grillage afin de nous aider a faire les coordonnées et à faire ce jeu spectaculaire"""
    cote = taille/15
    for i in range (taille):
        for j in range (taille):
            rectangle(cote*i,cote*j,(i+1)*cote,(j+1)*cote,remplissage="")
            
def choix_map(n):
    """Cette fonction permet de choisir la map en fonction du nombre de pion"""
    if n == 3 :
        zone3pions(taille)
        affiche_3(taille)
    elif n == 5 :
        zone5_6pions(taille)
        affiche5_6(taille)
    elif n == 6 :
        zone5_6pions(taille)
        affiche5_6(taille)
    elif n == 7 :
        zone7pions(taille)
        affiche_7(taille)
    elif n == 9 :
        zone9_10pions(taille)
        affiche_9_10_12(taille)
    elif n == 10 :
        zone9_10pions(taille)
        affiche_9_10_12(taille)
    else :
        zone12pions(taille)
        affiche_9_10_12(taille)


def pixel_vers_case(x, y, taille, case):
    """Cette fonction permet de convertir les pixel en case """
    ligne = x//case
    colonne = y//case
    return (int(ligne), (int(colonne)))
 
def case_vers_pixel(x, y):
    """Cette fonction permet de convertir les cases en pixel"""
    return (x + .5) * case, (y + .5) * case

def affiche_pions(blanc, noir, joueur1, joueur2):
    """Cette fonction permet d'afficher les pions sur le plateau"""
    for j in range(2):
        if j % 2 == 0:
            color = blanc
            coul = couleurs[joueur1]
        else:
            color = noir
            coul = couleurs[joueur2]
        for co in color:
            x, y = co
            x, y = case_vers_pixel(x, y)
            cercle(x, y, 30,couleur = coul, remplissage = coul)
            


def coup_valide_p_1(blanc, noir, joueur1, joueur2, n):
    """Cette fonction permet de faire la phase 1 du jeu (poser les pions sur le plateau)"""
    i = 0
    etat_moulin_blanc = []
    etat_moulin_noir = []
    while i < nb_pions:
        x, y = case_valide()
        if (x, y) not in noir and (x, y) not in blanc:
            if i % 2 == 0:
                joueur = blanc
                p = couleurs[joueur2]
            else :
                joueur = noir
                p = couleurs[joueur1]
            print(f"it's the {p} player's turn to place a pawn\n")
            playsound('Ognjen_Riyane_Enzo-deplacement.mp3')
            joueur.append((x, y))
            affiche_pions(blanc, noir, joueur1, joueur2)
            i += 1
            etat_moulin_blanc, etat_moulin_noir, pions_sup_blanc, pions_sup_noir = status_moulin(blanc, noir, joueur, etat_moulin_blanc, etat_moulin_noir, joueur1, joueur2)
            if pions_sup_blanc == 1 and n == 3 or pions_sup_noir == 1 and n == 3:
                return etat_moulin_blanc, etat_moulin_noir, pions_sup_blanc, pions_sup_noir
            
    return etat_moulin_blanc, etat_moulin_noir, pions_sup_blanc, pions_sup_noir

def selectionner(joueur):
    """Cette fonction permet de selectionner le pion """
    while True:
        x, y = case_valide()
        if (x, y) in joueur:
            x1, y1 = case_vers_pixel(x, y)
            efface_tout()
            affichemap(taille,n, joueur1, joueur2)
            cercle(x1, y1, 30, couleur = 'yellow', epaisseur = 5)
            return (x, y)

def selectionnersupp(joueur):
    """Cette fonction permet de selectionner le pion a supprimer"""
    while True:
        x, y = case_valide()
        if (x, y) in joueur:
            x1, y1 = case_vers_pixel(x, y)
            efface_tout()
            affichemap(taille,n, joueur1, joueur2)
            return (x, y)

def case_valide():
    """Cette fonction permet de verifier si la case est valide (si nous sommes sur une intersection et si un pion n'est pas déjà posé) """
    while True:
        x, y = attend_clic_gauche()
        x1, y1 = pixel_vers_case(x, y, taille, case)
        if (x1, y1) in lstvalide:
            return x1, y1    
        
def supprimer(joueur, etat_blanc, etat_noir, joueur1, joueur2):
    """Cette fonction permet de supprimer les pions adverse après la formation d'un moulin"""
    playsound('Ognjen_Riyane_Enzo-moulined.mp3') # Permet de jouer un son
    if joueur == blanc:
        j = couleurs[joueur1]
    else :
        j = couleurs[joueur2]
    print(f'remove a {j} pawn')
    while True:
        x, y = selectionnersupp(joueur) #On sélectionne le joueur que l'on souhaite supprimer
        if tout_pions_dans_moulin(etat_blanc, etat_noir, joueur) == True: # Condition vérifiant si tous les pions adverse sont dans un moulin
            joueur.remove((x, y))
            actualiser()
            playsound('Ognjen_Riyane_Enzo-capture.mp3') # Permet de jouer un son
            return
        else:
            if pion_dans_moulin(x, y,etat_blanc, etat_noir, joueur) == True: # Condition vérifiant si le pion selectionné est dans un moulin
                joueur.remove((x, y))
                actualiser()
                playsound('Ognjen_Riyane_Enzo-capture.mp3')  # Permet de jouer un son
                return 
    
def pion_dans_moulin(x, y, etat_blanc, etat_noir, joueur):
    """Cette fonction permet de détecter s'il le pion que nous voulons retirer est dans un moulin"""
    if joueur == blanc:
        etat_moulin = etat_blanc
    else:
        etat_moulin = etat_noir
    for lst in etat_moulin: # Regarde moulins formées
        if (x, y) in lst: # Vérifie si (x, y) est dans la liste
            return False
    return True

def tout_pions_dans_moulin(etat_blanc, etat_noir, joueur):
    """Cette fonction permet de détecter s'il y a des pions adverse qui ne sont pas dans un moulins, s'ils sont tous dans un moulin alors nous pourons
    en retirer un dans un moulin."""
    cpt = 0
    lst_moulin = []
    if joueur == blanc:
        etat_moulin = etat_blanc
    else:
        etat_moulin = etat_noir
    for moulin in etat_moulin: # Regarde moulins formées
        for co in moulin: # Regarde les coordonnées des moulins formés
            lst_moulin.append(co) # Fait une liste avec ces coordonnées
    for couple in joueur: 
        if couple not in lst_moulin:
            cpt += 1
    if cpt == 0: # Si aucun pion n'est en dehors d'un moulin alors on return True
        return True
    else :
        return False
       

def actualiser():
    """Cette fonction permet de d'actualiser le plateau"""
    efface_tout()
    affichemap(taille, n, joueur1, joueur2)
    

def phase_2(blanc, noir, etat_moulin_blanc, etat_moulin_noir, joueur, joueur1, joueur2):
    """Cette fonction est la phase 2 qui consiste à déplacer les pions sur les cases voisines """
    while True:
        x, y = selectionner(joueur)
        x1, y1 = case_valide()
        for values in deplacements_possibles[(x, y)] :
            if (x1, y1) == values and (x1, y1) not in blanc and (x1, y1) not in noir: # Vérifie si la case est libre
                joueur.remove((x, y))
                animation(x, y, x1, y1, joueur1, joueur2, joueur) # Déclanche l'animation 
                joueur.append((x1, y1))
                actualiser()
                playsound('Ognjen_Riyane_Enzo-deplacement.mp3')
                etat_moulin_blanc, etat_moulin_noir, pions_sup_blanc, pions_sup_noir = status_moulin(blanc, noir, joueur, etat_moulin_blanc, etat_moulin_noir, joueur1, joueur2) # Vérifie l'état des moulins (regarder docstring de la fonction pour comprendre)
                return etat_moulin_blanc, etat_moulin_noir, pions_sup_blanc, pions_sup_noir
    
def phase_3(blanc, noir, etat_moulin_blanc, etat_moulin_noir, joueur, joueur1, joueur2):
    """Cette fonction permet de passer a la phase 3 qui consiste à pouvoir déplacer ses pions n'importe où sur le plateau"""
    while True:
        x, y = selectionner(joueur)
        x1, y1 = case_valide()
        if (x1, y1) not in blanc and (x1, y1) not in noir: # Vérifie si la case est libre
            joueur.remove((x, y))
            animation(x, y, x1, y1, joueur1, joueur2, joueur)
            joueur.append((x1, y1))
            actualiser()
            playsound('Ognjen_Riyane_Enzo-deplacement.mp3')
            etat_moulin_blanc, etat_moulin_noir, pions_sup_blanc, pions_sup_noir = status_moulin(blanc, noir, joueur, etat_moulin_blanc, etat_moulin_noir, joueur1, joueur2)
            return etat_moulin_blanc, etat_moulin_noir, pions_sup_blanc, pions_sup_noir

def animation(x, y, x1, y1, joueur1, joueur2, joueur):
    """Cette fonction permet de faire une animation des cercles lors des deplacements (les voir se déplacer d'une intersection à l'autre)"""
    x, y = case_vers_pixel(x, y)
    x1, y1 = case_vers_pixel(x1, y1)
    a = (y1 - y)
    b = (x1 - x)
    nb_frames = 30 # Nombre d'images pour faire l'animation de déplacement
    fa = a/nb_frames
    fb = b/nb_frames
    if joueur == blanc:
        coul = couleurs[joueur1]
    else :
        coul = couleurs[joueur2]
    id = None
    actualiser()
    for i in range(nb_frames): # Boucle ajoutant les pixels pour déplacer le pion 
        y += fa
        x += fb
        if id is not None:
            efface(id) # Supprime le dernier cercle formé
        id = cercle(x, y, 30,couleur = coul, remplissage = coul)
        mise_a_jour()
            
        
def coup_valide_p_1_2_3(blanc, noir, n):
    """Cette fonction permet de d'avoir un joueur en phase 3 alors que l'autre est encore dans la phase 2"""
    i = 0
    pions_sup_blanc = 0 
    pions_sup_noir = 0 
    etat_moulin_blanc, etat_moulin_noir, pions_sup_b, pions_sup_n = coup_valide_p_1(blanc, noir, joueur1, joueur2, n)
    while True:
        pions_sup_blanc += pions_sup_b # Ajoute le nombre de pions supprimés 
        pions_sup_noir +=  pions_sup_n
        if i % 2 == 0 :
            joueur = blanc
            p = couleurs[joueur1]
        else :
            joueur = noir
            p = couleurs[joueur2]
        print(f"it's {p} player's turn to move his pawn")

        if len(blanc) < 3 :
            return blanc, pions_sup_blanc, pions_sup_noir
        elif len(noir) < 3 :
            return noir, pions_sup_blanc, pions_sup_noir
        elif len(joueur) > 3 :
            etat_moulin_blanc, etat_moulin_noir, pions_sup_b, pions_sup_n = phase_2(blanc, noir, etat_moulin_blanc, etat_moulin_noir, joueur, joueur1, joueur2) # Phase 2
        else:
            etat_moulin_blanc, etat_moulin_noir, pions_sup_b, pions_sup_n = phase_3(blanc, noir, etat_moulin_blanc, etat_moulin_noir, joueur, joueur1, joueur2) # Phase 3
        i += 1



def status_moulin(blanc, noir, joueur, etat_moulin_blanc, etat_moulin_noir, joueur1, joueur2):
    """Cette fonction permet de detecter la formation d un nouveau moulin !"""
    etat_blanc, etat_noir = moulin(blanc, noir, joueur)
    pions_sup_blanc = 0
    pions_sup_noir = 0
    if etat_blanc != [] or etat_noir != []: # S'il n'y a aucun moulin de formé, on ne rentre pas dans la condition 
        if joueur == blanc and etat_moulin_blanc != etat_blanc and len(etat_blanc) >= len(etat_moulin_blanc): # Pour savoir s'il y a un nouveau moulin on regarde la liste des moulin actuelle est différente de la précédente et si dans le cas
                                                                                                            # où dans un même coup un s'est formé et un autre déformé 
            joueur = noir
            supprimer(joueur, etat_blanc, etat_noir, joueur1, joueur2)
            pions_sup_blanc += 1
            
        elif joueur == noir and etat_moulin_noir != etat_noir and len(etat_noir) >= len(etat_moulin_noir):
            joueur = blanc
            supprimer(joueur, etat_blanc, etat_noir, joueur1, joueur2) # Permet de supprimer un pion
            pions_sup_noir += 1
    etat_moulin_blanc = etat_blanc # Actualise les moulins du coup précédent
    etat_moulin_noir = etat_noir
    return etat_moulin_blanc, etat_moulin_noir, pions_sup_blanc, pions_sup_noir


                  
def moulin(blanc, noir, joueur):
    """Cette fonction permet de renvoyer la liste des moulins formés de chaque joueur!"""
    lst_blanc = []
    lst_noir = []
    for i in range(2):
        if i % 2 == 0:
            joueur = blanc
            lst = lst_blanc
        else:
            joueur = noir
            lst = lst_noir
        for values in solu.values():
            cpt = 0
            for co in joueur:
                if co in values:
                    cpt += 1
            if cpt == 3:
                lst.append(values)
    return lst_blanc, lst_noir


def coups_deplacements_possibles(n):
    """Cette fonction permet d'associer les déplacements, les listes de coordonnées valides et les différents moulins possible en fonction du nombre de pions choisi"""
    if n == 3 :
        return deplacement_possible_3, lstvalide_3, 6, solutions3
    elif n == 5 :
        return deplacement_possible5_6, lstvalide_5_6_7, 10, solutions5_6
    elif n == 6 :
        return deplacement_possible5_6, lstvalide_5_6_7, 12, solutions5_6
    elif n == 7 :
        return deplacement_possible_7, lstvalide_5_6_7, 14, solutions7
    elif n == 9 :
        return deplacement_possible_9_10, lstvalide_9_10_12, 18, solutions9_10
    elif n == 10 :
        return deplacement_possible_9_10, lstvalide_9_10_12, 20, solutions9_10
    else :
        return deplacement_possible_12, lstvalide_9_10_12, 24, solutions12
    
def gagnant(blanc, noir, perdant, joueur1, joueur2, score1, score2):
    """Cette fonction permet de renvoyer le joueur gagnant à la fin de la partie"""
    if perdant == blanc:
        gagnant = couleurs[joueur2]
        score2 += 1
    else :
        gagnant = couleurs[joueur1]
        score1 += 1
    return gagnant, score1, score2        
    
def affichemap(taille, n, joueur1, joueur2):
    """Cette fonction permet de d'afficher la map avec les pions dessus"""
    choix_map(n)
    affiche_pions(blanc, noir, joueur1, joueur2)

deplacement_possible_12 = {(1, 1): [(7, 1),(1, 7),(3, 3)]
                        ,(7, 1): [(7, 3),(1, 1),(13, 1)]
                        ,(13, 1): [(7, 1),(11, 3),(13, 7)]
                        ,(3, 3): [(1, 1),(5, 5),(7, 3),(3, 7)]
                        ,(7, 3): [(7, 1),(7, 5),(11, 3),(3, 3)]
                        ,(11, 3): [(9, 5),(7, 3),(11, 7),(13, 1)]
                        ,(5, 5): [(5, 7),(7, 5),(3, 3)]
                        ,(7, 5): [(5, 5),(7, 3),(9, 5)]
                        ,(9, 5): [(7, 5),(9, 7),(11, 3)]
                        ,(1, 7): [(1, 13),(3, 7),(1, 1)]
                        ,(3, 7): [(1, 7),(3, 11),(5, 7),(3, 3)]
                        ,(5, 7): [(5, 9),(3, 7),(5, 5)]
                        ,(9, 7): [(9, 5),(11, 7),(9, 9)]
                        ,(11, 7): [(9, 7),(11, 3),(13, 7),(11, 11)] 
                        ,(13, 7): [(11, 7),(13, 1),(13, 13)]
                        ,(5, 9): [(3, 11),(5, 7),(7, 9)]
                        ,(7, 9): [(5, 9),(9, 9),(7, 11)]
                        ,(9, 9): [(7, 9),(9, 7),(11, 11)]
                        ,(3, 11): [(1, 13),(3, 7),(5, 9),(7, 11)]
                        ,(7, 11): [(3, 11),(7, 9),(11, 11),(7, 13)]
                        ,(11, 11): [(13, 13),(7, 11),(9, 9),(11, 7)]
                        ,(1, 13): [(3, 11),(1, 7),(7, 13)]
                        ,(7, 13): [(1, 13),(7, 11),(13, 13)]
                        ,(13, 13): [(7, 13),(11, 11),(13, 7)]}

deplacement_possible_9_10 = {(1, 1): [(7, 1),(1, 7)]
                        ,(7, 1): [(7, 3),(1, 1),(13, 1)]
                        ,(13, 1): [(7, 1),(13, 7)]
                        ,(3, 3): [(7, 3),(3, 7)]
                        ,(7, 3): [(7, 1),(7, 5),(11, 3),(3, 3)]
                        ,(11, 3): [(7, 3),(11, 7)]
                        ,(5, 5): [(5, 7),(7, 5)]
                        ,(7, 5): [(5, 5),(7, 3),(9, 5)]
                        ,(9, 5): [(7, 5),(9, 7)]
                        ,(1, 7): [(1, 13),(3, 7),(1, 1)]
                        ,(3, 7): [(1, 7),(3, 11),(5, 7),(3, 3)]
                        ,(5, 7): [(5, 9),(3, 7),(5, 5)]
                        ,(9, 7): [(9, 5),(11, 7),(9, 9)]
                        ,(11, 7): [(9, 7),(11, 3),(13, 7),(11, 11)] 
                        ,(13, 7): [(11, 7),(13, 1),(13, 13)]
                        ,(5, 9): [(5, 7),(7, 9)]
                        ,(7, 9): [(5, 9),(9, 9),(7, 11)]
                        ,(9, 9): [(7, 9),(9, 7)]
                        ,(3, 11): [(3, 7),(7, 11)]
                        ,(7, 11): [(3, 11),(7, 9),(11, 11),(7, 13)]
                        ,(11, 11): [(7, 11),(11, 7)]
                        ,(1, 13): [(1, 7),(7, 13)]
                        ,(7, 13): [(1, 13),(7, 11),(13, 13)]
                        ,(13, 13): [(7, 13),(13, 7)]}


lstvalide_9_10_12 = [(1, 1),(7, 1),(13, 1),(3, 3),(7, 3),(11, 3),(5, 5),(7, 5),
              (9, 5),(1, 7),(3, 7),(5, 7),(9, 7),(11, 7),(13, 7),(5, 9),
              (7, 9),(9, 9),(3, 11),(7, 11),(11, 11),(1, 13),(7, 13),(13, 13)]


deplacement_possible_3 = {(2, 2): [(7, 2),(7, 7),(2, 7)]
                        ,(7, 2): [(2, 2),(7, 7),(12, 2)]
                        ,(12, 2): [(7, 2),(7, 7),(12, 7)]
                        ,(2, 7): [(2, 2),(7, 7),(2, 12)]
                        ,(7, 7): [(2, 2),(7, 2),(12, 2),(12, 7),(12, 12),(7, 12),(2, 12),(2, 7)]
                        ,(12, 7): [(12, 2),(7, 7),(12, 12)]
                        ,(2, 12): [(2, 7),(7, 7),(7, 12)]
                        ,(7, 12): [(2, 12),(7, 7),(12, 12)]
                        ,(12, 12): [(7, 12),(7, 7),(12, 7)]}

lstvalide_3 = [(2, 2),(7, 2),(12, 2),(12, 7),(2, 7),(7, 7),(12, 7),(2, 12),(7, 12),(12, 12)]

deplacement_possible5_6 = {(2, 2):[(2, 7),(7, 2)]
                        ,(7, 2):[(2, 2),(7, 5),(12, 2)]
                        ,(12, 2):[(7, 2),(12, 7)]
                        ,(5, 5):[(7, 5),(5, 7)]
                        ,(7, 5):[(5, 5),(7, 2),(9, 5)]
                        ,(9, 5):[(7, 5),(9, 7)]
                        ,(2, 7):[(2, 2),(5, 7),(2, 12)]
                        ,(5, 7):[(5, 5),(5, 9),(2, 7)]
                        ,(9, 7):[(9, 5),(12, 7),(9, 9)]
                        ,(12, 7):[(9, 7),(12, 2),(12, 12)]
                        ,(5, 9):[(5, 7),(7, 9)]
                        ,(7, 9):[(5, 9),(7, 12),(9, 9)]
                        ,(9, 9): [(7, 9),(9, 7)]
                        ,(2, 12): [(2, 7),(7, 12)]
                        ,(7, 12): [(2, 12),(7, 9),(12, 12)]
                        ,(12, 12):[(7, 12),(12, 7)]}

deplacement_possible_7 = {(2, 2):[(2, 7),(7, 2)]
                        ,(7, 2):[(2, 2),(7, 5),(12, 2)]
                        ,(12, 2):[(7, 2),(12, 7)]
                        ,(5, 5):[(7, 5),(5, 7),(9, 9)]
                        ,(7, 5):[(5, 5),(7, 2),(9, 5)]
                        ,(9, 5):[(7, 5),(9, 7),(5, 9)]
                        ,(2, 7):[(2, 2),(5, 7),(2, 12)]
                        ,(5, 7):[(5, 5),(5, 9),(2, 7)]
                        ,(9, 7):[(9, 5),(12, 7),(9, 9)]
                        ,(12, 7):[(9, 7),(12, 2),(12, 12)]
                        ,(5, 9):[(5, 7),(7, 9),(9, 5)]
                        ,(7, 9):[(5, 9),(7, 12),(9, 9)]
                        ,(9, 9):[(7, 9),(9, 7),(5, 5)]
                        ,(2, 12):[(2, 7),(7, 12)]
                        ,(7, 12):[(2, 12),(7, 9),(12, 12)]
                        ,(12, 12):[(7, 12),(12, 7)]}
lstvalide_5_6_7 = [(2, 2),(7, 2),(12, 2),(5, 5),(7, 5),(9, 5),
             (2, 7),(5, 7),(9, 7),(12, 7),(5, 9),
             (7, 9),(9, 9),(2, 12),(7, 12),(12, 12)]

solutions3 = {'s1' :[(2, 2),(7, 2),(12, 2)]
             ,'s2':[(2, 7),(7, 7),(12, 7)]
             ,'s3':[(2, 12),(7, 12),(12, 12)]
             ,'s4':[(2, 2),(2, 7),(2, 12)]
             ,'s5':[(7, 2),(7, 7),(7, 12)]
             ,'s6':[(12, 2),(12, 7),(12, 12)]
             ,'s7':[ (2, 2),(7, 7),(12, 12)]
             ,'s8':[ (12, 2),(7, 7),(2, 12)]}

solutions5_6 = {'s1' :[(2, 2), (7, 2), (12, 2)]
            ,'s2' :[(12, 2), (12, 7), (12, 12)]
            ,'s3' :[(2, 12), (7, 12), (12, 12)]
            ,'s4' :[(2, 2), (2, 7), (2, 12)]
            ,'s5' :[(5, 5), (7, 5), (9, 5)]
            ,'s6' :[(9, 5), (9, 7), (9, 9)]
            ,'s7' :[(5, 9), (7, 9), (9, 9)]
            ,'s8' :[(5, 5), (5, 7), (5, 9)]}


solutions5 = {'s1' :[(2, 2), (7, 2), (12, 2)]
            ,'s2' :[(12, 2), (12, 7), (12, 12)]
            ,'s3' :[(2, 12), (7, 12), (12, 12)]
            ,'s4' :[(2, 2), (2, 7), (2, 12)]
            ,'s5' :[(5, 5), (7, 5), (9, 5)]
            ,'s6' :[(9, 5), (9, 7), (9, 9)]
            ,'s7' :[(5, 9), (7, 9), (9, 9)]
            ,'s8' :[(5, 5), (5, 7), (5, 9)]}

solutions7 = {'s1' :[(2, 2), (7, 2), (12, 2)]
            ,'s2' :[(12, 2), (12, 7), (12, 12)]
            ,'s3' :[(2, 12), (7, 12), (12, 12)]
            ,'s4' :[(2, 2), (2, 7), (2, 12)]
            ,'s5' :[(5, 5), (7, 5), (9, 5)]
            ,'s6' :[(9, 5), (9, 7), (9, 9)]
            ,'s7' :[(5, 9), (7, 9), (9, 9)]
            ,'s8' :[(5, 5), (5, 7), (5, 9)]}

solutions9_10 = {'s1' :[(1, 1), (7, 1), (13, 1)]
            ,'s2' :[(3, 3), (7, 3), (11, 3)]
            ,'s3' :[(5, 5), (7, 5), (9, 5)]
            ,'s4' :[(1, 7), (3, 7), (5, 7)]
            ,'s5' :[(9, 7), (11, 7), (13, 7)]
            ,'s6' :[(5, 9), (7, 9), (9, 9)]
            ,'s7' :[(3, 11), (7, 11), (11, 11)]
            ,'s8' :[(1, 13), (7, 13), (13, 13)]
            ,'s9' :[(1, 1), (1, 7), (1, 13)]
            ,'s10' :[(3, 3), (3, 7), (3, 11)]
            ,'s11' :[(5, 5), (5, 7), (5, 9)]
            ,'s12' :[(7, 1), (7, 3), (7, 5)]
            ,'s13' :[(7, 9), (7, 11), (7, 13)]
            ,'s14' :[(9, 5), (9, 7), (9, 9)]
            ,'s15' :[(11, 3), (11, 7), (11, 11)]
            ,'s16' :[(13, 1), (13, 7), (13, 13)]}

solutions12 = {'s1' :[(1, 1), (7, 1), (13, 1)]
            ,'s2' :[(3, 3), (7, 3), (11, 3)]
            ,'s3' :[(5, 5), (7, 5), (9, 5)]
            ,'s4' :[(1, 7), (3, 7), (5, 7)]
            ,'s5' :[(9, 7), (11, 7), (13, 7)]
            ,'s6' :[(5, 9), (7, 9), (9, 9)]
            ,'s7' :[(3, 11), (7, 11), (11, 11)]
            ,'s8' :[(1, 13), (7, 13), (13, 13)]
            ,'s9' :[(1, 1), (1, 7), (1, 13)]
            ,'s10' :[(3, 3), (3, 7), (3, 11)]
            ,'s11' :[(5, 5), (5, 7), (5, 9)]
            ,'s12' :[(7, 1), (7, 3), (7, 5)]
            ,'s13' :[(7, 9), (7, 11), (7, 13)]
            ,'s14' :[(9, 5), (9, 7), (9, 9)]
            ,'s15' :[(11, 3), (11, 7), (11, 11)]
            ,'s16' :[(13, 1), (13, 7), (13, 13)]
            ,'s17' : [(1, 1), (3, 3), (5, 5)]
            ,'s18' : [(13, 1), (11, 3), (9, 5)]
            ,'s19' : [(1, 13), (3, 11), (5, 9)]
            ,'s20' : [(13, 13), (11, 11), (9, 9)]
               }



if __name__ == '__main__':  
    new_game = True
    score1 = 0
    score2 = 0
    taille = 800
    couleurs = ['white', 'black', 'red', 'yellow', 'blue', 'green', 'purple']
    fde = ["espace","automne","printemps","ete","hiver","bois","metal","paradis","enfer"]
    fichiers_images = ["Ognjen_Riyane_Enzo-espace","Ognjen_Riyane_Enzo-automne","Ognjen_Riyane_Enzo-printemps","Ognjen_Riyane_Enzo-ete",
                         "Ognjen_Riyane_Enzo-hiver","Ognjen_Riyane_Enzo-bois","Ognjen_Riyane_Enzo-metal","Ognjen_Riyane_Enzo-paradis","Ognjen_Riyane_Enzo-enfer"]
    n = 0
    joueur1 = 0
    joueur2 = 1
    nbpion = [3,5,6,7,9,10,12]
    epaisseur = 2
    wallpaper = 0
    while new_game:
        cree_fenetre(taille, taille)
        noir = []
        blanc = []
        jouer = True
        new_game = False
        option = True
        while option == True:
            jouer, option = main_menu(wallpaper, joueur1)
            if option == True:
                options(taille, n, joueur1, joueur2, epaisseur, wallpaper , couleurs, fde)
                taille, n, joueur1, joueur2, epaisseur, wallpaper, option = modif(nbpion, joueur1, joueur2, epaisseur, wallpaper, n, taille)

                ferme_fenetre()
                cree_fenetre(taille, taille)
        case = taille//15
        n = nbpion[n]
        wallpaper = fichiers_images[wallpaper]
        deplacements_possibles, lstvalide, nb_pions, solu = coups_deplacements_possibles(n)
        while jouer == True:
            efface_tout()
            affichemap(taille, n, joueur1, joueur2)
            perdant, pions_sup_blanc, pions_sup_noir = coup_valide_p_1_2_3(blanc, noir, n)
            vinqueur, score1, score2 = gagnant(blanc, noir, perdant, joueur1, joueur2, score1, score2)
            print(f"{vinqueur} won the game !")
            new_game = fin_menu(pions_sup_blanc, pions_sup_noir, score1, score2, vinqueur)
            if new_game == True:
                ferme_fenetre()
            n = nbpion.index(n)
            wallpaper = fichiers_images.index(wallpaper)
            jouer = False
