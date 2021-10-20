import CharacterClass as CC
import random

class Room():
    def __init__(self, Name, Description):
        self.name = Name
        self.description = Description
        self.Inhabitants = []
        
    def AddNewInhabitant(self, NewPerson):
        self.Inhabitants.append(NewPerson)

    def GetRoomName(self):
        return self.name
    def GetRoomInfo(self):
        return self.description
    
    def GetInhabitants(self):
        for i in range(0, len(self.Inhabitants)):
            print(i,":",self.Inhabitants[i].name)
        
        ValidNumber = False
        while not ValidNumber:
            UserIn = input()
            ValidNumber = UserIn.isdigit()
            if not ValidNumber:
                print("Must be a number, try again")
        
        from main import Player
        chosenPerson = int(UserIn)%len(self.Inhabitants)
        self.Inhabitants[chosenPerson].SaleOption(Player)
        

class GameHandeler():
    def __init__(self):
        self.RoomList = []
        self.currentRoom = 0 #index of room in List of ROoms
        self.Connections = []
        self.incounterPercentage = 50 #how often in % do you get attacked

    def PrintCurrentRoomInfo(self):
        print("\n--", self.RoomList[self.currentRoom].name, "--")
        print(self.RoomList[self.currentRoom].description)
        if len(self.RoomList[self.currentRoom].Inhabitants) != 0:
            print("Their are", len(self.RoomList[self.currentRoom].Inhabitants),"inhabitans in the room")
        print("")

    def AddRoom(self, Room):
        self.RoomList.append(Room)

    def addConnection(self, Room1, Room2, Direction):
        self.Connections.append([Room1, Room2, Direction])

    def WhatUDoin(self):
        if len(self.RoomList[self.currentRoom].Inhabitants) != 0:
            print("press (i) to talk to people in the room")
        print("Press (m) to move room")
        self.WhatImDoin = input().lower()
        if self.WhatImDoin == "m":
            self.RoomExits()
            self.MoveRoom()
            self.GenorateEncounter()
        elif self.WhatImDoin == "i":
            self.RoomList[self.currentRoom].GetInhabitants()

    def RoomExits(self):
        self.ExitList = self.GetRoomExits()
        for exits in self.ExitList:
            if exits[1][0] == "-":
                if exits[1] == "-north":
                    exits[1] = "south"
                if exits[1] == "-south":
                    exits[1] = "north"
                if exits[1] == "-east":
                    exits[1] = "west"
                if exits[1] == "-west":
                    exits[1] = "east"
            print(exits[1]+": "+exits[0].name)
    
    def GetRoomExits(self):
        self.Room = self.RoomList[self.currentRoom]
        exits = []
        for Connection in self.Connections:
            if self.Room in Connection:
                if self.Room == Connection[0]:
                    exits.append([Connection[1], Connection[2]])
                else:
                    FlippedSign = "-"+str(Connection[2])
                    exits.append([Connection[0], FlippedSign])
        return exits

    def MoveRoom(self):

        validInput = False
        while not validInput:
            PlayerIn = input("Which direction do you want to go?\n").lower()
            for exit in self.ExitList:
                if PlayerIn == exit[1]:
                    validInput = True
                    self.currentRoom = self.RoomList.index(exit[0])
            if not validInput:
                print("you try really hard to go",PlayerIn,"but you cannot")
    
    def GenorateEncounter(self):
        attackedNum = random.randint(0,100)
        if attackedNum > self.incounterPercentage:
            Enemy = CC.CreateEnemy()
            print("you where attacked by",Enemy.name)



def RoomsINIT(className):
    EntranceHall = Room("Entrance Hall", "A long dark hallway with a dim flickering light\n")
    StarterMerchant = CC.Merchant("Jhon")
    EntranceHall.AddNewInhabitant(StarterMerchant)
    className.AddRoom(EntranceHall)
    DiningRoom = Room("Dining Room", "A large room with a old wood table covered in moldy food\n")
    className.AddRoom(DiningRoom)
    LivingRoom = Room("Living Room", "Your average living room but full of dead bodys, its not very living\n")
    className.AddRoom(LivingRoom)

    className.addConnection(EntranceHall, DiningRoom, "north")
    className.addConnection(EntranceHall, LivingRoom, "east")
    print("Rooms Created")
    