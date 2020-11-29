# Grid to model the field
from Tile import Tile
from random import randint

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
            if self.inbounds(x+dx, y+dy) and self.grid[x+dx][y+dy].isBomb():
                s += 1
        return s
    
    def printBombs(self):
        '''
        Print bombs in the field
        '''
        for i in range(self.size):
            print("=== ", end='')
        print()
        for i in range(self.size):
            for j in range(self.size):
                if(self.grid[j][i].isBomb()):
                    print(" B  ", end = '')
                else:
                    print("[ ] ", end = '')
            print()
        for i in range(self.size):
            print("=== ", end='')
        print()

    def printField(self):
        '''
        Print the board with all tiles opened
        '''
        for i in range(self.size):
            print("=== ", end='')
        print()
        for y in range(self.size):
            for x in range(self.size):
                currTile = self.grid[x][y]
                if (currTile.isBomb()):
                    print(" B  ", end='')
                else:
                    print("[" + str(self.getLabel(x,y)) + "] ", end='')
            print()
        for i in range(self.size):
            print("=== ", end='')
        print()

    def printBoard(self):
        '''
        Print the board as it is
        '''
        for i in range(self.size):
            print("=== ", end='')
        print()
        for y in range(self.size):
            for x in range(self.size):
                currTile = self.grid[x][y]
                if (currTile.isOpened()):
                    if (currTile.isBomb()):
                        print(" B  ", end='')
                    else:
                        print(" " + self.getLabel(x,y) + "  ", end='')
                elif (currTile.isFlagged()):
                    print("[F] ", end = '')
                else:
                    print("[ ] ", end = '')
            print()
        for i in range(self.size):
            print("=== ", end='')
        print()

    def openTile(self, x, y):
        self.grid[x][y].open()
        self.openAdjacent(x, y)

    def openAdjacent(self, x, y):
        '''
        Open adjacent safe tiles, recursively
        '''
        surr = self.getSurroundings(x, y)
        for ax, ay in surr:
            if self.getLabel(ax,ay) == 0:
                self.openTile(ax, ay)

    def getSurroundings(self, x, y):
        '''
        Get surrounding tiles' ids
        '''
        surr = []
        for (dx, dy) in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]:
            if self.inbounds(x+dx, y+dy):
                surr.append((x + dx, y + dy))
        return surr