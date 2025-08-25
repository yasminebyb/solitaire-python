from typing import List
from models.carte import Carte
from enums import Couleur, Valeur


class Fondation:
    """
    Fondation d'une couleur à compléter de l'As au Roi.
    """

    def __init__(self, couleur: Couleur) -> None:
        """
        Initialise une fondation vide pour une couleur donnée.

        Args:
            couleur (Couleur): La couleur de la fondation (ex: Cœur, Pique...).
        """
        self.couleur: Couleur = couleur
        self.cartes: List[Carte] = []

    def peut_ajouter(self, carte: Carte) -> bool:
        """
        Vérifie si une carte peut être ajoutée à la fondation.

        Args:
            carte (Carte): La carte à vérifier.

        Returns:
            bool: True si la carte peut être posée, False sinon.
        """
        if carte.couleur != self.couleur:
            return False
        if not self.cartes:
            return carte.valeur == Valeur.AS
        sommet = self.cartes[-1]
        return carte.valeur.value == sommet.valeur.value + 1

    def ajouter(self, carte: Carte) -> None:
        """
        Ajoute une carte à la fondation si elle est valide.

        Args:
            carte (Carte): La carte à ajouter.

        Raises:
            ValueError: Si la carte ne peut pas être ajoutée.
        """
        if self.peut_ajouter(carte):
            self.cartes.append(carte)
        else:
            raise ValueError(f"Impossible d'ajouter {carte} à la fondation {self.couleur}.")

    def __repr__(self) -> str:
        """
        Représentation textuelle de la fondation.

        Returns:
            str: La couleur et la carte du dessus ou 'vide'.
        """
        if not self.cartes:
            return f"Fondation({self.couleur}): vide"
        return f"Fondation({self.couleur}): {self.cartes[-1]}"

    def est_complete(self) -> bool:
        """
        Vérifie si la fondation est complète (du As au Roi).
        Returns:
            bool: True si la fondation est complète, False sinon.
        """       
        return len(self.cartes) == 13   