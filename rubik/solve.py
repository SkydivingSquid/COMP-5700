import rubik.cube as rubik

"""
###############################################     
############### CUBE CONSTANTS ################
###############################################
"""

#CENTERS
FRONT_CENTER = 4
RIGHT_CENTER = RIGHT_CENTER
BACK_CENTER = BACK_CENTER
LEFT_CENTER = LEFT_CENTER
TOP_CENTER = TOP_CENTER
BOTTOM_CENTER = BOTTOM_CENTER 

#MIDDLES
FRONT_UPPER_MIDDLE = 1
FRONT_LOWER_MIDDLE = 7
RIGHT_UPPER_MIDDLE = RIGHT_UPPER_MIDDLE
RIGHT_LOWER_MIDDLE = RIGHT_LOWER_MIDDLE
BACK_UPPER_MIDDLE = BACK_UPPER_MIDDLE
BACK_LOWER_MIDDLE = BACK_LOWER_MIDDLE
LEFT_UPPER_MIDDLE = LEFT_UPPER_MIDDLE
LEFT_LOWER_MIDDLE = LEFT_LOWER_MIDDLE
TOP_UPPER_MIDDLE = TOP_UPPER_MIDDLE
TOP_LOWER_MIDDLE = TOP_LOWER_MIDDLE
BOTTOM_UPPER_MIDDLE = BOTTOM_UPPER_MIDDLE 
BOTTOM_LOWER_MIDDLE = BOTTOM_LOWER_MIDDLE

#SIDES
FRONT_PORT = 3
FRONT_STRBD = 5
RIGHT_PORT = 12
RIGHT_STBD = 14
BACK_PORT = 21
BACK_STBD = 23
LEFT_PORT = 30
LEFT_STBD = 32
TOP_PORT = 39
TOP_STBD = 41
BOTTOM_PORT = 48
BOTTOM_STBD = 50

#EDGES

FRONT_UPPER_PORT_EDGE = 0
FRONT_UPPER_STBD_EDGE = 2
FRONT_LOWER_PORT_EDGE = 6
FRONT_LOWER_STBD_EDGE = 8

RIGHT_UPPER_PORT_EDGE = 9
RIGHT_UPPER_STBD_EDGE = 11
RIGHT_LOWER_PORT_EDGE = 15
RIGHT_LOWER_STBD_EDGE = 17

BACK_UPPER_PORT_EDGE = 18
BACK_UPPER_STBD_EDGE = 20
BACK_LOWER_PORT_EDGE = 24
BACK_LOWER_STBD_EDGE = 26

LEFT_UPPER_PORT_EDGE = 27
LEFT_UPPER_STBD_EDGE = 29
LEFT_LOWER_PORT_EDGE = 33
LEFT_LOWER_STBD_EDGE = 35

TOP_UPPER_PORT_EDGE = 36
TOP_UPPER_STBD_EDGE = 38
TOP_LOWER_PORT_EDGE = 42
TOP_LOWER_STBD_EDGE = 44

BOTTOM_UPPER_PORT_EDGE = 45
BOTTOM_UPPER_STBD_EDGE = 47
BOTTOM_LOWER_PORT_EDGE = 51
BOTTOM_LOWER_STBD_EDGE = 53


"""
#############################################################        
############### Main Method For Solving Cube ################
#############################################################
"""
def _solve(parms):
    """ Returns the solutions needed to solve a cube and the status of input. """
    result = {}
    solvedBottomCrossResult = {}
    encodedCube = parms.get('cube',None)
    
    #Verify If Input Is Valid and Return Status
    status = _verifyInput(encodedCube)
    
    #Solve for Bottom Cross and set rotations to the solution.
    if status == 'ok':
        solvedBottomCrossResult = _solveBottomCross(encodedCube)
        result['rotations'] = solvedBottomCrossResult.get('solution')
    
    result['status'] = status
    return result

"""
#############################################################        
############## Verify Method For Solving Cube ###############
#############################################################
"""
def _verifyInput(encodedCube):
    """ Verifies Cube Input as Valid (does not current check if 'possible', just valid). """
    result = {}
    result['status'] = 'ok'
    status = result['status']
    
    if encodedCube == None:
        result['status'] = 'error: Missing Cube Argument'
        status = result['status']
        return status 
    
    elif rubik.Cube.isValidLengthCube(encodedCube) == False:
        result['status'] = 'error: Invalid Cube Length'
        status = result['status']
        return status
    
    elif rubik.Cube.isValidCubeChar(encodedCube) == False:
        result['status'] = 'error: Invalid Cube Char'
        status = result['status']
        return status
    
    elif rubik.Cube.isValidCenterColors(encodedCube) == False:
        result['status'] = 'error: Duplicate Center Colors'
        status = result['status']
        return status
        
    elif rubik.Cube.isNineOfEachChar(encodedCube) == False:
        result['status'] = 'error: There May Only Be 9 Of Each Color'
        status = result['status']
        return status    
    
    return status

"""
########################################################       
########### Methods for Solving Bottom Cross ###########
########################################################
"""    
def _solveBottomCross(encodedCube):
    """ First Step in Solving a Cube. Solves for Bottom Cross. """
    result = {}
    cubeList = list(encodedCube)
    rotatedCubeList = cubeList[:]
    result['solution'] = ""
    result['status'] = 'ok'
    
    #Check for bottom cross
    if (_bottomCrossExists(rotatedCubeList)):
        
        #Check for bottom cross alignment
        if (_bottomCrossAligned(rotatedCubeList)):
            result['solution'] = ''
            result['status'] = 'ok'
            return result

        #Rotate unaligned bottom cross into top daisy
        else: 
            encodedCube = _bottomCrossToDaisy(encodedCube, result)
            daisySolution = _daisySolution(encodedCube)
            result['solution'] += daisySolution.get('solution')
            return result
    
    #Check Top for Daisy  
    elif (_daisyExists(rotatedCubeList)):
        daisySolution = _daisySolution(encodedCube)
        result['solution'] += daisySolution.get('solution')
        return result
        
    #If Not a Daisy
    else:
        rotatedCubeList = _notDaisyCase(result, rotatedCubeList)  
      
    #TIME FOR DAISY SOLUTION HERE
    daisySolution = _daisySolution(rotatedCubeList)
    rotatedCubeList = daisySolution.get('cube')
    
    #Set result keys
    _setFinalSolveVariables(result, rotatedCubeList, daisySolution)
    
    return result
    
