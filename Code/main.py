#Importation du coeur de PyQt5, dont le timer.
from PyQt5.QtCore import (
    Qt,                     #Classe de base
    QBasicTimer             #Timer 
)
#Importation des outils du GUI
from PyQt5.QtGui import (
    QBrush,                 #Pinceau
    QPixmap,                #Map matricielle
    QIcon                   #Icone de la fenêtre
)
#Importation de quelques widgets (window gadgets) de PyQt5
from PyQt5.QtWidgets import (
    QApplication,           #Import de la classe de la fenêtre
    QWidget,                #Import de la classe de base QWidget
    QGraphicsItem,          #Import de la classe des items graphiques
    QGraphicsPixmapItem,    #Import de la classe des graphismes des maps matricielles
    QGraphicsRectItem,      #Import d'une classe permettant de créer un rectangle
    QGraphicsScene,         #Import de la classe des scènes
    QGraphicsView           #Import d'une classe permettant l'affichage des graphismes
)
#Importation des widgets multimédia de PyQt5
from PyQt5.QtMultimedia import (
    QSound                  #Import de la classe des sons
)
#Importation de note bibliothèque de simplification de PyQt5 : PyCutie5
from PyCutie5 import (
    audioSelect,            #Import de la fonction de sélection/lancement des fichiers audios
    windowBuild             #Import de la fonction de création de fenêtre
)
#Importation de nos classes pour tou0ou
from tou0ouClasses import (
    chara,                  #Classes des personages
    mecha,                  #Classes des Mecha
    obstacles,              #Classes des obstacles
    zones                   #Classes des zones et tiles
)
#Importation de la bibliothèque de base sys permettant d'interagir entre Python et le système Python
import sys
#Importation de fonctions la bibliothèque de base OS permettant d'intéragir avec le système d'exploitation
from os import (
    chdir                   #Import de la fonction permettant de naviguer dans les dossiers
)
#Importation de pygame
import pygame

from PyCutie5 import (
    audioSelect,
    fullImport,
    windowBuild
)

from tou0ouLoops import (
    menu_loop
)

#FONCTIONS

def swap_colors():
    """
        La fonction échange les couleurs du texte et du fond dans l'accueil.
    """
    global currentBGColor, currentTextColor, LABEL, w
    if currentBGColor == brighterMiamiPink:
        currentBGColor   = brightMiamiBlue
        currentTextColor = brighterMiamiPink
    else:
        currentBGColor   = brighterMiamiPink
        currentTextColor = brightMiamiBlue
    LABEL = TOU0OU_WELCOME_FONT.render(TOU0OU_WELCOME_TEXT, 1, currentTextColor)
    w.fill(currentBGColor)
    w.blit(LABEL, (4,4))
    pygame.display.flip()

#INITIALISATION DE PYGAME

pygame.init()

#INITIALISATION DES COULEURS

brighterMiamiPink   = pygame.Color(253,   0, 225)
brightMiamiPink     = pygame.Color(228,   0, 247)
brightMiamiBlue     = pygame.Color(  0, 255, 213)
brighterMiamiBlue   = pygame.Color(  0, 253, 241)
black               = pygame.Color(  0,   0,   0)
retroYellow         = pygame.Color(224, 198,  27)

#INITIALISATION DES CONSTANTES

INFO_OBJECT         = pygame.display.Info()
W_HEIGHT            = INFO_OBJECT.current_h
W_WIDTH             = INFO_OBJECT.current_w
AUTHOR              = ['CASTEL Benjamin', 'CRAND Juliben', 'GRIVEL Sonia', 'ROUMANI Rudy']
VERSION             = 'Tou0ou V.0.1.1 [ALPHA]'
TOU0OU_ICON         = pygame.image.load('../SystemFiles/Icons/tou0ouIcon.png')
TOU0OU_WELCOME_TEXT = 'Tou0ou is alive !'
TOU0OU_WELCOME_FONT = pygame.font.Font('../SystemFiles/Fonts/RetroComputer.ttf', 32)
LABEL               = TOU0OU_WELCOME_FONT.render(TOU0OU_WELCOME_TEXT, 1, brightMiamiBlue)

#OBJETS

currentBGColor   = brighterMiamiPink
currentTextColor = brightMiamiBlue
clock            = pygame.time.Clock()

#PARAMETRAGE DE PYGAME

w=pygame.display.set_mode((W_WIDTH,W_HEIGHT))
pygame.display.set_caption(VERSION)
pygame.display.set_icon(TOU0OU_ICON)

#MODE DE TEST ?

testMode = False

#BOUCLE PYGAME

pygame.display.flip()

pygameRun = True

while pygameRun :
    if testMode :
        w.fill(brighterMiamiPink)
        w.blit(LABEL, (0,0))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            swap_colors()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygameRun = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                pygameRun = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_z :
                pygameRun = False
        clock.tick(0.5)
        swap_colors()
    else :
        menu_loop.menu_loop(w,clock,testMode,pygame)
        pygameRun = False
