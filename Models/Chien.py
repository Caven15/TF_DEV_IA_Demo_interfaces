from Interfaces.AnimalTerrestre import AnimalTerrestre

# Class représentant un chien
class Chien(AnimalTerrestre):
    def parler(self):
        return "Le chien aboie !"

    def marcher(self):
        return "le chien marche sur ses quatre pattes"