def _bottomCrossToDaisy(encodedCube, result):
    """ Rotate an unaligned Bottom-Cross into a Daisy """
    
    algorithm = 'FFRRBBLL'
    
    for char in algorithm:
        result['solution'], encodedCube = _functionalRotations(encodedCube, result, char)

    return encodedCube

def _unalignedBottomToDaisy(bottomPetalIndex: int, topPetalIndex: int, solution, rotatedCubeList):
    """ Moves unaligned bottom pieces to top to begin forming a Daisy """
    bottomToDaisyResult = {}
    bottomToDaisyResult['solution'] = solution
    bottomToDaisyResult['rotatedCubeList'] = rotatedCubeList
    
    while rotatedCubeList[bottomPetalIndex] == rotatedCubeList[topPetalIndex]:
        bottomToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, bottomToDaisyResult, 'U')

    if rotatedCubeList[bottomPetalIndex] != rotatedCubeList[topPetalIndex]:
        
        if bottomPetalIndex == BOTTOM_UPPER_MIDDLE:
            letters = 'FF'

        elif bottomPetalIndex == 48:
            letters = 'LL'
            
        elif bottomPetalIndex == 50:
            letters = 'RR'
            
        elif bottomPetalIndex == BOTTOM_LOWER_MIDDLE:
            letters = 'BB'

        for char in letters:
            bottomToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, bottomToDaisyResult, char) 
        
        bottomToDaisyResult['rotatedCubeList'] = rotatedCubeList
    return bottomToDaisyResult

def _horizontalCubesToDaisy(horizontalPetalIndex: int, topPetalIndex: int, solution, rotatedCubeList):
    """ Moves horizontal pieces to top to begin forming a Daisy """
    horizontalToDaisyResult = {}
    horizontalToDaisyResult['solution'] = solution
    horizontalToDaisyResult['rotatedCubeList'] = rotatedCubeList
    
    while rotatedCubeList[horizontalPetalIndex] == rotatedCubeList[topPetalIndex]:
        horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'U')

    if rotatedCubeList[horizontalPetalIndex] != rotatedCubeList[topPetalIndex]:
        
        if horizontalPetalIndex == 3:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'l')
            
        if horizontalPetalIndex == 5:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'R')
            
        if horizontalPetalIndex == 12:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'f')
            
        if horizontalPetalIndex == 14:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'B')
            
        if horizontalPetalIndex == 21:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'r')
            
        if horizontalPetalIndex == 23:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'L')

        if horizontalPetalIndex == 30:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'b')
            
        if horizontalPetalIndex == 32:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'F')
        
        horizontalToDaisyResult['rotatedCubeList'] = rotatedCubeList
    return horizontalToDaisyResult

def _verticalCubesToDaisy(verticalPetalIndex: int, topPetalIndex: int, solution, rotatedCubeList):
    """ Moves vertical pieces to top to begin forming a Daisy """
    veritcalToDaisyResult = {}
    veritcalToDaisyResult['solution'] = solution
    veritcalToDaisyResult['rotatedCubeList'] = rotatedCubeList
    
    while rotatedCubeList[verticalPetalIndex] == rotatedCubeList[topPetalIndex]:
        veritcalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, veritcalToDaisyResult, 'U')

    if rotatedCubeList[verticalPetalIndex] != rotatedCubeList[topPetalIndex]:
        
        if verticalPetalIndex == 1:
            rotatedCubeList, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(rotatedCubeList, veritcalToDaisyResult, "lfLDFF")
        
        if verticalPetalIndex == 7:
            rotatedCubeList, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(rotatedCubeList, veritcalToDaisyResult, "FFlfLDFF")
    
        if verticalPetalIndex == RIGHT_UPPER_MIDDLE:
            rotatedCubeList, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(rotatedCubeList, veritcalToDaisyResult, "frFDRR")
    
        if verticalPetalIndex == RIGHT_LOWER_MIDDLE:
            rotatedCubeList, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(rotatedCubeList, veritcalToDaisyResult, "RRfrFDRR")

        if verticalPetalIndex == BACK_UPPER_MIDDLE:
            rotatedCubeList, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(rotatedCubeList, veritcalToDaisyResult, "rbRDBB")
        
        if verticalPetalIndex == BACK_LOWER_MIDDLE:
            rotatedCubeList, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(rotatedCubeList, veritcalToDaisyResult, "BBrbRDBB")
            
        if verticalPetalIndex == LEFT_UPPER_MIDDLE: 
            rotatedCubeList, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(rotatedCubeList, veritcalToDaisyResult, "blBDLL")
            
        if verticalPetalIndex == LEFT_LOWER_MIDDLE:
            rotatedCubeList, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(rotatedCubeList, veritcalToDaisyResult, "LLblBDLL")
        
        veritcalToDaisyResult['rotatedCubeList'] = rotatedCubeList
    return veritcalToDaisyResult

def _setFinalSolveVariables(result, rotatedCubeList, daisySolution):
    result['cube'] = "".join(rotatedCubeList)
    result['solution'] += daisySolution.get('solution')
    result['status'] = 'ok'

"""  
########################################################       
############## Methods for Solving Daisy ###############
########################################################
""" 
def _daisyVariableUpdate(encodedCube, result, daisyResult):
    """ Sets variables post daisyIntegrated. Forgot to refactor this into it originally. """
    result['solution'] = daisyResult.get('solution')
    encodedCube = daisyResult.get('daisyCubeList')
    rotatedCubeList = encodedCube
    return rotatedCubeList, encodedCube

