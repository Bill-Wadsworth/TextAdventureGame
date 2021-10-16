import RoomClass as RC
import CharacterClass as CC

GameRunner = RC.GameHandeler()
RC.RoomsINIT(GameRunner)

GameLoop = True
while GameLoop:

    GameRunner.PrintCurrentRoomInfo()
    GameRunner.RoomExits()
    GameRunner.MoveRoom()
