class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def hit(self, points):
        self.health -= points
    
    def isAlive(self):
        return self.health > 0
    
    def __str__(self):
        return f'{self.name}, Class: {self.__class__.__name__}, Strength: {self.strength}, Health: {self.health}'

class Warrior(Character):
    pass

class Mage(Character):
    pass

class Archer(Character):
    pass
