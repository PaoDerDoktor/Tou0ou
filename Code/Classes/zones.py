class Sea:
	"""Objet représentant une mer"""
	def __init__(self,corrosive,name):
		self.corrosive = corrosive
		self.name = name

class Forest:
	"""Objet représentant une forêt"""
	def __init__(self,density,highness,name):
		self.density = density
		self.highness = highness
		self.name = name

class Void:
	"""Objet représentant du Vide, comme l'Espace ou lors d'un vol"""
	def __init__(self,name,inertia):
		self.name = name
		self.inertia = inertia

class Mountain:
	"""Objet représentant une montagne"""
	def __init__(self,name,highness,coefficient):
		self.coefficient = coefficient
		self.name = name
		self.highness = highness