import RoomClass as RC
import CharacterClass as CC
import ItemClass as IC

GameRunner = RC.GameHandeler()
RC.RoomsINIT(GameRunner)

Player = CC.Player()

GameLoop = True
while GameLoop:

    GameRunner.PrintCurrentRoomInfo()
    GameRunner.WhatUDoin()