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