from models.carte import Carte
from typing import List
from random import shuffle  

class Pioche:
    """Représente la pioche de cartes (tas face cachée) dans un jeu de solitaire."""

    def __init__(self, cartes: List[Carte]) -> None:
        """
        Initialise une pioche avec une liste de cartes.

        Args:
            cartes (List[Carte]): Liste de cartes à inclure dans la pioche.
        """
        self.cartes = cartes

    def tirer_carte(self) -> Carte:
        """
        Tire une carte de la pioche.

        Returns:
            Carte: La carte tirée de la pioche.

        Raises:
            IndexError: Si la pioche est vide.
        """
        if not self.cartes:
            raise IndexError("La pioche est vide, impossible de tirer une carte.")
        self.taille -= 1
        return self.cartes.pop()
    
   
    def remettre(self, cartes: List[Carte]) -> None:
        """Remet des cartes dans la pioche (souvent depuis la défausse)."""
        self.cartes.extend(cartes)
        shuffle(self.cartes)
    
    def est_vide(self) -> bool:
        """
        Vérifie si la pioche est vide.

        Returns:
            bool: True si la pioche est vide, False sinon.
        """
        return len(self.cartes) == 0    
    
    def taille(self) -> int:
        """
        Retourne le nombre de cartes restantes dans la pioche.

        Returns:
            int: Nombre de cartes dans la pioche.
        """
        return len(self.cartes)
    
    def __str__(self) -> str:
        """
        Retourne une représentation textuelle de la pioche.

        Returns:
            str: Représentation de la pioche sous forme de chaîne de caractères.
        """
        return f"Pioche avec {len(self.cartes)} cartes restantes."
    
    