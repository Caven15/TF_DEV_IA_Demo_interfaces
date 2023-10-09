from abc import ABC, abstractmethod
from Interfaces.Animal import Animal
# Interface pour les animaux terrestre
class AnimalTerrestre(Animal, ABC):
    @abstractmethod
    def marcher(self):
        pass