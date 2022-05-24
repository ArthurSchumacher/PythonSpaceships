from spaceship import Spaceship

class BattleSpaceship(Spaceship):
    def __init__(self, name, crewQuantity, weaponsQuantity):
        super().__init__(name, crewQuantity)
        self.weaponsQuantity = weaponsQuantity