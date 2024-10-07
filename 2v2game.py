from characters import Warrior, Mage, Archer

def battle(char1, char2):
    while char1.isAlive() and char2.isAlive():
        char2.hit(char1.attack())
        if char2.isAlive():
            char1.hit(char2.attack())
        print(char1)
        print(char2)
    
    if char1.isAlive():
        print(f'{char1.name} wins!')
    else:
        print(f'{char2.name} wins!')

if __name__ == "__main__":
    char1 = Warrior(name="Warrior", health=100, strength=10)
    char2 = Mage(name="Mage", health=80, strength=12)
    battle(char1, char2)
