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