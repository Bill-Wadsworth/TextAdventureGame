import RoomClass as RC

GameRunner = RC.GameHandeler()
RC.RoomsINIT(GameRunner)

GameLoop = True
while GameLoop:

    GameRunner.PrintCurrentRoomInfo()
    GameRunner.RoomExits()
    move = input()