def _daisySolution(encodedCube):
    """ When a daisy is made, align colors and rotate into Bottom Cross solution. """
    result = {}
    daisyResult = {}
    cubeList = list(encodedCube)
    rotatedCubeList = cubeList[:]
    result['solution'] = ""
    
    #Front Face 
    if not (rotatedCubeList[4] == rotatedCubeList[7] and rotatedCubeList[BOTTOM_CENTER] == rotatedCubeList[BOTTOM_UPPER_MIDDLE]):
        
        daisyResult = _daisyIntegrated(4, 1, TOP_LOWER_MIDDLE, encodedCube, result['solution'])
        rotatedCubeList, encodedCube = _daisyVariableUpdate(encodedCube, result, daisyResult)
        
    #Right Face 
    if not (rotatedCubeList[RIGHT_CENTER] == rotatedCubeList[RIGHT_LOWER_MIDDLE] and rotatedCubeList[BOTTOM_CENTER] == rotatedCubeList[50]):
        
        daisyResult = _daisyIntegrated(RIGHT_CENTER, RIGHT_UPPER_MIDDLE, 41, encodedCube, result['solution'])
        rotatedCubeList, encodedCube = _daisyVariableUpdate(encodedCube, result, daisyResult)
        
    # #Back Face 
    if not (rotatedCubeList[BACK_CENTER] == rotatedCubeList[BACK_LOWER_MIDDLE] and rotatedCubeList[BOTTOM_CENTER] == rotatedCubeList[BOTTOM_LOWER_MIDDLE]):
        
        daisyResult = _daisyIntegrated(BACK_CENTER, BACK_UPPER_MIDDLE, TOP_UPPER_MIDDLE, encodedCube, result['solution'])
        rotatedCubeList, encodedCube = _daisyVariableUpdate(encodedCube, result, daisyResult)

    # #Left Face 
    if not (rotatedCubeList[LEFT_CENTER] == rotatedCubeList[LEFT_LOWER_MIDDLE] and rotatedCubeList[BOTTOM_CENTER] == rotatedCubeList[48]):
        
        daisyResult = _daisyIntegrated(LEFT_CENTER, LEFT_UPPER_MIDDLE, 39, encodedCube, result['solution'])
        rotatedCubeList, encodedCube = _daisyVariableUpdate(encodedCube, result, daisyResult)
            
    result['cube'] = encodedCube
    return result

def _BrokenAndConfusedU(encodedCube, daisyResult):
    """ A unique method to rotate U in daisy. Not sure why it doesn't need to return daisyResult['solution'] """
    U_result = _rotateU(encodedCube)
    daisyResult['solution'] += U_result.get('letter')
    encodedCube = U_result.get('cube')
    return encodedCube

def _daisyURotations(uniqueCenter: int, topMiddle: int, adjacentDaisy: int, encodedCube, solution): 
    """ Sub-method for Integrated Daisy Method. Rotates U until alignment found. """
    daisyResult = {}
    cubeList = list(encodedCube)
    rotatedCubeList = cubeList[:]
    daisyResult['solution'] = solution
    daisyResult['daisyCubeList'] = encodedCube
    
    while (rotatedCubeList[uniqueCenter]!= rotatedCubeList[topMiddle] or rotatedCubeList[adjacentDaisy] != rotatedCubeList[BOTTOM_CENTER]):
        
        encodedCube = _BrokenAndConfusedU(encodedCube, daisyResult)
        rotatedCubeList = encodedCube
        
    daisyResult['daisyCubeList'] = encodedCube
    return daisyResult
  
def _daisy_Rotations(uniqueCenter: int, topMiddle: int, encodedCube, solution):
    """ Sub-method for Integrated Daisy Method. Rotates the block a specific direction depending on its uniqueCenter. """
    daisyRotResult = {}
    cubeList = list(encodedCube)
    rotatedCubeList = cubeList[:]
    daisyRotResult['solution'] = solution
    daisyRotResult['daisyCubeList'] = encodedCube
    irrelevantVar = None
    
    if rotatedCubeList[uniqueCenter] == rotatedCubeList[topMiddle]:
        if uniqueCenter == 4:
            letters = 'FF'
            
        if uniqueCenter == RIGHT_CENTER:
            letters = 'RR'
            
        if uniqueCenter == BACK_CENTER:
            letters = 'BB'
            
        if uniqueCenter == LEFT_CENTER:
            letters = 'LL'
            
        for char in letters:
            irrelevantVar, encodedCube = _functionalRotations(encodedCube, daisyRotResult, char)
            
        rotatedCubeList = encodedCube
        
    daisyRotResult['daisyCubeList'] = encodedCube

    return daisyRotResult

def _daisyIntegrated(uniqueCenter: int, topMiddle: int, adjacentDaisy: int, encodedCube, solution):
    """ Rotation method for _DaisySolution. This rotates U when not aligned and the top to bottom when aligned. """
    integratedResult = {}

    #Rotate U if applicable
    innerMethodResult = _daisyURotations(uniqueCenter, topMiddle, adjacentDaisy, encodedCube, solution)
    
    #Rotate top to bottom
    innerMethodResult = _daisy_Rotations(uniqueCenter, topMiddle, innerMethodResult.get('daisyCubeList'), innerMethodResult.get('solution'))
    
    integratedResult['daisyCubeList'] = innerMethodResult.get('daisyCubeList')
    integratedResult['solution'] = innerMethodResult.get('solution')

    return integratedResult

"""
####################################################################################        
############ Rotation Functions and Updates to Cube and Solution String ############
#################################################################################### 
"""

def _functionalRotations(encodedCube, result, letter):
    rotationDirection = None
    
    if letter == 'F':
        rotationDirection = _rotateF(encodedCube)
    elif letter == 'f':
        rotationDirection = _rotatef(encodedCube)
    elif letter == 'R':
        rotationDirection = _rotateR(encodedCube)
    elif letter == 'r':
        rotationDirection = _rotater(encodedCube)
    elif letter == 'B':
        rotationDirection = _rotateB(encodedCube)
    elif letter == 'b':
        rotationDirection = _rotateb(encodedCube)
    elif letter == 'L':
        rotationDirection = _rotateL(encodedCube)
    elif letter == 'l':
        rotationDirection = _rotatel(encodedCube)
    elif letter == 'U':
        rotationDirection = _rotateU(encodedCube)
    elif letter == 'u':
        rotationDirection = _rotateu(encodedCube)
    elif letter == 'D':
        rotationDirection = _rotateD(encodedCube)
    elif letter == 'd':
        rotationDirection = _rotated(encodedCube)
        
    Direct_result = rotationDirection
    result['solution'] += Direct_result.get('letter')
    encodedCube = Direct_result.get('cube')
    
    return result['solution'], encodedCube
    

