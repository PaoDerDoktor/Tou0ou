def importerModules():
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
    #Importation de la bibliothèque de base sys permettant d'interragir avec Python et le système
    import sys
    #Importation de fonctions la bibliothèque de base OS permettant d'intéragir avec le système d'exploitation
    from os import (
        chdir                   #Import de la fonction permettant de naviguer dans les dossiers
    )
    #Importation de pygame
    import pygame
