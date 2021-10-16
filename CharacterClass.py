import random
import ItemClass as IC

class Player():
    def __init__(self):
        self.Health = 10
        self.Inventory = []
    

class NPC():
    def __init__(self, Name):
        self.name = Name
        self.dialouge = ""

    def setDialouge(self, dialouge):
        self.dialouge = dialouge

    def speak(self):
        if self.dialouge != "":
            print("[",self.name,"]:",self.dialouge)
        else:
            print(self.name,"Does not want to speak to you right now")

class Enemy(NPC):
    def __init__(self, Name):
        super.__init__(Name)
        self.Health = random.randint(1, 10)
        self.Damage = random.randint(1, 3)
    
    def Attack(self):
        pass
    
class Merchant(NPC):
    def __init__(self, Name):
        super().__init__(Name)
        soldItems = []
    
    def AddWeaponToShop(self):
        self.soldItems.append(IC.WeaponFactory())