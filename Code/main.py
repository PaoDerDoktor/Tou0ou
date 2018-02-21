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
from tou0ouClasses import (
	chara,
	mecha,
	obstacles,
	zones
	)
import pygame



COLOR = {
	'brighterMiamiPink'   : (249,141,201),
	'brightMiamiPink'     : (247,101,184),
	'reallyPaleMiamiBlue' : (215,255,254),
	'paleMiamiBlue'       : (168,246,248),
	'fluoMiamiBlue'       : ( 39,253,245)
}



def swapColors():
	global COLOR
	global MENU_FONT
	global DIALOGUES_FONT
	global TEXT_COLOR
	global screen
	global menuText
	global BACKGROUND_COLOR


	if BACKGROUND_COLOR == COLOR['brighterMiamiPink']:
		BACKGROUND_COLOR = COLOR['fluoMiamiBlue']
		TEXT_COLOR = COLOR['brighterMiamiPink']
	else :
		BACKGROUND_COLOR = COLOR['brighterMiamiPink']
		TEXT_COLOR = COLOR['fluoMiamiBlue']
	renderThings()


def renderThings():
	menuText = MENU_FONT.render("Tou0ou IS ALIVE !", True, TEXT_COLOR)
	screen.fill(BACKGROUND_COLOR)
	screen.blit(menuText, (0,0))

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()
WINDOW_ICON = pygame.image.load('../SystemFiles/Icons/Tou0ouIcon.ico')
MONITOR_INFO = pygame.display.Info()

MENU_FONT = pygame.font.Font('../SystemFiles/Fonts/RetroComputer.ttf', 72)
DIALOGUES_FONT = pygame.font.Font('../SystemFiles/Fonts/RetroComputer.ttf', 16)
TEXT_COLOR = COLOR['fluoMiamiBlue']
menuText = MENU_FONT.render("Tou0ou IS ALIVE !", True, TEXT_COLOR)
BACKGROUND_COLOR = COLOR['fluoMiamiBlue']
screen = pygame.display.set_mode((MONITOR_INFO.current_w, MONITOR_INFO.current_h), pygame.FULLSCREEN)

screen.fill(BACKGROUND_COLOR)
pygame.display.set_icon(WINDOW_ICON)

#renderThings()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			running = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			swapColors()