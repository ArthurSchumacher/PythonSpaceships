class Spaceship:
    def __init__(self, name, crewQuantity):
        self.name = name
        self.crewQuantity = crewQuantity
        self.velocity = 0
    
    def speedUp(self, acceleration):
        self.velocity += acceleration
    
    def printData(self):
        print(f'\nNome: {self.name}')
        print(f'Quantidade de tripulantes: {self.crewQuantity}')
        print(f'Velocidade atual: {self.velocity}\n')