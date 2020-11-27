"""This module creates a mainwindow to run the application."""
# from os import system
# from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QPushButton, QListWidget, QListWidgetItem, QLineEdit
# from PyQt5.QtGui import QPixmap, QIcon
# from .productwindow import prod_window
from random import randint

class Tile:
    def __init__(self):
        self.bomb = False
        self.label = None

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [ [Tile() for n in range(size)] for n in range(size)]

    def generateRandomBombs(self, count):
        for n in range(count):
            while (True):
                x = randint(0, self.size-1)
                y = randint(0, self.size-1)
                if self.grid[x][y].bomb == False:
                    self.grid[x][y].bomb = True
                    break

    def inputBombs(self, count):
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
        return (0 <= x and x < self.size and 0 <= y and y < self.size) 

    def getLabel(self, x, y):
        s = 0
        for (dx, dy) in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]:
            if inbounds(x+dx, y+dy) and grid[x+dx][y+dy].bomb:
                s+=1
        return s
    
    def printBombs(self):
        for i in range(self.size):
            for j in range(self.size):
                if(self.grid[i][j].bomb):
                    print(" B  ", end = '')
                else:
                    print("[ ] ", end = '')
            print()

def main():
    size = 0
    while(True):
        size = int(input("Masukkan ukuran papan (4<= n <= 10): "))
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

def init(size):
    size = int(input("Masukkan ukuran papan (4<= n <= 10): "))
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