"""
#############################################################        
############ Rotating Vertical Cubes into Daisy #############
#############################################################
"""
def _verticalCubeIntoDaisy(rotatedCubeList, veritcalToDaisyResult, algorithm):
    
    for char in algorithm:
        veritcalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, veritcalToDaisyResult, char)
    
    return rotatedCubeList, veritcalToDaisyResult['solution']
    
"""
#############################################################        
########### Bottom-Cross Methods For Solving Cube ###########
#############################################################
"""

""" Bottom Moves """
def _moveBottomCubesToDaisy(result, rotatedCubeList, numberOfPetalsFound):
#Checking Top of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveBottomTopCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Checking Left of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveBottomRightCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Checking Right of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveBottomBackCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Checking Bottom of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveBottomLeftCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)

    return numberOfPetalsFound, rotatedCubeList

def _moveBottomTopCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[BOTTOM_UPPER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER]:
        bottomToDaisyResult = _unalignedBottomToDaisy(BOTTOM_UPPER_MIDDLE, TOP_LOWER_MIDDLE, result['solution'], rotatedCubeList)
        result['solution'] = bottomToDaisyResult.get('solution')
        rotatedCubeList = bottomToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveBottomRightCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[48] == rotatedCubeList[BOTTOM_CENTER]:
        bottomToDaisyResult = _unalignedBottomToDaisy(48, 39, result['solution'], rotatedCubeList)
        result['solution'] = bottomToDaisyResult.get('solution')
        rotatedCubeList = bottomToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveBottomBackCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[50] == rotatedCubeList[BOTTOM_CENTER]:
        bottomToDaisyResult = _unalignedBottomToDaisy(50, 41, result['solution'], rotatedCubeList)
        result['solution'] = bottomToDaisyResult.get('solution')
        rotatedCubeList = bottomToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveBottomLeftCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[BOTTOM_LOWER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER]:
        bottomToDaisyResult = _unalignedBottomToDaisy(BOTTOM_LOWER_MIDDLE, TOP_UPPER_MIDDLE, result['solution'], rotatedCubeList)
        result['solution'] = bottomToDaisyResult.get('solution')
        rotatedCubeList = bottomToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

""" Horizontal Moves """
def _moveHorizontalCubesToDaisy(result, rotatedCubeList, numberOfPetalsFound):
#Check Front Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveFrontPortCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Check Front Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveFrontStarboardCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Check Right Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveRightPortCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Check Right Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveRightStarboardCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Check Back Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveBackPortCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Check Back Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveBackStarboardCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Check Left Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveLeftPortCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Check Left Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveLeftStarboardCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
  
    return numberOfPetalsFound, rotatedCubeList

def _moveFrontPortCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[3] == rotatedCubeList[BOTTOM_CENTER]:
        horizontalToDaisyResult = _horizontalCubesToDaisy(3, 39, result['solution'], rotatedCubeList)
        result['solution'] = horizontalToDaisyResult.get('solution')
        rotatedCubeList = horizontalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveFrontStarboardCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[5] == rotatedCubeList[BOTTOM_CENTER]:
        horizontalToDaisyResult = _horizontalCubesToDaisy(5, 41, result['solution'], rotatedCubeList)
        result['solution'] = horizontalToDaisyResult.get('solution')
        rotatedCubeList = horizontalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveRightPortCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[12] == rotatedCubeList[BOTTOM_CENTER]:
        horizontalToDaisyResult = _horizontalCubesToDaisy(12, TOP_LOWER_MIDDLE, result['solution'], rotatedCubeList)
        result['solution'] = horizontalToDaisyResult.get('solution')
        rotatedCubeList = horizontalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveRightStarboardCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[14] == rotatedCubeList[BOTTOM_CENTER]:
        horizontalToDaisyResult = _horizontalCubesToDaisy(14, TOP_UPPER_MIDDLE, result['solution'], rotatedCubeList)
        result['solution'] = horizontalToDaisyResult.get('solution')
        rotatedCubeList = horizontalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveBackPortCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[21] == rotatedCubeList[BOTTOM_CENTER]:
        horizontalToDaisyResult = _horizontalCubesToDaisy(21, 41, result['solution'], rotatedCubeList)
        result['solution'] = horizontalToDaisyResult.get('solution')
        rotatedCubeList = horizontalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveBackStarboardCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[23] == rotatedCubeList[BOTTOM_CENTER]:
        horizontalToDaisyResult = _horizontalCubesToDaisy(23, 39, result['solution'], rotatedCubeList)
        result['solution'] = horizontalToDaisyResult.get('solution')
        rotatedCubeList = horizontalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveLeftPortCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[30] == rotatedCubeList[BOTTOM_CENTER]:
        horizontalToDaisyResult = _horizontalCubesToDaisy(30, TOP_UPPER_MIDDLE, result['solution'], rotatedCubeList)
        result['solution'] = horizontalToDaisyResult.get('solution')
        rotatedCubeList = horizontalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveLeftStarboardCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[32] == rotatedCubeList[BOTTOM_CENTER]:
        horizontalToDaisyResult = _horizontalCubesToDaisy(32, TOP_LOWER_MIDDLE, result['solution'], rotatedCubeList)
        result['solution'] = horizontalToDaisyResult.get('solution')
        rotatedCubeList = horizontalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

""" Vertical Moves """
def _moveVerticalCubesToDaisy(result, rotatedCubeList, numberOfPetalsFound):
#Front Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveFrontUpperVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Front Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveFrontLowerVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Right Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveRightUpperVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Right Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveRightLowerVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
# Back Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveBackUpperVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
# Back Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveBackLowerVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Left Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveLeftUpperVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Left Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveLeftLowerVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
        
    return numberOfPetalsFound, rotatedCubeList

