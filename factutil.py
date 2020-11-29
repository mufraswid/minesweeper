# Fact utils
def isFactSquare(str):
    return str[1:7] == 'square'

def isFactFlagged(str):
    return str[1:8] == 'flagged'

def getFlaggedCoord(str):
    '''
    get flagged coord of surrounding, coord is id
    '''
    raw = str[10:]
    id = 0
    # raw is (xx)
    if (len(raw) == 4):
        id = int(raw[1:2])
    # raw is (x)
    else:
        id = int(raw[1])
    return id

def getFlaggedCoord(str, size):
    '''
    get flagged coord of surrounding, coord is (x,y)
    '''
    raw = str[10:]
    id = 0
    # raw is (xx)
    if (len(raw) > 2):
        id = int(raw[1:2])
    # raw is (x)
    else:
        id = int(raw[1])
    return (id % size, id // size)

def isFactOpened(str):
    # return true if fact is opened
    return str[1:7] == 'opened'

def getOpenedCoord(str):
    '''
    get opened coord of surrounding, coord is id
    '''
    raw = str[9:]
    id = 0
    # raw is (xx)
    if (len(raw) > 2):
        id = int(raw[1:2])
    # raw is (x)
    else:
        id = int(raw[2])
    return id

def getOpenedCoord(str, size):
    '''
    get opened coord of surrounding, coord is (x,y)
    '''
    raw = str[9:]
    id = 0
    # raw is (xx)
    if (len(raw) > 2):
        id = int(raw[1:2])
    # raw is (x)
    else:
        id = int(raw[2])
    return (id % size, id // size)

def main():
    string = "(opened (no 0))"
    x, y = getOpenedCoord(string, 4)
    print(x)
    print(y)

if __name__ == "__main__":
    main()