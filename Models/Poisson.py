from Interfaces.AnimalAquatique import AnimalAquatique
# classe représentant un poisson
class Poisson(AnimalAquatique):
    def parler(self):
        return "Moris ne parle pas..."

    def nager(self):
        return "Moris nage dans l'eau"