def _moveFrontUpperVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[1] == rotatedCubeList[BOTTOM_CENTER]:
        verticalToDaisyResult = _verticalCubesToDaisy(1, TOP_LOWER_MIDDLE, result['solution'], rotatedCubeList)
        result['solution'] = verticalToDaisyResult.get('solution')
        rotatedCubeList = verticalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveFrontLowerVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[7] == rotatedCubeList[BOTTOM_CENTER]:
        verticalToDaisyResult = _verticalCubesToDaisy(7, TOP_LOWER_MIDDLE, result['solution'], rotatedCubeList)
        result['solution'] = verticalToDaisyResult.get('solution')
        rotatedCubeList = verticalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveRightUpperVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[RIGHT_UPPER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER]:
        verticalToDaisyResult = _verticalCubesToDaisy(RIGHT_UPPER_MIDDLE, 41, result['solution'], rotatedCubeList)
        result['solution'] = verticalToDaisyResult.get('solution')
        rotatedCubeList = verticalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveRightLowerVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[RIGHT_LOWER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER]:
        verticalToDaisyResult = _verticalCubesToDaisy(RIGHT_LOWER_MIDDLE, 41, result['solution'], rotatedCubeList)
        result['solution'] = verticalToDaisyResult.get('solution')
        rotatedCubeList = verticalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveBackUpperVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[BACK_UPPER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER]:
        verticalToDaisyResult = _verticalCubesToDaisy(BACK_UPPER_MIDDLE, TOP_UPPER_MIDDLE, result['solution'], rotatedCubeList)
        result['solution'] = verticalToDaisyResult.get('solution')
        rotatedCubeList = verticalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveBackLowerVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[BACK_LOWER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER]:
        verticalToDaisyResult = _verticalCubesToDaisy(BACK_LOWER_MIDDLE, TOP_UPPER_MIDDLE, result['solution'], rotatedCubeList)
        result['solution'] = verticalToDaisyResult.get('solution')
        rotatedCubeList = verticalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveLeftUpperVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[LEFT_UPPER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER]:
        verticalToDaisyResult = _verticalCubesToDaisy(LEFT_UPPER_MIDDLE, 39, result['solution'], rotatedCubeList)
        result['solution'] = verticalToDaisyResult.get('solution')
        rotatedCubeList = verticalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

def _moveLeftLowerVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound):
    if rotatedCubeList[LEFT_LOWER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER]:
        verticalToDaisyResult = _verticalCubesToDaisy(LEFT_LOWER_MIDDLE, 39, result['solution'], rotatedCubeList)
        result['solution'] = verticalToDaisyResult.get('solution')
        rotatedCubeList = verticalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

"""
###############################################################        
########### Bottom Cross / Daisy Orientation Checks ###########
###############################################################
"""
def _countTopPetals(rotatedCubeList):
    numberOfPetalsFound = 0
    if rotatedCubeList[TOP_UPPER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER]:
        numberOfPetalsFound += 1
    if rotatedCubeList[39] == rotatedCubeList[BOTTOM_CENTER]:
        numberOfPetalsFound += 1
    if rotatedCubeList[41] == rotatedCubeList[BOTTOM_CENTER]:
        numberOfPetalsFound += 1
    if rotatedCubeList[TOP_LOWER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER]:
        numberOfPetalsFound += 1
    return numberOfPetalsFound

def _notDaisyCase(result, rotatedCubeList):
    #Count Number of Top Petals
    numberOfPetalsFound = _countTopPetals(rotatedCubeList)
    while numberOfPetalsFound <= 3:
        #Bottom Cubes To Daisy
        numberOfPetalsFound, rotatedCubeList = _moveBottomCubesToDaisy(result, rotatedCubeList, numberOfPetalsFound)
        #Horizontal Cubes To Daisy
        numberOfPetalsFound, rotatedCubeList = _moveHorizontalCubesToDaisy(result, rotatedCubeList, numberOfPetalsFound)
        #Vertical Cubes To Daisy
        numberOfPetalsFound, rotatedCubeList = _moveVerticalCubesToDaisy(result, rotatedCubeList, numberOfPetalsFound)
    
    return rotatedCubeList

def _bottomCrossExists(rotatedCubeList):
    return (rotatedCubeList[BOTTOM_UPPER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER] 
            and rotatedCubeList[48] == rotatedCubeList[BOTTOM_CENTER] 
            and rotatedCubeList[50] == rotatedCubeList[BOTTOM_CENTER] 
            and rotatedCubeList[BOTTOM_LOWER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER])
    
def _bottomCrossAligned(rotatedCubeList):
    return (rotatedCubeList[4] == rotatedCubeList[7] 
            and rotatedCubeList[RIGHT_CENTER] == rotatedCubeList[RIGHT_LOWER_MIDDLE] 
            and rotatedCubeList[BACK_CENTER] == rotatedCubeList[BACK_LOWER_MIDDLE] 
            and rotatedCubeList[LEFT_CENTER] == rotatedCubeList[LEFT_LOWER_MIDDLE])
    
def _daisyExists(rotatedCubeList):
    return (rotatedCubeList[TOP_UPPER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER] 
            and rotatedCubeList[39] == rotatedCubeList[BOTTOM_CENTER] 
            and rotatedCubeList[41] == rotatedCubeList[BOTTOM_CENTER] 
            and rotatedCubeList[TOP_LOWER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER])

"""
#############################################################        
############## Rotate Methods For Solving Cube ##############
##############   These are my 'magic numbers'  ##############
#############################################################
"""
def _rotateF(cube):
    result = {}
    
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
        #rotate front face
    rotatedCubeList[2] = cubeList[0]
    rotatedCubeList[5] = cubeList[1]
    rotatedCubeList[8] = cubeList[2]
    rotatedCubeList[1] = cubeList[3]
    rotatedCubeList[4] = cubeList[4]
    rotatedCubeList[7] = cubeList[5]
    rotatedCubeList[0] = cubeList[6]
    rotatedCubeList[3] = cubeList[7]
    rotatedCubeList[6] = cubeList[8]
    
    #rotate top to right
    rotatedCubeList[9] = cubeList[TOP_CENTER]
    rotatedCubeList[12] = cubeList[TOP_LOWER_MIDDLE]
    rotatedCubeList[15] = cubeList[44]
    
    #rotate right to bottom
    rotatedCubeList[47] = cubeList[9]
    rotatedCubeList[BOTTOM_UPPER_MIDDLE] = cubeList[12]
    rotatedCubeList[45] = cubeList[15]
    
    #rotate bottom to left
    rotatedCubeList[29] = cubeList[45]
    rotatedCubeList[32] = cubeList[BOTTOM_UPPER_MIDDLE]
    rotatedCubeList[35] = cubeList[47]
    
    #rotate left to top
    rotatedCubeList[44] = cubeList[29]
    rotatedCubeList[TOP_LOWER_MIDDLE] = cubeList[32] 
    rotatedCubeList[TOP_CENTER] = cubeList[35]
    
    result['cube'] = rotatedCubeList
    result['letter'] = 'F'
    return result


