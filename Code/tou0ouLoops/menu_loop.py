def menu_loop(w,clock,testMode,pygame):
	"""
		Boucle pygame pour le menu de tou0ou
	"""
	print("Lancement de la boucle du menu...")

	#VARIABLES DE TEST & IMPORT DE VARIABLES

	pygameMenuRuns = True

	#INITIALISATION DE VARIABLES

		#FONTS

	TOU0OU_MENU_BUTTONS_FONT = pygame.font.Font('../SystemFiles/Fonts/joystixMonospace.ttf', 32)

		#OBJETS COULEURS

	brighterMiamiPink   = pygame.Color(253,   0, 225)
	brightMiamiPink     = pygame.Color(228,   0, 247)
	brightMiamiBlue     = pygame.Color(  0, 255, 213)
	brighterMiamiBlue   = pygame.Color(  0, 253, 241)
	black               = pygame.Color(  0,   0,   0)
	retroYellow         = pygame.Color(224, 198,  27)

		#VARIABLES DE CHOIX

	choice = 0

		#TEXTES

	leftButtonText      = "Nouvelle Partie"
	middleButtonText    = "Charger une Partie"
	rightButtonText     = "options"
	titre               = "TOU0OU"

		#LABELS

	newGameLabel = TOU0OU_MENU_BUTTONS_FONT.render("Nouvelle Partie", True, retroYellow)
	newGameRect  = newGameLabel.get_rect()
	pygame.draw.rect(w, brightMiamiBlue, newGameRect)

	#ACTIONS

	w.fill(black)
	w.blit(newGameLabel, (0,0))
	pygame.display.flip()

	#BOUCLE PYGAME

	while pygameMenuRuns :
		if testMode :
			print("MODE TEST")
		else :
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygameMenuRuns = False
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
					pygameMenuRuns = False
		clock.tick(60)
