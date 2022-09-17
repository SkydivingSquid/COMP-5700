class Cube:
    
    '''
    Rubik's cube
    '''

    def __init__(self, initCube):
        self.cube = initCube


    def isValidLengthCube(cube):
        if (len(cube) == 54):
            return True
        else:
            return False
        
    def isValidCubeChar(cube):
        
        allowed_cubeChar = "wryobg"

        if all(ch in allowed_cubeChar for ch in cube):
            return True
        else:
            return False
        
    def isValidCenterColors(cube):
        
        CenterList = cube[4] + cube[13] +cube[22] + cube[31] + cube[40] + cube[49]
        
        #Checks for duplicates, returns false is duplicate is found.
        for colors in CenterList:
            if CenterList.count(colors) > 1:
                return False
        #Returns True is no duplicates are found.
        return True
        
    def isValidDirChar(dir):
        
        allowed_dirChar = "FfRrBbLlUuDd"

        if all(ch in allowed_dirChar for ch in dir):
            return True
        
        else:
            return False
        
        