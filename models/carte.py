from enums import Couleur, Valeur

class Carte:
    """
    Classe représentant une carte pour un jeu de solitaire.
    """

    def __init__(self, valeur: Valeur, couleur: Couleur) -> None:
        """
        Initialise une carte avec une valeur et une couleur.

        Args:
            valeur (Valeur): La valeur de la carte (As, Deux, ..., Roi).
            couleur (Couleur): La couleur de la carte (Pique, Cœur, Carreau, Trèfle).
        """
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle de la carte.

        Returns:
            str: La représentation sous forme "Valeur de Couleur".
        """
        return f"{self.valeur} de {self.couleur}"

    def __eq__(self, autre_carte: object) -> bool:
        """
        Vérifie si deux cartes sont égales.

        Args:
            autre_carte (object): L'autre carte à comparer.

        Returns:
            bool: True si même valeur et couleur, False sinon.
        """
        if not isinstance(autre_carte, Carte):
            return False
        return self.valeur == autre_carte.valeur and self.couleur == autre_carte.couleur

    def est_rouge(self) -> bool:
        """
        Vérifie si la carte est rouge (Cœur ou Carreau).

        Returns:
            bool: True si rouge, False sinon.
        """
        return self.couleur.est_rouge()

    def est_noir(self) -> bool:
        """
        Vérifie si la carte est noire (Pique ou Trèfle).

        Returns:
            bool: True si noire, False sinon.
        """
        return self.couleur.est_noir()
