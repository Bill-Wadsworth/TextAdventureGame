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
        print("--", self.RoomList[self.currentRoom].name, "--")
        print(self.RoomList[self.currentRoom].description)

    def AddRoom(self, Room):
        self.RoomList.append(Room)

    def addConnection(self, Room1, Room2, Direction):
        self.Connections.append([Room1, Room2, Direction])

    def RoomExits(self):
        self.ExitList = self.GetRoomExits()
        for exits in self.ExitList:
            if exits[1][0] == "-":
                print("FLIP DIRECTION")
            else:
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
        pass


def RoomsINIT(className):
    EntranceHall = Room("Entrance Hall", "A long dark hallway with a dim flickering light")
    className.AddRoom(EntranceHall)
    DiningRoom = Room("Dining Room", "A large room with a olf wood table covered in moldy food")
    className.AddRoom(DiningRoom)
    LivingRoom = Room("Living Room", "Your average living room but full of dead bodys, its not very living")
    className.AddRoom(LivingRoom)

    className.addConnection(EntranceHall, DiningRoom, "North")
    className.addConnection(EntranceHall, LivingRoom, "East")
    print("Rooms Created")
    