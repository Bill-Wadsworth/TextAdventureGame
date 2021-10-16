class Room():
    def __init__(self, Name, Description):
        self.name = Name
        self.description = Description

    def GetRoomName(self):
        return self.name
    def GetRoomInfo(self):
        return self.description

class GameHandeler():
    def __init__(self):
        self.RoomList = []
        self.currentRoom = 0 #index of room in List of ROoms
        self.Connections = []

    def PrintCurrentRoomInfo(self):
        print("\n--", self.RoomList[self.currentRoom].name, "--")
        print(self.RoomList[self.currentRoom].description)

    def AddRoom(self, Room):
        self.RoomList.append(Room)

    def addConnection(self, Room1, Room2, Direction):
        self.Connections.append([Room1, Room2, Direction])

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


def RoomsINIT(className):
    EntranceHall = Room("Entrance Hall", "A long dark hallway with a dim flickering light\n")
    className.AddRoom(EntranceHall)
    DiningRoom = Room("Dining Room", "A large room with a old wood table covered in moldy food\n")
    className.AddRoom(DiningRoom)
    LivingRoom = Room("Living Room", "Your average living room but full of dead bodys, its not very living\n")
    className.AddRoom(LivingRoom)

    className.addConnection(EntranceHall, DiningRoom, "north")
    className.addConnection(EntranceHall, LivingRoom, "east")
    print("Rooms Created")
    