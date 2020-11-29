"""This module creates a mainwindow to run the application."""
# from os import system
# from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QPushButton, QListWidget, QListWidgetItem, QLineEdit
# from PyQt5.QtGui import QPixmap, QIcon
# from .productwindow import prod_window
from clips import Environment, Symbol
from random import randint

### CLASSES ###
# Tile to model each tile in the field
class Tile:
    def __init__(self, id):
        '''
        Constructor
        '''
        self.id = id                # id of the tile
        self.bomb = False           # is a bomb or not
        self.flagged = False        # is flagged or not
        self.label = None           # Tile's value
        self.opened = False         # Status if it is opened or not
    
    def isBomb(self):
        '''
        Returns bomb status
        '''
        return self.bomb

    def isFlagged(self):
        ''' 
        Return flagged status
        '''
        return self.flagged
    
    def setFlag(self):
        ''' 
        Set flag on the tile
        '''
        self.flagged = True
    
    def open(self):
        '''
        Open the tile
        '''
        self.opened = True
    
    def getLabel(self):
        '''
        Get value
        '''
        return self.label

# Grid to model the field
class Grid:
    def __init__(self, size):
        '''
        Konstruktor
        '''
        self.size = size
        self.grid = [ [Tile(n + self.size * i) for n in range(size)] for i in range(size)]

    def generateRandomBombs(self, count):
        '''
        Generate random bombs on the field
        '''
        for n in range(count):
            while (True):
                x = randint(0, self.size-1)
                y = randint(0, self.size-1)
                if x > 0 and y > 0 and self.grid[x][y].bomb == False:
                    self.grid[x][y].bomb = True
                    break

    def inputBombs(self, count):
        '''
        Take input to set the bombs in the field
        '''
        for n in range(count):
            while(True):
                x, y =  map(int, input('Koordinat bomb %d: '%(n+1)).split(','))
                if (x < 0) or (x >= self.size) or (y < 0) or (y >= self.size) or ((x == 0) and (y == 0)):
                    print("Out of bounds!")
                else:
                    if self.grid[x][y].bomb == False and not((x == 0) and (y == 0)):
                        self.grid[x][y].bomb = True
                        break
                    else:
                        print("Koordinat sudah terisi bomb!")

    def inbounds(self, x, y):
        '''
        Check if x and y is within the field
        '''
        return (0 <= x and x < self.size and 0 <= y and y < self.size) 

    def getLabel(self, x, y):
        '''
        Get value of a Tile from its surroundings
        '''
        s = 0
        for (dx, dy) in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]:
            if inbounds(x+dx, y+dy) and grid[x+dx][y+dy].isBomb():
                s += 1
        return s
    
    def printBombs(self):
        '''
        Print bombs in the field
        '''
        for i in range(self.size):
            for j in range(self.size):
                if(self.grid[i][j].isBomb()):
                    print(" B  ", end = '')
                else:
                    print("[ ] ", end = '')
            print()
    
    def openAdjacent(self, id):
        '''
        Open adjacent safe tiles
        '''
        surr = self.getSurroundings(id)
        for tile in surr:
            x, y = tile % 8, tile // 8
            if self.grid[x][y].getLabel() == 0:
                self.grif[x][y].open()
                self.openAdjacent(tile)          
    
    def getSurroundings(self, id):
        '''
        Get surrounding tiles' ids
        '''
        surr = []
        for (dx, dy) in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]:
            if inbounds(x+dx, y+dy):
                nx = x + dx
                ny = y + dy
                surr.append(nx + ny * self.size)
        return surr


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

    ### SOLVER PART ###


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
