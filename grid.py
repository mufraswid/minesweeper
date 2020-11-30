from Tile import Tile
from random import randint

class Grid:
    def __init__(self, size, bombCount):
        '''
        Konstruktor
        '''
        self.size = size
        self.grid = [ [Tile(n + self.size * i) for n in range(size)] for i in range(size)]
        self.bombCount = bombCount
        # List of opened tiles, used for iterate through it to calculate adjacent square probability
        self.openedValuedTiles = []

    def generateRandomBombs(self, count):
        '''
        Generate random bombs on the field
        '''
        for n in range(count):
            while (True):
                x = randint(0, self.size-1)
                y = randint(0, self.size-1)
                if self.grid[x][y].bomb == False and not(x == 0 and (y==0 or y==1)) and not(x==1 and (y==0 or y==1)):
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
                        print(" " + str(self.getLabel(x,y)) + "  ", end='')
                elif (currTile.isFlagged()):
                    print("[F] ", end = '')
                else:
                    print("[ ] ", end = '')
            print()
        for i in range(self.size):
            print("=== ", end='')
        print()

    def openTile(self, x, y):
        if (not(self.grid[x][y].isFlagged()) and not(self.grid[x][y].isOpened())):
            self.grid[x][y].open()
            self.openedValuedTiles.append((x, y))
            if self.getLabel(x, y) == 0:
                self.openAdjacent(x, y)
    
    def isOpenedBomb(self, x, y):
        '''
        Returns true if bomb is opened, expected to end game
        '''
        return (self.grid[x][y].isOpened()) and (self.grid[x][y].isBomb())

    def openAdjacent(self, x, y):
        '''
        Open adjacent safe tiles, recursively
        '''
        surr = self.getSurroundings(x, y)
        for ax, ay in surr:
            if not(self.grid[ax][ay].isOpened()) and not(self.grid[ax][ay].isFlagged()):
                self.openTile(ax, ay)

    def flagTile(self, x, y):
        if (not(self.grid[x][y].isFlagged()) and not(self.grid[x][y].isOpened())):
            self.grid[x][y].setFlag()
    
    def getSurroundings(self, x, y):
        '''
        Get surrounding tiles' ids
        '''
        surr = []
        for (dx, dy) in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]:
            if self.inbounds(x+dx, y+dy):
                surr.append((x + dx, y + dy))
        return surr

    def isWin(self):
        count = 0
        for y in range(self.size):
            for x in range(self.size):
                if (self.grid[x][y].isBomb() and self.grid[x][y].isFlagged()):
                    count+=1
        return (count == self.bombCount)

    def checkBombOpened(self):
        for y in range(self.size):
            for x in range(self.size):
                if (self.isOpenedBomb(x,y)):
                    return True
        return False
            

# def checkOpened()