#Rotate front face counter-clockwise (f)
def _rotatef(cube):
    result = {}
    
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate front face
    rotatedCubeList[0] = cubeList[2]
    rotatedCubeList[1] = cubeList[5]
    rotatedCubeList[2] = cubeList[8]
    rotatedCubeList[3] = cubeList[1]
    rotatedCubeList[4] = cubeList[4]
    rotatedCubeList[5] = cubeList[7]
    rotatedCubeList[6] = cubeList[0]
    rotatedCubeList[7] = cubeList[3]
    rotatedCubeList[8] = cubeList[6]
    
    #rotate right to top
    rotatedCubeList[TOP_CENTER] = cubeList[9]
    rotatedCubeList[TOP_LOWER_MIDDLE] = cubeList[12]
    rotatedCubeList[44] = cubeList[15]
    
    #rotate bottom to right
    rotatedCubeList[9] = cubeList[47]
    rotatedCubeList[12] = cubeList[BOTTOM_UPPER_MIDDLE]
    rotatedCubeList[15] = cubeList[45]
    
    #rotate left to bottom
    rotatedCubeList[45] = cubeList[29]
    rotatedCubeList[BOTTOM_UPPER_MIDDLE] = cubeList[32]
    rotatedCubeList[47] = cubeList[35]
    
    #rotate top to left
    rotatedCubeList[29] = cubeList[44]
    rotatedCubeList[32] = cubeList[TOP_LOWER_MIDDLE] 
    rotatedCubeList[35] = cubeList[TOP_CENTER]
    
    result['cube'] = rotatedCubeList
    result['letter'] = 'f'
    return result

#Rotate right face clockwise (R)
def _rotateR(cube):
    result = {}
    
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate front face
    rotatedCubeList[11] = cubeList[9]
    rotatedCubeList[14] = cubeList[RIGHT_UPPER_MIDDLE]
    rotatedCubeList[17] = cubeList[11]
    rotatedCubeList[RIGHT_UPPER_MIDDLE] = cubeList[12]
    rotatedCubeList[RIGHT_CENTER] = cubeList[RIGHT_CENTER]
    rotatedCubeList[RIGHT_LOWER_MIDDLE] = cubeList[14]
    rotatedCubeList[9] = cubeList[15]
    rotatedCubeList[12] = cubeList[RIGHT_LOWER_MIDDLE]
    rotatedCubeList[15] = cubeList[17]
    
    #rotate top to right
    rotatedCubeList[18] = cubeList[44]
    rotatedCubeList[21] = cubeList[41]
    rotatedCubeList[24] = cubeList[38]
    
    #rotate right to bottom
    rotatedCubeList[53] = cubeList[18]
    rotatedCubeList[50] = cubeList[21]
    rotatedCubeList[47] = cubeList[24]
    
    #rotate bottom to left
    rotatedCubeList[2] = cubeList[47]
    rotatedCubeList[5] = cubeList[50]
    rotatedCubeList[8] = cubeList[53]
    
    #rotate left to top
    rotatedCubeList[38] = cubeList[2]
    rotatedCubeList[41] = cubeList[5] 
    rotatedCubeList[44] = cubeList[8]
    
    result['cube'] = rotatedCubeList
    result['letter'] = 'R'
    return result

#Rotate right face counter-clockwise (r)
def _rotater(cube):
    result = {}
    
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate front face
    rotatedCubeList[9] = cubeList[11]
    rotatedCubeList[RIGHT_UPPER_MIDDLE] = cubeList[14]
    rotatedCubeList[11] = cubeList[17]
    rotatedCubeList[12] = cubeList[RIGHT_UPPER_MIDDLE]
    rotatedCubeList[RIGHT_CENTER] = cubeList[RIGHT_CENTER]
    rotatedCubeList[14] = cubeList[RIGHT_LOWER_MIDDLE]
    rotatedCubeList[15] = cubeList[9]
    rotatedCubeList[RIGHT_LOWER_MIDDLE] = cubeList[12]
    rotatedCubeList[17] = cubeList[15]
    
    #rotate top to right
    rotatedCubeList[44] = cubeList[18]
    rotatedCubeList[41] = cubeList[21]
    rotatedCubeList[38] = cubeList[24]
    
    #rotate right to bottom
    rotatedCubeList[18] = cubeList[53]
    rotatedCubeList[21] = cubeList[50]
    rotatedCubeList[24] = cubeList[47]
    
    #rotate bottom to left
    rotatedCubeList[47] = cubeList[2]
    rotatedCubeList[50] = cubeList[5]
    rotatedCubeList[53] = cubeList[8]
    
    #rotate left to top
    rotatedCubeList[2] = cubeList[38]
    rotatedCubeList[5] = cubeList[41] 
    rotatedCubeList[8] = cubeList[44]
    
    result['cube'] = rotatedCubeList
    result['letter'] = 'r'
    return result

