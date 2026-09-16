class Personnage :
    """Classe de personnage"""
    def __init__(self, pseudo: str, niveau: int = 1):
        """
        Arguments :
        pseudo : str nom du personnage
        niveau : int niveau du personnage

        """
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__pv = niveau
        self.__init = niveau

    @property
    def init(self):
        return self.__init

    @property
    def pv(self):
        return self.__pv


    def attaque(self, opposant : Personnage) ->None:

        if opposant.__init < self.__init:
            opposant.__pv = opposant.__pv - self.__niveau
            if opposant.__pv > 0:
                self.__pv = self.__pv - opposant.__niveau

        elif opposant.__init == self.__init
             opposant.__pv = opposant.__pv - self.__niveau
             self.__pv = self.__pv - opposant.__pv

        else
            self.__pv = self.__pv - opposant.__niveau
            if self.__pv < 0:
                opposant.__pv = opposant.__pv - self.__niveau

    def combattre(self, opposant : Personnage) -> str :
        while self.__pv > 0 and opposant.__pv > 0:
            self.attaque(opposant)
            print(f"{self.__pseudo} ({self.__pv} PV) vs {autre.__pseudo} ({autre.__pv} PV)")

    def soigner (self):
        self.__pv = self.__niveau

class Guerrier(Personnage) :

    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.pv = niveau * 8 + 4
        self.init = niveau * 4 + 6

class Mage(Personnage) :

    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.pv = niveau * 5 + 10
        self.init = niveau * 6 + 4
        self.mana = niveau * 5

    def degats(self):
        if self.__mana >= 4:
            self.__mana -= 4
            return self.niveau * 3
        return self.niveau

class Joueur:
    def __init__(self, nom, max_personnages):
        self.__nom = nom
        self.__max_personnages = max_personnages
        self.__personnages = []
