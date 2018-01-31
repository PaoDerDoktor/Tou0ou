class Mecha:
    """Classe contenant les informations relatives aux mechas des joueurs"""
    def __init__(self,HP,style,laserAmmo,shieldEnergy,bombAmmo,level):
        self.HP = HP
        self.style = style
        self.laserAmmo = laserAmmo
        self.shiedlEnergy = shieldEnergy
        self.bombAmmo = bombAmmo
        self.level = level
