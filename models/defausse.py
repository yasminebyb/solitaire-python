from typing import List, Optional
from models.carte import Carte


class Defausse:
    """Représente la pile de défausse dans un jeu de solitaire."""

    def __init__(self) -> None:
        """Initialise une défausse vide."""
        self.cartes: List[Carte] = []

    def ajouter(self, carte: Carte) -> None:
        """Ajoute une carte sur la défausse."""
        self.cartes.append(carte)

    def sommet(self) -> Optional[Carte]:
        """Renvoie la carte du dessus sans la retirer.

        Returns:
            Carte ou None si la défausse est vide.
        """
        if self.est_vide():
            return None
        return self.cartes[-1]

    def retirer(self) -> Carte:
        """Retire et retourne la carte du dessus.

        Returns:
            Carte: La carte retirée.

        Raises:
            IndexError: Si la défausse est vide.
        """
        if self.est_vide():
            raise IndexError("La défausse est vide.")
        return self.cartes.pop()

    def vider(self) -> List[Carte]:
        """Vide la défausse et renvoie toutes les cartes (dans l'ordre inverse).

        Returns:
            List[Carte]: Les cartes de la défausse à remettre dans la pioche.
        """
        cartes = self.cartes[:]
        self.cartes.clear()
        return cartes

    def est_vide(self) -> bool:
        """Indique si la défausse est vide."""
        return not self.cartes

    def __str__(self) -> str:
        """Affiche la carte visible ou indique que la défausse est vide."""
        if self.est_vide():
            return "Défausse vide"
        return f"Défausse : {self.sommet()}"
