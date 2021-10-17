import random

class Item():
    def __init__(self, Name, Desciption, Value):
        self.name = Name
        self.description = Desciption
        self.value = Value

def WeaponFactory():
    randWeaponNames = ["Chesse", "Moldy Chesse", "Wooden Sword", "Diamond Sword", "Bat", "Machine Gun"]
    randWeaponDescription = ["Oddly sharp", "Comically large", "very pointy", "boring", "smells really really bad"]
    weapon = Weapon(randWeaponNames[random.randint(0, len(randWeaponNames)-1)], randWeaponDescription[random.randint(0, len(randWeaponDescription)-1)])
    return weapon

class Weapon(Item):
    def __init__(self, Name, Desciption):
        super().__init__(Name, Desciption, 10)
        self.Damage = random.randint(0,5)