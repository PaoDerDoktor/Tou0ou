class Slower:
	"""Objet représentant les obstacles ralentissant et/où donnant des dégâts"""
	def __init__(self,coefficient,affectsList,damage,canKill,obstacleType,name):
		self.coefficient = coefficient
		self.affectsList = affectsList
		self.damages = damages
		self.canKill = canKill
		self.obstacleType = obstacleType
		self.name = name

class Swamp:
	"""Objet représentant une tile, une partie de tile dans laquelle on s'enfonce et ralentit"""
	def __init__(self,coefficient,affectsList,canKill,obstacleType,name,maxDeep,deepCoordinates):
		self.coefficient = coefficient
		self.affectsList = affectsList
		self.canKill = canKill
		self.obstacleType = obstacleType
		self.name = name
		self.maxDeep = maxDeep
		self.deepCoordinates = deepCoordinates

class Lake:
	"""Objet représentant une vaste étendue d'eau"""
	def __init__(self,maxDeep,deepCoordinates,name,affectsList,obstacleType):
		self.maxDeep = maxDeep
		self.deepCoordinates = deepCoordinates
		self.name = name
		self.obstacleType = obstacleType
		self.affectsList = affectsList

class Damager:
	"""Objet représentant une étendue de matière toxique/corrosive de faible profondeur"""
	def __init__(self,damage,affectsList,obstacleType,name):
		self.obstacleType = obstacleType
		self.affectsList = affectsList
		self.name

class MovingObject:
	"""Objet représentatnt un objet volant en mouvement"""
	def __init__(self,damage,speed,name,mass,canKill,affectsList):
		self.damage = damage
		self.speed = speed
		self.name = name
		self.mass = mass
		self.canKill = canKill
		self.affectsList = affectsList

class StillObject:
	"""Un objet représentant un objet immobile, comme un arbre ou un rocher"""
	def __init__(self,name,damage,canKill,mass,integrity,affectsList):
		self.name = name
		self.damage = damage
		self.canKill = canKill
		self.mass = mass
		self.integrity = integrity
		self.affectsList = affectsList

class Drifter:
	"""Un objet représentant un objet glissant, comme du verglas à notre échelle"""
	def __init__(self,name,driftRate,affectsList):
		self.name = name
		self.driftRate = driftRate
		self.affectsList = affectsList