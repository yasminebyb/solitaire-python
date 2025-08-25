from typing import List
from models.carte import Carte  # ou .carte si c'est dans le même package
import random   

class Paquet:
    """
    Classe représentant un paquet de cartes pour un jeu de solitaire.
    Un paquet est constitué d'une liste de cartes et peut être mélangé. 
    """
    def __init__(self, cartes: List[Carte]) -> None:
        """
        Initialise un paquet de cartes.

        Args:
            cartes (List[Carte]): Liste de cartes à inclure dans le paquet.
        """
        self.cartes = cartes
        self.taille = len(cartes)
        self.est_melange = False      

    def melanger(self) -> None:
        """
        Mélange le paquet de cartes.

        Modifie l'état du paquet pour indiquer qu'il a été mélangé.
        """
        random.shuffle(self.cartes)
        self.est_melange = True 

    def tirer_carte(self) -> Carte:
        """
        Tire une carte du paquet.

        Returns:
            Carte: La carte tirée du paquet.

        Raises:
            IndexError: Si le paquet est vide.
        """
        if not self.cartes:
            raise IndexError("Le paquet est vide, impossible de tirer une carte.")
        return self.cartes.pop()
    
    def afficher(self) -> List[Carte]:
        """
        Affiche les cartes du paquet.

        Returns:
            List[Carte]: Liste des cartes dans le paquet.
        """
        return self.cartes

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle du paquet de cartes.

        Returns:
            str: Représentation du paquet sous forme de chaîne de caractères.
        """
        return ', '.join(str(carte) for carte in self.cartes)                   

    def __eq__(self, autre_paquet: 'Paquet') -> bool:
        """
        Vérifie si deux paquets de cartes sont égaux.

        Args:
            autre_paquet (Paquet): L'autre paquet à comparer.

        Returns:
            bool: True si les paquets contiennent les mêmes cartes, False sinon.
        """
        return sorted(self.cartes) == sorted(autre_paquet.cartes)      