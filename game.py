"""This module creates a mainwindow to run the application."""
# from os import system
# from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QPushButton, QListWidget, QListWidgetItem, QLineEdit
# from PyQt5.QtGui import QPixmap, QIcon
# from .productwindow import prod_window

from clips import Environment, Symbol
from Tile import Tile
from grid import Grid
from factutil import *

def main():
    '''
    Main function
    '''
    size = 0
    while(True):
        size = int(input("Masukkan ukuran papan (4 <= n <= 10): "))
        if (4 <= size and size <= 10):
            break
        else:
            print("Invalid size!")
    
    bombCount = 0
    while(True):
        bombCount = int(input("Masukkan jumlah bomb dalam papan: "))
        if (1 <= bombCount and bombCount <= (size*size-1)):
            break
        else:
            print("Invalid amount!")
    
    grid = Grid(size)

    while (True):
        case = input("Apakah bomb diinput secara random? (y/n)")
        if (case == "y"):
            grid.generateRandomBombs(bombCount)
            break
        elif (case == "n"):
            grid.inputBombs(bombCount)
            break
    grid.printBombs()
    grid.printField()
    grid.printBoard()

    ### SOLVER PART ###
    # init clps environment, load mines.clp
    env = Environment()
    env.load('mines.clp')
    clips_bomb_count = 0
    print("We begin")
    
    
    
    while clips_bomb_count < bombCount:
        print("Start!")
        for fact in env.facts():
            print(fact)
            strfact = str(fact)
            if isFactSquare(strfact):
                # Retract because the fact is outdated
                fact.retract()
            elif isFactFlagged(strfact):
                # Ensure the flag has never been checked before
                x, y = getFlaggedCoord(strfact, grid.size)
                if not grid.grid[x][y].isFlagged():
                    grid.grid[x][y].setFlag()
                    clips_bomb_count += 1
            elif isFactOpened(strfact):
                x, y = getOpenedCoord(strfact, grid.size)
                if not grid.grid[x][y].isOpened():
                    grid.openTile(x, y)
        
        # Calculate probability to each adjacent unopened tiles
        # Format map = {id: probability}
        adjDict = {}
        for x, y in grid.openedValuedTiles:
            arr = grid.getSurroundings(x, y)
            adj = set([])
            flag = set([])
            # for every unopened adjacent squares, increment probability from every adjacent valued tile
            for ax, ay in arr:
                id = ax + ay * grid.size
                if not grid.grid[ax][ay].isOpened() and not grid.grid[ax][ay].isFlagged():
                    if id not in adjDict:
                        adjDict[id] = 1 
                    else:
                        adjDict[id] += 1
                    adj.add(id)
                elif grid[ax][ay].isFlagged():
                    flag.add(id)
            
            # cek surroundingnya ada yang belom kebuka
            # kalo belom, assert squarenya
            if (len(adj) > 0):
                sqid = x + y * grid.size
                sqqval = grid.getLabel(x,y)
                sqadj = "".join(adj)
                sqflag = len(flag)
                sqstring = "(square (no " + str(sqid) + ") (value " + str(sqval) + ") (adjacent " + str(sqadj) + ") (nflags " + str(sqflag) + "))"
                f = env.assert_string(sqstring)
                f.assertit()

        for key, value in adjDict:
            # assert to clips
            probstring = "(prob (p " + str(value) + ") (id " + str(key) + "))"
            f = env.assert_string(probstring)
            f.assertit()

        for fact in env.facts():
            print(fact)
        break

def init(size):
    ''' 
    Init game aspects
    '''
    size = int(input("Masukkan ukuran papan (4 <= n <= 10): "))
    bombCount = int(input("Masukkan jumlah bomb dalam papan: "))

    grid = Grid(size)

    while (True):
        case = input("Apakah bomb diinput secara random? (y/n)")
        if (case == "y"):
            grid.generateRandomBombs(bombCount)
            break
        elif (case == "n"):
            grid.inputBombs(bombCount)
            break
    grid.print()
    

if __name__ == "__main__":
    main()
