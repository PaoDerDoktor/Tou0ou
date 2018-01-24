class Enemy:
	"""Objet représentant les ennemis"""

	def __init__(self,name,HP,pilotName,enemyType,level,XPDrop,objectDropChances,speed):
		self.name = name
		self.HP = HP
		self.pilotName = pilotName
		self.enemyType = enemyType
		self.level = level
		self.XPDrop = XPDrop
		self.objectDropChances = objectDropChances
		self.speed = speed

class Boss:
	"""Objet représentant un Boss"""

	def __init__(self,name,HP,pilotName,enemyType,level,XPDrop,objectDropChances,specialAmmo1,specialAmmo2,system1HP,system2HP,system3HP,system4HP,system5HP,dialogueFile,speed):
		self.name = name
		self.HP = HP
		self.pilotName = pilotName
		self.enemyType = enemyType
		self.level = level
		self.XPDrop = XPDrop
		self.objectDropChances = objectDropChances
		self.specialAmmo1 = specialAmmo1
		self.specialAmmo2 = specialAmmo2
		self.system1HP = system1HP
		self.system2HP = system2HP
		self.system3HP = system3HP
		self.system4HP = system4HP
		self.system5HP = system5HP
		self.dialogueFile = dialogueFile
		self.speed = speed

	def attack(self, perso2)

class Battery:
	"""Objet représentant une batterie d'armes"""
	def __init__(self,name,HP,pilotNameDictionary,enemyType,level,XPDrop,objectDropChances,weaponNumber,weaponShotTypesDictionary):
		self.name = name
		self.HP = HP
		self.pilotNameDictionary = pilotNameDictionary
		self.enemyType = enemyType
		self.level = level
		self.XPDrop = XPDrop
		self.objectDropChances = objectDropChances
		self.weaponNumber = weaponNumber
		self.weaponShotTypesDictionary = weaponShotTypesDictionary
