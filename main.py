from Models.Chien import Chien
from Models.Poisson import Poisson
from Models.Python import Python

# Fonction d'affichage dans le chat
def afficherChat(texte):
    return(print(f'Alexa : {texte}'))

if __name__ == "__main__":
    chien = Chien()
    afficherChat(chien.parler())
    afficherChat(chien.marcher())
    
    python = Python()
    afficherChat(python.parler())
    afficherChat(python.marcher())

    poisson = Poisson()
    afficherChat(poisson.parler())
    afficherChat(poisson.nager())

