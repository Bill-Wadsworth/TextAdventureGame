class Room():
    def __init__(self, Name, Description):
        self.name = Name
        self.description = Description

    def GetRoomName(self):
        return self.name
    def GetRoomInfo(self):
        return self.description

class ConnectionHandeler():
    def __init__(self):
        self.Connections = []

    def addConnection(self, Room1, Room2, Direction):
        self.Connections.append([Room1, Room2, Direction])
    
    def GetRoomExits(self, Room):
        for Connection in self.Connections:
            if Room in Connection:
                if Room == Connection[0]:
                    return Room, Connection[2]
                else:
                    FlippedSign = "-"+str(Connection[2])
                    return Room, FlippedSign


class GameHandeler():
    def __init__(self):
        self.RoomList = []
        self.currentRoom = 0 #index of room in List of Rooms

    def AddRoom(self, RoomName, RoomDescription):
        self.RoomList.append(Room(RoomName, RoomDescription))

    def MoveRoom(self):
        pass
