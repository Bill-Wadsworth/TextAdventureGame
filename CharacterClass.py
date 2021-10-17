import random
import ItemClass as IC

class Player():
    def __init__(self):
        self.Health = 10
        self.Inventory = []
        self.wealth = 10
    

class NPC():
    def __init__(self, Name):
        self.name = Name
        self.dialouge = ""

    def setDialouge(self, dialouge):
        self.dialouge = dialouge

    def speak(self):
        if self.dialouge != "":
            print("["+self.name+"]:",self.dialouge)
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
        self.soldWeapon = ""
        self.HealRate = random.randint(0,5)
        self.soldItems = IC.WeaponFactory()
    
    def BuyItems(self):
        pass
    
    def SellAnItem(self):
        self.sale = random.randint(0,3)
        if self.sale == 0: #No Sale
            self.setDialouge("I am not selling anything right now, come back later")
        if self.sale == 1: #Sell Heal
            self.setDialouge("Here traveler i have a med kit but it will cost you 5 gold\n[y/n]: ")
        if self.sale == 2: #Sell Weapon
            self.setDialouge("I found this weapon and i will sell it to you for a small price of 7 gold\n[y/n]: ")
    
    def SaleOption(self, playerClass):
        self.SellAnItem()
        self.speak()
        if self.sale != 0:
            option = input().lower()
            if option == "y" and playerClass.wealth >= self.saleCost:
                if self.sale == 1:
                    playerClass.health += self.HealRate
                    print("You where healed by", self.HealRate)
                elif self.sale == 2:
                    playerClass.Inventory.append(self.soldWeapon)
            elif option == "n":
                print("Ok, suit yourslef")
            else:
                print("I dont know what that means but you have missed your chance now")
        