#Rotate Back face clockwise (B)
def _rotateB(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[20] = cubeList[18]
    rotatedCubeList[23] = cubeList[BACK_UPPER_MIDDLE]
    rotatedCubeList[26] = cubeList[20]
    rotatedCubeList[BACK_UPPER_MIDDLE] = cubeList[21]
    rotatedCubeList[BACK_CENTER] = cubeList[BACK_CENTER]
    rotatedCubeList[BACK_LOWER_MIDDLE] = cubeList[23]
    rotatedCubeList[18] = cubeList[24]
    rotatedCubeList[21] = cubeList[BACK_LOWER_MIDDLE]
    rotatedCubeList[24] = cubeList[26]

    #rotate top to right
    rotatedCubeList[27] = cubeList[38]
    rotatedCubeList[30] = cubeList[TOP_UPPER_MIDDLE]
    rotatedCubeList[33] = cubeList[36]

    #rotate right to bottom
    rotatedCubeList[51] = cubeList[27]
    rotatedCubeList[BOTTOM_LOWER_MIDDLE] = cubeList[30]
    rotatedCubeList[53] = cubeList[33]

    #rotate bottom to left
    rotatedCubeList[17] = cubeList[51]
    rotatedCubeList[14] = cubeList[BOTTOM_LOWER_MIDDLE]
    rotatedCubeList[11] = cubeList[53]

    #rotate left to top
    rotatedCubeList[36] = cubeList[11]
    rotatedCubeList[TOP_UPPER_MIDDLE] = cubeList[14] 
    rotatedCubeList[38] = cubeList[17]
#
    result['cube'] = rotatedCubeList
    result['letter'] = 'B'
    return result

#Rotate Back face counter-clockwise (b)
def _rotateb(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[18] = cubeList[20]
    rotatedCubeList[BACK_UPPER_MIDDLE] = cubeList[23]
    rotatedCubeList[20] = cubeList[26]
    rotatedCubeList[21] = cubeList[BACK_UPPER_MIDDLE]
    rotatedCubeList[BACK_CENTER] = cubeList[BACK_CENTER]
    rotatedCubeList[23] = cubeList[BACK_LOWER_MIDDLE]
    rotatedCubeList[24] = cubeList[18]
    rotatedCubeList[BACK_LOWER_MIDDLE] = cubeList[21]
    rotatedCubeList[26] = cubeList[24]

    #rotate top to right
    rotatedCubeList[38] = cubeList[27]
    rotatedCubeList[TOP_UPPER_MIDDLE] = cubeList[30]
    rotatedCubeList[36] = cubeList[33]

    #rotate right to bottom
    rotatedCubeList[27] = cubeList[51]
    rotatedCubeList[30] = cubeList[BOTTOM_LOWER_MIDDLE]
    rotatedCubeList[33] = cubeList[53]

    #rotate bottom to left
    rotatedCubeList[51] = cubeList[17]
    rotatedCubeList[BOTTOM_LOWER_MIDDLE] = cubeList[14]
    rotatedCubeList[53] = cubeList[11]

    #rotate left to top
    rotatedCubeList[11] = cubeList[36]
    rotatedCubeList[14] = cubeList[TOP_UPPER_MIDDLE] 
    rotatedCubeList[17] = cubeList[38]
#
    result['cube'] = rotatedCubeList
    result['letter'] = 'b'
    return result

#Rotate Left face clockwise (L)
def _rotateL(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[29] = cubeList[27]
    rotatedCubeList[32] = cubeList[LEFT_UPPER_MIDDLE]
    rotatedCubeList[35] = cubeList[29]
    rotatedCubeList[LEFT_UPPER_MIDDLE] = cubeList[30]
    rotatedCubeList[LEFT_CENTER] = cubeList[LEFT_CENTER]
    rotatedCubeList[LEFT_LOWER_MIDDLE] = cubeList[32]
    rotatedCubeList[27] = cubeList[33]
    rotatedCubeList[30] = cubeList[LEFT_LOWER_MIDDLE]
    rotatedCubeList[33] = cubeList[35]

    #rotate top to right
    rotatedCubeList[0] = cubeList[36]
    rotatedCubeList[3] = cubeList[39]
    rotatedCubeList[6] = cubeList[TOP_CENTER]

    #rotate right to bottom
    rotatedCubeList[45] = cubeList[0]
    rotatedCubeList[48] = cubeList[3]
    rotatedCubeList[51] = cubeList[6]

    #rotate bottom to left
    rotatedCubeList[26] = cubeList[45]
    rotatedCubeList[23] = cubeList[48]
    rotatedCubeList[20] = cubeList[51]

    #rotate left to top
    rotatedCubeList[TOP_CENTER] = cubeList[20]
    rotatedCubeList[39] = cubeList[23] 
    rotatedCubeList[36] = cubeList[26]

    result['cube'] = rotatedCubeList
    result['letter'] = 'L'
    return result

#Rotate Left face clockwise (l)
def _rotatel(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[27] = cubeList[29]
    rotatedCubeList[LEFT_UPPER_MIDDLE] = cubeList[32]
    rotatedCubeList[29] = cubeList[35]
    rotatedCubeList[30] = cubeList[LEFT_UPPER_MIDDLE]
    rotatedCubeList[LEFT_CENTER] = cubeList[LEFT_CENTER]
    rotatedCubeList[32] = cubeList[LEFT_LOWER_MIDDLE]
    rotatedCubeList[33] = cubeList[27]
    rotatedCubeList[LEFT_LOWER_MIDDLE] = cubeList[30]
    rotatedCubeList[35] = cubeList[33]
    
    #rotate top to right
    rotatedCubeList[36] = cubeList[0]
    rotatedCubeList[39] = cubeList[3]
    rotatedCubeList[TOP_CENTER] = cubeList[6]
    
    #rotate right to bottom
    rotatedCubeList[0] = cubeList[45]
    rotatedCubeList[3] = cubeList[48]
    rotatedCubeList[6] = cubeList[51]
    
    #rotate bottom to left
    rotatedCubeList[51] = cubeList[20]
    rotatedCubeList[48] = cubeList[23]
    rotatedCubeList[45] = cubeList[26]
    
    #rotate left to top
    rotatedCubeList[20] = cubeList[TOP_CENTER]
    rotatedCubeList[23] = cubeList[39] 
    rotatedCubeList[26] = cubeList[36]

    result['cube'] = rotatedCubeList
    result['letter'] = 'l'
    return result

#Rotate top (Upper) face clockwise (U)
def _rotateU(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[38] = cubeList[36]
    rotatedCubeList[41] = cubeList[TOP_UPPER_MIDDLE]
    rotatedCubeList[44] = cubeList[38]
    rotatedCubeList[TOP_UPPER_MIDDLE] = cubeList[39]
    rotatedCubeList[TOP_CENTER] = cubeList[TOP_CENTER]
    rotatedCubeList[TOP_LOWER_MIDDLE] = cubeList[41]
    rotatedCubeList[36] = cubeList[TOP_CENTER]
    rotatedCubeList[39] = cubeList[TOP_LOWER_MIDDLE]
    rotatedCubeList[TOP_CENTER] = cubeList[44]
    
    #rotate top to right
    rotatedCubeList[9] = cubeList[18]
    rotatedCubeList[RIGHT_UPPER_MIDDLE] = cubeList[BACK_UPPER_MIDDLE]
    rotatedCubeList[11] = cubeList[20]
    
    #rotate right to bottom
    rotatedCubeList[0] = cubeList[9]
    rotatedCubeList[1] = cubeList[RIGHT_UPPER_MIDDLE]
    rotatedCubeList[2] = cubeList[11]
    
    #rotate bottom to left
    rotatedCubeList[27] = cubeList[0]
    rotatedCubeList[LEFT_UPPER_MIDDLE] = cubeList[1]
    rotatedCubeList[29] = cubeList[2]
    
    #rotate left to top
    rotatedCubeList[18] = cubeList[27]
    rotatedCubeList[BACK_UPPER_MIDDLE] = cubeList[LEFT_UPPER_MIDDLE] 
    rotatedCubeList[20] = cubeList[29]

    result['cube'] = rotatedCubeList
    result['letter'] = 'U'
    return result

#Rotate top (Upper) face counter-clockwise (u)
def _rotateu(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[36] = cubeList[38]
    rotatedCubeList[TOP_UPPER_MIDDLE] = cubeList[41]
    rotatedCubeList[38] = cubeList[44]
    rotatedCubeList[39] = cubeList[TOP_UPPER_MIDDLE]
    rotatedCubeList[TOP_CENTER] = cubeList[TOP_CENTER]
    rotatedCubeList[41] = cubeList[TOP_LOWER_MIDDLE]
    rotatedCubeList[TOP_CENTER] = cubeList[36]
    rotatedCubeList[TOP_LOWER_MIDDLE] = cubeList[39]
    rotatedCubeList[44] = cubeList[TOP_CENTER]
    
    #rotate top to right
    rotatedCubeList[18] = cubeList[9]
    rotatedCubeList[BACK_UPPER_MIDDLE] = cubeList[RIGHT_UPPER_MIDDLE]
    rotatedCubeList[20] = cubeList[11]
    
    #rotate right to bottom
    rotatedCubeList[9] = cubeList[0]
    rotatedCubeList[RIGHT_UPPER_MIDDLE] = cubeList[1]
    rotatedCubeList[11] = cubeList[2]
    
    #rotate bottom to left
    rotatedCubeList[0] = cubeList[27]
    rotatedCubeList[1] = cubeList[LEFT_UPPER_MIDDLE]
    rotatedCubeList[2] = cubeList[29]
    
    #rotate left to top
    rotatedCubeList[27] = cubeList[18]
    rotatedCubeList[LEFT_UPPER_MIDDLE] = cubeList[BACK_UPPER_MIDDLE] 
    rotatedCubeList[29] = cubeList[20]

    result['cube'] = rotatedCubeList
    result['letter'] = 'u'
    return result

#Rotate bottom (Downward) face clockwise (D)
def _rotateD(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[45] = cubeList[51]
    rotatedCubeList[BOTTOM_UPPER_MIDDLE] = cubeList[48]
    rotatedCubeList[47] = cubeList[45]
    rotatedCubeList[48] = cubeList[BOTTOM_LOWER_MIDDLE]
    rotatedCubeList[BOTTOM_CENTER] = cubeList[BOTTOM_CENTER]
    rotatedCubeList[50] = cubeList[BOTTOM_UPPER_MIDDLE]
    rotatedCubeList[51] = cubeList[53]
    rotatedCubeList[BOTTOM_LOWER_MIDDLE] = cubeList[50]
    rotatedCubeList[53] = cubeList[47]
    
    #rotate top to left
    rotatedCubeList[6] = cubeList[33]
    rotatedCubeList[7] = cubeList[LEFT_LOWER_MIDDLE]
    rotatedCubeList[8] = cubeList[35]
    
    #rotate right to top
    rotatedCubeList[15] = cubeList[6]
    rotatedCubeList[RIGHT_LOWER_MIDDLE] = cubeList[7]
    rotatedCubeList[17] = cubeList[8]
    
    #rotate bottom to right
    rotatedCubeList[24] = cubeList[15]
    rotatedCubeList[BACK_LOWER_MIDDLE] = cubeList[RIGHT_LOWER_MIDDLE]
    rotatedCubeList[26] = cubeList[17]
    
    #rotate left to bottom
    rotatedCubeList[33] = cubeList[24]
    rotatedCubeList[LEFT_LOWER_MIDDLE] = cubeList[BACK_LOWER_MIDDLE] 
    rotatedCubeList[35] = cubeList[26]

    result['cube'] = rotatedCubeList
    result['letter'] = 'D'
    return result

#Rotate bottom (Downward) face counter-clockwise (d)
def _rotated(cube):
    result = {}
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[51] = cubeList[45]
    rotatedCubeList[48] = cubeList[BOTTOM_UPPER_MIDDLE]
    rotatedCubeList[45] = cubeList[47]
    rotatedCubeList[BOTTOM_LOWER_MIDDLE] = cubeList[48]
    rotatedCubeList[BOTTOM_CENTER] = cubeList[BOTTOM_CENTER]
    rotatedCubeList[BOTTOM_UPPER_MIDDLE] = cubeList[50]
    rotatedCubeList[53] = cubeList[51]
    rotatedCubeList[50] = cubeList[BOTTOM_LOWER_MIDDLE]
    rotatedCubeList[47] = cubeList[53]
    
    #rotate top to left
    rotatedCubeList[33] = cubeList[6]
    rotatedCubeList[LEFT_LOWER_MIDDLE] = cubeList[7]
    rotatedCubeList[35] = cubeList[8]
    
    #rotate right to top
    rotatedCubeList[6] = cubeList[15]
    rotatedCubeList[7] = cubeList[RIGHT_LOWER_MIDDLE]
    rotatedCubeList[8] = cubeList[17]
    
    #rotate bottom to right
    rotatedCubeList[15] = cubeList[24]
    rotatedCubeList[RIGHT_LOWER_MIDDLE] = cubeList[BACK_LOWER_MIDDLE]
    rotatedCubeList[17] = cubeList[26]
    
    #rotate left to bottom
    rotatedCubeList[24] = cubeList[33]
    rotatedCubeList[BACK_LOWER_MIDDLE] = cubeList[LEFT_LOWER_MIDDLE] 
    rotatedCubeList[26] = cubeList[35]

    result['cube'] = rotatedCubeList
    result['letter'] = 'd'
    return result
