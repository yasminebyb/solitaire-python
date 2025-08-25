"""
Définition de l'énumération Valeur pour les cartes du jeu.
"""

from enum import Enum


class Valeur(Enum):
    """Les treize valeurs possibles d’une carte."""
    AS = 1
    DEUX = 2
    TROIS = 3
    QUATRE = 4
    CINQ = 5
    SIX = 6
    SEPT = 7
    HUIT = 8
    NEUF = 9
    DIX = 10
    VALET = 11
    DAME = 12
    ROI = 13

    def __str__(self) -> str:
        noms = {
            Valeur.AS: "As",
            Valeur.DEUX: "Deux",
            Valeur.TROIS: "Trois",
            Valeur.QUATRE: "Quatre",
            Valeur.CINQ: "Cinq",
            Valeur.SIX: "Six",
            Valeur.SEPT: "Sept",
            Valeur.HUIT: "Huit",
            Valeur.NEUF: "Neuf",
            Valeur.DIX: "Dix",
            Valeur.VALET: "Valet",
            Valeur.DAME: "Dame",
            Valeur.ROI: "Roi"
        }
        return noms[self]
