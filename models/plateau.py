from typing import List, Dict
from models.paquet import Paquet
from models.carte import Carte
from enums import Couleur, Valeur
from models.fondation import Fondation
from models.colonne import Colonne
from models.pioche import Pioche
from models.defausse import Defausse


class Plateau:
    """
    Plateau principal du jeu de solitaire, contenant toutes les structures du jeu.
    """

    def __init__(self) -> None:
        """
        Initialise un plateau complet avec colonnes, pioche, défausse et fondations.
        """

        self.colonnes: List[Colonne] = []
        self.pioche: Pioche = Pioche([])
        self.defausse: Defausse = Defausse()
        self.fondations: Dict[Couleur, Fondation] = {
            Couleur.COEUR: Fondation(Couleur.COEUR),
            Couleur.CARREAU: Fondation(Couleur.CARREAU),
            Couleur.PIQUE: Fondation(Couleur.PIQUE),
            Couleur.TREFLE: Fondation(Couleur.TREFLE),
        }   
        
        # Génération du paquet complet
        cartes = [Carte(valeur, couleur) for couleur in Couleur for valeur in Valeur]
        paquet = Paquet(cartes)
        paquet.melanger()


        # Distribution des carrtes dans les 7 colonnes (1 à 7 cartes)
        self._distribuer_colonnes(paquet)

        # Le reste va dans la pioche
        self.pioche: Pioche = Pioche(paquet.cartes)

    def _distribuer_colonnes(self, paquet: Paquet) -> None:
        """
        Distribue les cartes du paquet dans les 7 colonnes selon les règles du solitaire.

        Args:
            paquet (Paquet): Le paquet de cartes à distribuer.
        """
        for i in range(7):
            cartes_cachees = [paquet.tirer_carte() for _ in range(i)]
            carte_visible = paquet.tirer_carte()
            self.colonnes.append(Colonne(cartes_cachees, [carte_visible]))

    def afficher(self) -> None:
        """
        Affiche l'état actuel du plateau.
        """
        print("== COLONNES ==")
        for i, colonne in enumerate(self.colonnes, 1):
            print(f"Colonne {i} : {colonne}")

        print("\n== FONDATIONS ==")
        for couleur, fondation in self.fondations.items():
            print(f"{couleur} : {fondation}")

        print(f"\n== DEFAUSSE ==\n{self.defausse}")
        print(f"\n== PIOCHE ==\n{self.pioche}")
