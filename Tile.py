
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
        # self.label = None           # Tile's value
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
    
    def isOpened(self):
        '''
        Return opened status
        '''
        return self.opened

    def getLabel(self):
        '''
        Get value
        '''
        return self.label
