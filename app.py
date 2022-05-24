from battle_spaceship import BattleSpaceship
from transport_spaceship import TransportSpaceship

class App:
    def __init__(self):
        self.spaceship: object
    
    def start(self):
        self.createSpaceship()
        userOption: int

        while True:
            userOption = self.showMenu()
            self.redirectFeature(userOption)

            if (userOption == 3):
                break
    
    def createSpaceship(self):
        spaceshipName = input('\nInforme o nome de sua nave:\n')
        spaceshipCrewQuantity = int(input('\nInforme a quantidade de tripulantes:\n'))
        spaceshipType = self.askForSpaceshipType()

        if (spaceshipType == 1):
            spaceshipWeapons = int(input('\nInforme a quantidade de armas que sua nave possui:\n'))
            self.spaceship = BattleSpaceship(spaceshipName, spaceshipCrewQuantity, spaceshipWeapons)
        
        if (spaceshipType == 2):
            spaceshipPlaces = int(input('\nInforme a quantidade de lugares disponiveis que sua nave possui:\n'))
            self.spaceship = TransportSpaceship(spaceshipName, spaceshipCrewQuantity, spaceshipPlaces)        
    
    def askForSpaceshipType(self):
        op: int

        while True:
            op = int(input(
                '\nEscolha o tipo de nave:\n' +
                '1. Batalha\n' +
                '2. Transporte\n' +
                'Sua escolha:\n'       
            ))

            if (op == 1 or op == 2):
                return op

    def showMenu(self):
        op: int

        while True:
            op = int(input(
                '\nEscolha uma das opções:\n' +
                '1. Acelerar nave atual\n' +
                '2. Trocar de nave\n' +
                '3. Imprimir dados e sair\n' + 
                'Sua escolha:\n'
            ))

            if (op == 1 or op == 2 or op == 3):
                return op

    def redirectFeature(self, option):
        if (option == 1):
            acceleration = int(input('\nInforme sua aceleração (km/s):\n'))
            self.spaceship.speedUp(acceleration)

        if (option == 2):
            self.createSpaceship()
        
        if (option == 3):
            self.spaceship.printData()
        
