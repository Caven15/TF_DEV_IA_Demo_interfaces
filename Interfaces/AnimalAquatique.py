from abc import ABC, abstractmethod
from Interfaces.Animal import Animal
# Interface pour les animaux aquatique
class AnimalAquatique(Animal, ABC):
    @abstractmethod
    def nager(self):
        pass