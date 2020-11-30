# Fact utils
def isFactSquare(str):
    return str[1:7] == 'square'

def isFactFlagged(str):
    return str[1:8] == 'flagged'

def getFlaggedCoord(str):
    '''
    get flagged coord of surrounding, coord is id
    '''
    raw = str[13:].replace(")","")
    id = int(raw)
    return id


def isFactOpened(str):
    # return true if fact is opened
    return str[1:7] == 'opened'

def getOpenedCoord(str):
    '''
    get opened coord of surrounding, coord is id
    '''
    raw = str[12:].replace(")","")
    id = int(raw)
    return id

def main():
    string = "(flagged (no 10))"
    x, y = getFlaggedCoord(string, 5)
    print(x)
    print(y)

if __name__ == "__main__":
    main()