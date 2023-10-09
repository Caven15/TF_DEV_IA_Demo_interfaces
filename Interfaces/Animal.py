from abc import ABC, abstractmethod
# Interface pour les animaux
class Animal(ABC):
    
    @abstractmethod
    def parler(self):
        pass