# Fact utils
def isFactSquare(str):
    return str[1:7] == 'square'

def isFactFlagged(str):
    return str[:7] == 'flagged'

def getFlaggedCoord(str):
    '''
    get flagged coord of surrounding, coord is id
    '''
    raw = str[13:].replace(")","")
    id = int(raw)
    return id

# def getFlaggedCoord(str, size):
#     '''
#     get flagged coord of surrounding, coord is (x,y)
#     '''
#     raw = str[13:].replace(")","")
#     id = int(raw)
#     return (id % size, id // size)

def isFactOpened(str):
    # return true if fact is opened
    return str[:6] == 'opened'

def getOpenedCoord(str):
    '''
    get opened coord of surrounding, coord is id
    '''
    raw = str[12:].replace(")","")
    id = int(raw)
    return id

# def getOpenedCoord(str, size):
#     '''
#     get opened coord of surrounding, coord is (x,y)
#     '''
#     raw = str[12:].replace(")","")
#     id = int(raw)
#     return (id % size, id // size)

def main():
    string = "(flagged (no 10))"
    x, y = getFlaggedCoord(string, 5)
    print(x)
    print(y)

if __name__ == "__main__":
    main()