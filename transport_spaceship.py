from spaceship import Spaceship

class TransportSpaceship(Spaceship):
    def __init__(self, name, crewQuantity, places):
        super().__init__(name, crewQuantity)
        self.places = places