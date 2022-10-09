import rubik.cube as rubik

"""
###############################################     
############### CUBE CONSTANTS ################
###############################################
"""

#CENTERS
FRONT_CENTER = 4
RIGHT_CENTER = 13
BACK_CENTER = 22
LEFT_CENTER = 31
TOP_CENTER = 40
BOTTOM_CENTER = 49 

#MIDDLES
FRONT_UPPER_MIDDLE = 1
FRONT_LOWER_MIDDLE = 7
RIGHT_UPPER_MIDDLE = 10
RIGHT_LOWER_MIDDLE = 16
BACK_UPPER_MIDDLE = 19
BACK_LOWER_MIDDLE = 25
LEFT_UPPER_MIDDLE = 28
LEFT_LOWER_MIDDLE = 34
TOP_UPPER_MIDDLE = 37
TOP_LOWER_MIDDLE = 43
BOTTOM_UPPER_MIDDLE = 46 
BOTTOM_LOWER_MIDDLE = 52

#SIDES
FRONT_PORT = 3
FRONT_STBD = 5
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

#INDIVIDUAL EDGES
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

#COMBINED EDGES
#TOP_UP_L_EDGE = {'Value': 1, 'EdgeIndices': {FRONT_UPPER_PORT_EDGE, LEFT_UPPER_PORT_EDGE, BACK_UPPER_STBD_EDGE}}


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

        elif bottomPetalIndex == BOTTOM_PORT:
            letters = 'LL'
            
        elif bottomPetalIndex == BOTTOM_STBD:
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
        
        if horizontalPetalIndex == FRONT_PORT:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'l')
            
        if horizontalPetalIndex == FRONT_STBD:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'R')
            
        if horizontalPetalIndex == RIGHT_PORT:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'f')
            
        if horizontalPetalIndex == RIGHT_STBD:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'B')
            
        if horizontalPetalIndex == BACK_PORT:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'r')
            
        if horizontalPetalIndex == BACK_STBD:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'L')

        if horizontalPetalIndex == LEFT_PORT:
            horizontalToDaisyResult['solution'], rotatedCubeList = _functionalRotations(rotatedCubeList, horizontalToDaisyResult, 'b')
            
        if horizontalPetalIndex == LEFT_STBD:
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
        
        if verticalPetalIndex == FRONT_UPPER_MIDDLE:
            rotatedCubeList, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(rotatedCubeList, veritcalToDaisyResult, "lfLDFF")
        
        if verticalPetalIndex == FRONT_LOWER_MIDDLE:
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
    if not (rotatedCubeList[FRONT_CENTER] == rotatedCubeList[FRONT_LOWER_MIDDLE] and rotatedCubeList[BOTTOM_CENTER] == rotatedCubeList[BOTTOM_UPPER_MIDDLE]):
        
        daisyResult = _daisyIntegrated(FRONT_CENTER, FRONT_UPPER_MIDDLE, TOP_LOWER_MIDDLE, encodedCube, result['solution'])
        rotatedCubeList, encodedCube = _daisyVariableUpdate(encodedCube, result, daisyResult)
        
    #Right Face 
    if not (rotatedCubeList[RIGHT_CENTER] == rotatedCubeList[RIGHT_LOWER_MIDDLE] and rotatedCubeList[BOTTOM_CENTER] == rotatedCubeList[BOTTOM_STBD]):
        
        daisyResult = _daisyIntegrated(RIGHT_CENTER, RIGHT_UPPER_MIDDLE, TOP_STBD, encodedCube, result['solution'])
        rotatedCubeList, encodedCube = _daisyVariableUpdate(encodedCube, result, daisyResult)
        
    # #Back Face 
    if not (rotatedCubeList[BACK_CENTER] == rotatedCubeList[BACK_LOWER_MIDDLE] and rotatedCubeList[BOTTOM_CENTER] == rotatedCubeList[BOTTOM_LOWER_MIDDLE]):
        
        daisyResult = _daisyIntegrated(BACK_CENTER, BACK_UPPER_MIDDLE, TOP_UPPER_MIDDLE, encodedCube, result['solution'])
        rotatedCubeList, encodedCube = _daisyVariableUpdate(encodedCube, result, daisyResult)

    # #Left Face 
    if not (rotatedCubeList[LEFT_CENTER] == rotatedCubeList[LEFT_LOWER_MIDDLE] and rotatedCubeList[BOTTOM_CENTER] == rotatedCubeList[BOTTOM_PORT]):
        
        daisyResult = _daisyIntegrated(LEFT_CENTER, LEFT_UPPER_MIDDLE, TOP_PORT, encodedCube, result['solution'])
        rotatedCubeList, encodedCube = _daisyVariableUpdate(encodedCube, result, daisyResult)
            
    result['cube'] = encodedCube
    return result

def _daisyURotations(uniqueCenter: int, topMiddle: int, adjacentDaisy: int, encodedCube, solution): 
    """ Sub-method for Integrated Daisy Method. Rotates U until alignment found. """
    daisyResult = {}
    cubeList = list(encodedCube)
    rotatedCubeList = cubeList[:]
    daisyResult['solution'] = solution
    daisyResult['daisyCubeList'] = encodedCube
    irrelevantVar = None
    
    while (rotatedCubeList[uniqueCenter]!= rotatedCubeList[topMiddle] or rotatedCubeList[adjacentDaisy] != rotatedCubeList[BOTTOM_CENTER]):
        
        irrelevantVar, encodedCube = _functionalRotations(rotatedCubeList, daisyResult, 'U')
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
        if uniqueCenter == FRONT_CENTER:
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
        numberOfPetalsFound, rotatedCubeList, result = _moveEachBottomCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, BOTTOM_UPPER_MIDDLE, TOP_LOWER_MIDDLE)
#Checking Left of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachBottomCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, BOTTOM_PORT, TOP_PORT)
#Checking Right of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachBottomCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, BOTTOM_STBD, TOP_STBD)
#Checking Bottom of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachBottomCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, BOTTOM_LOWER_MIDDLE, TOP_UPPER_MIDDLE)

    return numberOfPetalsFound, rotatedCubeList

def _moveEachBottomCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, cubeOne, cubeTwo):
    if rotatedCubeList[cubeOne] == rotatedCubeList[BOTTOM_CENTER]:
        bottomToDaisyResult = _unalignedBottomToDaisy(cubeOne, cubeTwo, result['solution'], rotatedCubeList)
        result['solution'] = bottomToDaisyResult.get('solution')
        rotatedCubeList = bottomToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

""" Horizontal Moves """
def _moveHorizontalCubesToDaisy(result, rotatedCubeList, numberOfPetalsFound):
#Check Front Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachFrontCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, FRONT_PORT, TOP_PORT)
#Check Front Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachFrontCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, FRONT_STBD, TOP_STBD)
#Check Right Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachFrontCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, RIGHT_PORT, TOP_LOWER_MIDDLE)
#Check Right Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachFrontCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, RIGHT_STBD, TOP_UPPER_MIDDLE)
#Check Back Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachFrontCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, BACK_PORT, TOP_STBD)
#Check Back Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachFrontCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, BACK_STBD, TOP_PORT)
#Check Left Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachFrontCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, LEFT_PORT, TOP_UPPER_MIDDLE)
#Check Left Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachFrontCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, LEFT_STBD, TOP_LOWER_MIDDLE)
  
    return numberOfPetalsFound, rotatedCubeList

def _moveEachFrontCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, cubeOne, cubeTwo):
    if rotatedCubeList[cubeOne] == rotatedCubeList[BOTTOM_CENTER]:
        horizontalToDaisyResult = _horizontalCubesToDaisy(cubeOne, cubeTwo, result['solution'], rotatedCubeList)
        result['solution'] = horizontalToDaisyResult.get('solution')
        rotatedCubeList = horizontalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, rotatedCubeList, result

""" Vertical Moves """
def _moveVerticalCubesToDaisy(result, rotatedCubeList, numberOfPetalsFound):
#Front Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, FRONT_UPPER_MIDDLE, TOP_LOWER_MIDDLE)
        #numberOfPetalsFound, rotatedCubeList, result = _moveFrontUpperVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound)
#Front Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, FRONT_LOWER_MIDDLE, TOP_LOWER_MIDDLE)
#Right Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, RIGHT_UPPER_MIDDLE, TOP_STBD)
#Right Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, RIGHT_LOWER_MIDDLE, TOP_STBD)
# Back Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, BACK_UPPER_MIDDLE, TOP_UPPER_MIDDLE)
# Back Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, BACK_LOWER_MIDDLE, TOP_UPPER_MIDDLE)
#Left Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, LEFT_UPPER_MIDDLE, TOP_PORT)
#Left Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, rotatedCubeList, result = _moveEachVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, LEFT_LOWER_MIDDLE, TOP_PORT)
        
    return numberOfPetalsFound, rotatedCubeList

def _moveEachVerticalCubeToDaisy(result, rotatedCubeList, numberOfPetalsFound, cubeOne, cubeTwo):
    if rotatedCubeList[cubeOne] == rotatedCubeList[BOTTOM_CENTER]:
        verticalToDaisyResult = _verticalCubesToDaisy(cubeOne, cubeTwo, result['solution'], rotatedCubeList)
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
    if rotatedCubeList[TOP_PORT] == rotatedCubeList[BOTTOM_CENTER]:
        numberOfPetalsFound += 1
    if rotatedCubeList[TOP_STBD] == rotatedCubeList[BOTTOM_CENTER]:
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
            and rotatedCubeList[BOTTOM_PORT] == rotatedCubeList[BOTTOM_CENTER] 
            and rotatedCubeList[BOTTOM_STBD] == rotatedCubeList[BOTTOM_CENTER] 
            and rotatedCubeList[BOTTOM_LOWER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER])
    
def _bottomCrossAligned(rotatedCubeList):
    return (rotatedCubeList[FRONT_CENTER] == rotatedCubeList[FRONT_LOWER_MIDDLE] 
            and rotatedCubeList[RIGHT_CENTER] == rotatedCubeList[RIGHT_LOWER_MIDDLE] 
            and rotatedCubeList[BACK_CENTER] == rotatedCubeList[BACK_LOWER_MIDDLE] 
            and rotatedCubeList[LEFT_CENTER] == rotatedCubeList[LEFT_LOWER_MIDDLE])
    
def _daisyExists(rotatedCubeList):
    return (rotatedCubeList[TOP_UPPER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER] 
            and rotatedCubeList[TOP_PORT] == rotatedCubeList[BOTTOM_CENTER] 
            and rotatedCubeList[TOP_STBD] == rotatedCubeList[BOTTOM_CENTER] 
            and rotatedCubeList[TOP_LOWER_MIDDLE] == rotatedCubeList[BOTTOM_CENTER])


"""
###############################################################        
########### Bottom Edge ###########
###############################################################
"""

def _findBottomEdge(rotatedCubeList):
    rcl = rotatedCubeList
    
    triangulatedBottomEdge_BFR = {rcl[BOTTOM_CENTER], rcl[FRONT_CENTER], rcl[RIGHT_CENTER]}
    
    #EDGES WITH TOP THEN SIDE AND THEN FACE (Ordered, for orientation with bottom)
    TOP_UPR_L_EDGE = {'Value': 1, 'Colors': {rcl[TOP_UPPER_PORT_EDGE], rcl[LEFT_UPPER_PORT_EDGE], rcl[BACK_UPPER_STBD_EDGE]}}
    TOP_UPR_R_EDGE = {'Value': 2, 'Colors': {rcl[TOP_UPPER_STBD_EDGE], rcl[BACK_UPPER_PORT_EDGE], rcl[RIGHT_UPPER_STBD_EDGE]}}
    TOP_LWR_L_EDGE = {'Value': 4, 'Colors': {rcl[TOP_LOWER_PORT_EDGE], rcl[FRONT_UPPER_PORT_EDGE], rcl[LEFT_UPPER_STBD_EDGE]}}
    TOP_LWR_R_RDGE = {'Value': 3, 'Colors': {rcl[TOP_LOWER_STBD_EDGE], rcl[RIGHT_LOWER_PORT_EDGE], rcl[FRONT_UPPER_STBD_EDGE]}}
    
    #EDGES WITH BOTTOM THEN FACE AND THEN SIDE (Ordered)
    BTTM_UPR_L_EDGE = {'Value': 5, 'Colors': {rcl[BOTTOM_UPPER_PORT_EDGE], rcl[FRONT_LOWER_PORT_EDGE], rcl[LEFT_LOWER_STBD_EDGE]}}
    BTTM_UPR_R_EDGE = {'Value': 6, 'Colors': {rcl[BOTTOM_UPPER_STBD_EDGE], rcl[RIGHT_LOWER_PORT_EDGE], rcl[FRONT_LOWER_STBD_EDGE]}}
    BTTM_LWR_L_EDGE = {'Value': 8, 'Colors': {rcl[BOTTOM_LOWER_PORT_EDGE], rcl[LEFT_LOWER_PORT_EDGE], rcl[BACK_LOWER_STBD_EDGE]}}  
    BTTM_LWR_R_EDGE = {'Value': 7, 'Colors': {rcl[BOTTOM_LOWER_STBD_EDGE], rcl[BACK_LOWER_PORT_EDGE], rcl[RIGHT_LOWER_STBD]}}
    
    
    if triangulatedBottomEdge_BFR == BTTM_UPR_R_EDGE['Colors']:
        return True
    else:
        return False
    
    

    











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
############## Rotate Methods For Solving Cube ##############
#############################################################
"""
def _rotateF(cube):
    result = {}
    
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
        #rotate front face
    rotatedCubeList[FRONT_UPPER_STBD_EDGE] = cubeList[FRONT_UPPER_PORT_EDGE]
    rotatedCubeList[FRONT_STBD] = cubeList[FRONT_UPPER_MIDDLE]
    rotatedCubeList[FRONT_LOWER_STBD_EDGE] = cubeList[FRONT_UPPER_STBD_EDGE]
    rotatedCubeList[FRONT_UPPER_MIDDLE] = cubeList[FRONT_PORT]
    rotatedCubeList[FRONT_CENTER] = cubeList[FRONT_CENTER]
    rotatedCubeList[FRONT_LOWER_MIDDLE] = cubeList[FRONT_STBD]
    rotatedCubeList[FRONT_UPPER_PORT_EDGE] = cubeList[FRONT_LOWER_PORT_EDGE]
    rotatedCubeList[FRONT_PORT] = cubeList[FRONT_LOWER_MIDDLE]
    rotatedCubeList[FRONT_LOWER_PORT_EDGE] = cubeList[FRONT_LOWER_STBD_EDGE]
    
    #rotate top to right
    rotatedCubeList[RIGHT_UPPER_PORT_EDGE] = cubeList[TOP_LOWER_PORT_EDGE]
    rotatedCubeList[RIGHT_PORT] = cubeList[TOP_LOWER_MIDDLE]
    rotatedCubeList[RIGHT_LOWER_PORT_EDGE] = cubeList[TOP_LOWER_STBD_EDGE]
    
    #rotate right to bottom
    rotatedCubeList[BOTTOM_UPPER_STBD_EDGE] = cubeList[RIGHT_UPPER_PORT_EDGE]
    rotatedCubeList[BOTTOM_UPPER_MIDDLE] = cubeList[RIGHT_PORT]
    rotatedCubeList[BOTTOM_UPPER_PORT_EDGE] = cubeList[RIGHT_LOWER_PORT_EDGE]
    
    #rotate bottom to left
    rotatedCubeList[LEFT_UPPER_STBD_EDGE] = cubeList[BOTTOM_UPPER_PORT_EDGE]
    rotatedCubeList[LEFT_STBD] = cubeList[BOTTOM_UPPER_MIDDLE]
    rotatedCubeList[LEFT_LOWER_STBD_EDGE] = cubeList[BOTTOM_UPPER_STBD_EDGE]
    
    #rotate left to top
    rotatedCubeList[TOP_LOWER_STBD_EDGE] = cubeList[LEFT_UPPER_STBD_EDGE]
    rotatedCubeList[TOP_LOWER_MIDDLE] = cubeList[LEFT_STBD] 
    rotatedCubeList[TOP_LOWER_PORT_EDGE] = cubeList[LEFT_LOWER_STBD_EDGE]
    
    result['cube'] = rotatedCubeList
    result['letter'] = 'F'
    return result


#Rotate front face counter-clockwise (f)
def _rotatef(cube):
    result = {}
    
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate front face
    rotatedCubeList[FRONT_UPPER_PORT_EDGE] = cubeList[FRONT_UPPER_STBD_EDGE]
    rotatedCubeList[FRONT_UPPER_MIDDLE] = cubeList[FRONT_STBD]
    rotatedCubeList[FRONT_UPPER_STBD_EDGE] = cubeList[FRONT_LOWER_STBD_EDGE]
    rotatedCubeList[FRONT_PORT] = cubeList[FRONT_UPPER_MIDDLE]
    rotatedCubeList[FRONT_CENTER] = cubeList[FRONT_CENTER]
    rotatedCubeList[FRONT_STBD] = cubeList[FRONT_LOWER_MIDDLE]
    rotatedCubeList[FRONT_LOWER_PORT_EDGE] = cubeList[FRONT_UPPER_PORT_EDGE]
    rotatedCubeList[FRONT_LOWER_MIDDLE] = cubeList[FRONT_PORT]
    rotatedCubeList[FRONT_LOWER_STBD_EDGE] = cubeList[FRONT_LOWER_PORT_EDGE]
    
    #rotate right to top
    rotatedCubeList[TOP_LOWER_PORT_EDGE] = cubeList[RIGHT_UPPER_PORT_EDGE]
    rotatedCubeList[TOP_LOWER_MIDDLE] = cubeList[RIGHT_PORT]
    rotatedCubeList[TOP_LOWER_STBD_EDGE] = cubeList[RIGHT_LOWER_PORT_EDGE]
    
    #rotate bottom to right
    rotatedCubeList[RIGHT_UPPER_PORT_EDGE] = cubeList[BOTTOM_UPPER_STBD_EDGE]
    rotatedCubeList[RIGHT_PORT] = cubeList[BOTTOM_UPPER_MIDDLE]
    rotatedCubeList[RIGHT_LOWER_PORT_EDGE] = cubeList[BOTTOM_UPPER_PORT_EDGE]
    
    #rotate left to bottom
    rotatedCubeList[BOTTOM_UPPER_PORT_EDGE] = cubeList[LEFT_UPPER_STBD_EDGE]
    rotatedCubeList[BOTTOM_UPPER_MIDDLE] = cubeList[LEFT_STBD]
    rotatedCubeList[BOTTOM_UPPER_STBD_EDGE] = cubeList[LEFT_LOWER_STBD_EDGE]
    
    #rotate top to left
    rotatedCubeList[LEFT_UPPER_STBD_EDGE] = cubeList[TOP_LOWER_STBD_EDGE]
    rotatedCubeList[LEFT_STBD] = cubeList[TOP_LOWER_MIDDLE] 
    rotatedCubeList[LEFT_LOWER_STBD_EDGE] = cubeList[TOP_LOWER_PORT_EDGE]
    
    result['cube'] = rotatedCubeList
    result['letter'] = 'f'
    return result

#Rotate right face clockwise (R)
def _rotateR(cube):
    result = {}
    
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate front face
    rotatedCubeList[RIGHT_UPPER_STBD_EDGE] = cubeList[RIGHT_UPPER_PORT_EDGE]
    rotatedCubeList[RIGHT_STBD] = cubeList[RIGHT_UPPER_MIDDLE]
    rotatedCubeList[RIGHT_LOWER_STBD_EDGE] = cubeList[RIGHT_UPPER_STBD_EDGE]
    rotatedCubeList[RIGHT_UPPER_MIDDLE] = cubeList[RIGHT_PORT]
    rotatedCubeList[RIGHT_CENTER] = cubeList[RIGHT_CENTER]
    rotatedCubeList[RIGHT_LOWER_MIDDLE] = cubeList[RIGHT_STBD]
    rotatedCubeList[RIGHT_UPPER_PORT_EDGE] = cubeList[RIGHT_LOWER_PORT_EDGE]
    rotatedCubeList[RIGHT_PORT] = cubeList[RIGHT_LOWER_MIDDLE]
    rotatedCubeList[RIGHT_LOWER_PORT_EDGE] = cubeList[RIGHT_LOWER_STBD_EDGE]
    
    #rotate top to right
    rotatedCubeList[BACK_UPPER_PORT_EDGE] = cubeList[TOP_LOWER_STBD_EDGE]
    rotatedCubeList[BACK_PORT] = cubeList[TOP_STBD]
    rotatedCubeList[BACK_LOWER_PORT_EDGE] = cubeList[TOP_UPPER_STBD_EDGE]
    
    #rotate right to bottom
    rotatedCubeList[BOTTOM_LOWER_STBD_EDGE] = cubeList[BACK_UPPER_PORT_EDGE]
    rotatedCubeList[BOTTOM_STBD] = cubeList[BACK_PORT]
    rotatedCubeList[BOTTOM_UPPER_STBD_EDGE] = cubeList[BACK_LOWER_PORT_EDGE]
    
    #rotate bottom to left
    rotatedCubeList[FRONT_UPPER_STBD_EDGE] = cubeList[BOTTOM_UPPER_STBD_EDGE]
    rotatedCubeList[FRONT_STBD] = cubeList[BOTTOM_STBD]
    rotatedCubeList[FRONT_LOWER_STBD_EDGE] = cubeList[BOTTOM_LOWER_STBD_EDGE]
    
    #rotate left to top
    rotatedCubeList[TOP_UPPER_STBD_EDGE] = cubeList[FRONT_UPPER_STBD_EDGE]
    rotatedCubeList[TOP_STBD] = cubeList[FRONT_STBD] 
    rotatedCubeList[TOP_LOWER_STBD_EDGE] = cubeList[FRONT_LOWER_STBD_EDGE]
    
    result['cube'] = rotatedCubeList
    result['letter'] = 'R'
    return result

#Rotate right face counter-clockwise (r)
def _rotater(cube):
    result = {}
    
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate front face
    rotatedCubeList[RIGHT_UPPER_PORT_EDGE] = cubeList[RIGHT_UPPER_STBD_EDGE]
    rotatedCubeList[RIGHT_UPPER_MIDDLE] = cubeList[RIGHT_STBD]
    rotatedCubeList[RIGHT_UPPER_STBD_EDGE] = cubeList[RIGHT_LOWER_STBD_EDGE]
    rotatedCubeList[RIGHT_PORT] = cubeList[RIGHT_UPPER_MIDDLE]
    rotatedCubeList[RIGHT_CENTER] = cubeList[RIGHT_CENTER]
    rotatedCubeList[RIGHT_STBD] = cubeList[RIGHT_LOWER_MIDDLE]
    rotatedCubeList[RIGHT_LOWER_PORT_EDGE] = cubeList[RIGHT_UPPER_PORT_EDGE]
    rotatedCubeList[RIGHT_LOWER_MIDDLE] = cubeList[RIGHT_PORT]
    rotatedCubeList[RIGHT_LOWER_STBD_EDGE] = cubeList[RIGHT_LOWER_PORT_EDGE]
    
    #rotate top to right
    rotatedCubeList[TOP_LOWER_STBD_EDGE] = cubeList[BACK_UPPER_PORT_EDGE]
    rotatedCubeList[TOP_STBD] = cubeList[BACK_PORT]
    rotatedCubeList[TOP_UPPER_STBD_EDGE] = cubeList[BACK_LOWER_PORT_EDGE]
    
    #rotate right to bottom
    rotatedCubeList[BACK_UPPER_PORT_EDGE] = cubeList[BOTTOM_LOWER_STBD_EDGE]
    rotatedCubeList[BACK_PORT] = cubeList[BOTTOM_STBD]
    rotatedCubeList[BACK_LOWER_PORT_EDGE] = cubeList[BOTTOM_UPPER_STBD_EDGE]
    
    #rotate bottom to left
    rotatedCubeList[BOTTOM_UPPER_STBD_EDGE] = cubeList[FRONT_UPPER_STBD_EDGE]
    rotatedCubeList[BOTTOM_STBD] = cubeList[FRONT_STBD]
    rotatedCubeList[BOTTOM_LOWER_STBD_EDGE] = cubeList[FRONT_LOWER_STBD_EDGE]
    
    #rotate left to top
    rotatedCubeList[FRONT_UPPER_STBD_EDGE] = cubeList[TOP_UPPER_STBD_EDGE]
    rotatedCubeList[FRONT_STBD] = cubeList[TOP_STBD] 
    rotatedCubeList[FRONT_LOWER_STBD_EDGE] = cubeList[TOP_LOWER_STBD_EDGE]
    
    result['cube'] = rotatedCubeList
    result['letter'] = 'r'
    return result

#Rotate Back face clockwise (B)
def _rotateB(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[BACK_UPPER_STBD_EDGE] = cubeList[BACK_UPPER_PORT_EDGE]
    rotatedCubeList[BACK_STBD] = cubeList[BACK_UPPER_MIDDLE]
    rotatedCubeList[BACK_LOWER_STBD_EDGE] = cubeList[BACK_UPPER_STBD_EDGE]
    rotatedCubeList[BACK_UPPER_MIDDLE] = cubeList[BACK_PORT]
    rotatedCubeList[BACK_CENTER] = cubeList[BACK_CENTER]
    rotatedCubeList[BACK_LOWER_MIDDLE] = cubeList[BACK_STBD]
    rotatedCubeList[BACK_UPPER_PORT_EDGE] = cubeList[BACK_LOWER_PORT_EDGE]
    rotatedCubeList[BACK_PORT] = cubeList[BACK_LOWER_MIDDLE]
    rotatedCubeList[BACK_LOWER_PORT_EDGE] = cubeList[BACK_LOWER_STBD_EDGE]

    #rotate top to right
    rotatedCubeList[LEFT_UPPER_PORT_EDGE] = cubeList[TOP_UPPER_STBD_EDGE]
    rotatedCubeList[LEFT_PORT] = cubeList[TOP_UPPER_MIDDLE]
    rotatedCubeList[LEFT_LOWER_PORT_EDGE] = cubeList[TOP_UPPER_PORT_EDGE]

    #rotate right to bottom
    rotatedCubeList[BOTTOM_LOWER_PORT_EDGE] = cubeList[LEFT_UPPER_PORT_EDGE]
    rotatedCubeList[BOTTOM_LOWER_MIDDLE] = cubeList[LEFT_PORT]
    rotatedCubeList[BOTTOM_LOWER_STBD_EDGE] = cubeList[LEFT_LOWER_PORT_EDGE]

    #rotate bottom to left
    rotatedCubeList[RIGHT_LOWER_STBD_EDGE] = cubeList[BOTTOM_LOWER_PORT_EDGE]
    rotatedCubeList[RIGHT_STBD] = cubeList[BOTTOM_LOWER_MIDDLE]
    rotatedCubeList[RIGHT_UPPER_STBD_EDGE] = cubeList[BOTTOM_LOWER_STBD_EDGE]

    #rotate left to top
    rotatedCubeList[TOP_UPPER_PORT_EDGE] = cubeList[RIGHT_UPPER_STBD_EDGE]
    rotatedCubeList[TOP_UPPER_MIDDLE] = cubeList[RIGHT_STBD] 
    rotatedCubeList[TOP_UPPER_STBD_EDGE] = cubeList[RIGHT_LOWER_STBD_EDGE]
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
    rotatedCubeList[BACK_UPPER_PORT_EDGE] = cubeList[BACK_UPPER_STBD_EDGE]
    rotatedCubeList[BACK_UPPER_MIDDLE] = cubeList[BACK_STBD]
    rotatedCubeList[BACK_UPPER_STBD_EDGE] = cubeList[BACK_LOWER_STBD_EDGE]
    rotatedCubeList[BACK_PORT] = cubeList[BACK_UPPER_MIDDLE]
    rotatedCubeList[BACK_CENTER] = cubeList[BACK_CENTER]
    rotatedCubeList[BACK_STBD] = cubeList[BACK_LOWER_MIDDLE]
    rotatedCubeList[BACK_LOWER_PORT_EDGE] = cubeList[BACK_UPPER_PORT_EDGE]
    rotatedCubeList[BACK_LOWER_MIDDLE] = cubeList[BACK_PORT]
    rotatedCubeList[BACK_LOWER_STBD_EDGE] = cubeList[BACK_LOWER_PORT_EDGE]

    #rotate top to right
    rotatedCubeList[TOP_UPPER_STBD_EDGE] = cubeList[LEFT_UPPER_PORT_EDGE]
    rotatedCubeList[TOP_UPPER_MIDDLE] = cubeList[LEFT_PORT]
    rotatedCubeList[TOP_UPPER_PORT_EDGE] = cubeList[LEFT_LOWER_PORT_EDGE]

    #rotate right to bottom
    rotatedCubeList[LEFT_UPPER_PORT_EDGE] = cubeList[BOTTOM_LOWER_PORT_EDGE]
    rotatedCubeList[LEFT_PORT] = cubeList[BOTTOM_LOWER_MIDDLE]
    rotatedCubeList[LEFT_LOWER_PORT_EDGE] = cubeList[BOTTOM_LOWER_STBD_EDGE]

    #rotate bottom to left
    rotatedCubeList[BOTTOM_LOWER_PORT_EDGE] = cubeList[RIGHT_LOWER_STBD_EDGE]
    rotatedCubeList[BOTTOM_LOWER_MIDDLE] = cubeList[RIGHT_STBD]
    rotatedCubeList[BOTTOM_LOWER_STBD_EDGE] = cubeList[RIGHT_UPPER_STBD_EDGE]

    #rotate left to top
    rotatedCubeList[RIGHT_UPPER_STBD_EDGE] = cubeList[TOP_UPPER_PORT_EDGE]
    rotatedCubeList[RIGHT_STBD] = cubeList[TOP_UPPER_MIDDLE] 
    rotatedCubeList[RIGHT_LOWER_STBD_EDGE] = cubeList[TOP_UPPER_STBD_EDGE]
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
    rotatedCubeList[LEFT_UPPER_STBD_EDGE] = cubeList[LEFT_UPPER_PORT_EDGE]
    rotatedCubeList[LEFT_STBD] = cubeList[LEFT_UPPER_MIDDLE]
    rotatedCubeList[LEFT_LOWER_STBD_EDGE] = cubeList[LEFT_UPPER_STBD_EDGE]
    rotatedCubeList[LEFT_UPPER_MIDDLE] = cubeList[LEFT_PORT]
    rotatedCubeList[LEFT_CENTER] = cubeList[LEFT_CENTER]
    rotatedCubeList[LEFT_LOWER_MIDDLE] = cubeList[LEFT_STBD]
    rotatedCubeList[LEFT_UPPER_PORT_EDGE] = cubeList[LEFT_LOWER_PORT_EDGE]
    rotatedCubeList[LEFT_PORT] = cubeList[LEFT_LOWER_MIDDLE]
    rotatedCubeList[LEFT_LOWER_PORT_EDGE] = cubeList[LEFT_LOWER_STBD_EDGE]

    #rotate top to right
    rotatedCubeList[FRONT_UPPER_PORT_EDGE] = cubeList[TOP_UPPER_PORT_EDGE]
    rotatedCubeList[FRONT_PORT] = cubeList[TOP_PORT]
    rotatedCubeList[FRONT_LOWER_PORT_EDGE] = cubeList[TOP_LOWER_PORT_EDGE]

    #rotate right to bottom
    rotatedCubeList[BOTTOM_UPPER_PORT_EDGE] = cubeList[FRONT_UPPER_PORT_EDGE]
    rotatedCubeList[BOTTOM_PORT] = cubeList[FRONT_PORT]
    rotatedCubeList[BOTTOM_LOWER_PORT_EDGE] = cubeList[FRONT_LOWER_PORT_EDGE]

    #rotate bottom to left
    rotatedCubeList[BACK_LOWER_STBD_EDGE] = cubeList[BOTTOM_UPPER_PORT_EDGE]
    rotatedCubeList[BACK_STBD] = cubeList[BOTTOM_PORT]
    rotatedCubeList[BACK_UPPER_STBD_EDGE] = cubeList[BOTTOM_LOWER_PORT_EDGE]

    #rotate left to top
    rotatedCubeList[TOP_LOWER_PORT_EDGE] = cubeList[BACK_UPPER_STBD_EDGE]
    rotatedCubeList[TOP_PORT] = cubeList[BACK_STBD] 
    rotatedCubeList[TOP_UPPER_PORT_EDGE] = cubeList[BACK_LOWER_STBD_EDGE]

    result['cube'] = rotatedCubeList
    result['letter'] = 'L'
    return result

#Rotate Left face clockwise (l)
def _rotatel(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[LEFT_UPPER_PORT_EDGE] = cubeList[LEFT_UPPER_STBD_EDGE]
    rotatedCubeList[LEFT_UPPER_MIDDLE] = cubeList[LEFT_STBD]
    rotatedCubeList[LEFT_UPPER_STBD_EDGE] = cubeList[LEFT_LOWER_STBD_EDGE]
    rotatedCubeList[LEFT_PORT] = cubeList[LEFT_UPPER_MIDDLE]
    rotatedCubeList[LEFT_CENTER] = cubeList[LEFT_CENTER]
    rotatedCubeList[LEFT_STBD] = cubeList[LEFT_LOWER_MIDDLE]
    rotatedCubeList[LEFT_LOWER_PORT_EDGE] = cubeList[LEFT_UPPER_PORT_EDGE]
    rotatedCubeList[LEFT_LOWER_MIDDLE] = cubeList[LEFT_PORT]
    rotatedCubeList[LEFT_LOWER_STBD_EDGE] = cubeList[LEFT_LOWER_PORT_EDGE]
    
    #rotate top to right
    rotatedCubeList[TOP_UPPER_PORT_EDGE] = cubeList[FRONT_UPPER_PORT_EDGE]
    rotatedCubeList[TOP_PORT] = cubeList[FRONT_PORT]
    rotatedCubeList[TOP_LOWER_PORT_EDGE] = cubeList[FRONT_LOWER_PORT_EDGE]
    
    #rotate right to bottom
    rotatedCubeList[FRONT_UPPER_PORT_EDGE] = cubeList[BOTTOM_UPPER_PORT_EDGE]
    rotatedCubeList[FRONT_PORT] = cubeList[BOTTOM_PORT]
    rotatedCubeList[FRONT_LOWER_PORT_EDGE] = cubeList[BOTTOM_LOWER_PORT_EDGE]
    
    #rotate bottom to left
    rotatedCubeList[BOTTOM_LOWER_PORT_EDGE] = cubeList[BACK_UPPER_STBD_EDGE]
    rotatedCubeList[BOTTOM_PORT] = cubeList[BACK_STBD]
    rotatedCubeList[BOTTOM_UPPER_PORT_EDGE] = cubeList[BACK_LOWER_STBD_EDGE]
    
    #rotate left to top
    rotatedCubeList[BACK_UPPER_STBD_EDGE] = cubeList[TOP_LOWER_PORT_EDGE]
    rotatedCubeList[BACK_STBD] = cubeList[TOP_PORT] 
    rotatedCubeList[BACK_LOWER_STBD_EDGE] = cubeList[TOP_UPPER_PORT_EDGE]

    result['cube'] = rotatedCubeList
    result['letter'] = 'l'
    return result

#Rotate top (Upper) face clockwise (U)
def _rotateU(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[TOP_UPPER_STBD_EDGE] = cubeList[TOP_UPPER_PORT_EDGE]
    rotatedCubeList[TOP_STBD] = cubeList[TOP_UPPER_MIDDLE]
    rotatedCubeList[TOP_LOWER_STBD_EDGE] = cubeList[TOP_UPPER_STBD_EDGE]
    rotatedCubeList[TOP_UPPER_MIDDLE] = cubeList[TOP_PORT]
    rotatedCubeList[TOP_CENTER] = cubeList[TOP_CENTER]
    rotatedCubeList[TOP_LOWER_MIDDLE] = cubeList[TOP_STBD]
    rotatedCubeList[TOP_UPPER_PORT_EDGE] = cubeList[TOP_LOWER_PORT_EDGE]
    rotatedCubeList[TOP_PORT] = cubeList[TOP_LOWER_MIDDLE]
    rotatedCubeList[TOP_LOWER_PORT_EDGE] = cubeList[TOP_LOWER_STBD_EDGE]
    
    #rotate top to right
    rotatedCubeList[RIGHT_UPPER_PORT_EDGE] = cubeList[BACK_UPPER_PORT_EDGE]
    rotatedCubeList[RIGHT_UPPER_MIDDLE] = cubeList[BACK_UPPER_MIDDLE]
    rotatedCubeList[RIGHT_UPPER_STBD_EDGE] = cubeList[BACK_UPPER_STBD_EDGE]
    
    #rotate right to bottom
    rotatedCubeList[FRONT_UPPER_PORT_EDGE] = cubeList[RIGHT_UPPER_PORT_EDGE]
    rotatedCubeList[FRONT_UPPER_MIDDLE] = cubeList[RIGHT_UPPER_MIDDLE]
    rotatedCubeList[FRONT_UPPER_STBD_EDGE] = cubeList[RIGHT_UPPER_STBD_EDGE]
    
    #rotate bottom to left
    rotatedCubeList[LEFT_UPPER_PORT_EDGE] = cubeList[FRONT_UPPER_PORT_EDGE]
    rotatedCubeList[LEFT_UPPER_MIDDLE] = cubeList[FRONT_UPPER_MIDDLE]
    rotatedCubeList[LEFT_UPPER_STBD_EDGE] = cubeList[FRONT_UPPER_STBD_EDGE]
    
    #rotate left to top
    rotatedCubeList[BACK_UPPER_PORT_EDGE] = cubeList[LEFT_UPPER_PORT_EDGE]
    rotatedCubeList[BACK_UPPER_MIDDLE] = cubeList[LEFT_UPPER_MIDDLE] 
    rotatedCubeList[BACK_UPPER_STBD_EDGE] = cubeList[LEFT_UPPER_STBD_EDGE]

    result['cube'] = rotatedCubeList
    result['letter'] = 'U'
    return result

#Rotate top (Upper) face counter-clockwise (u)
def _rotateu(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[TOP_UPPER_PORT_EDGE] = cubeList[TOP_UPPER_STBD_EDGE]
    rotatedCubeList[TOP_UPPER_MIDDLE] = cubeList[TOP_STBD]
    rotatedCubeList[TOP_UPPER_STBD_EDGE] = cubeList[TOP_LOWER_STBD_EDGE]
    rotatedCubeList[TOP_PORT] = cubeList[TOP_UPPER_MIDDLE]
    rotatedCubeList[TOP_CENTER] = cubeList[TOP_CENTER]
    rotatedCubeList[TOP_STBD] = cubeList[TOP_LOWER_MIDDLE]
    rotatedCubeList[TOP_LOWER_PORT_EDGE] = cubeList[TOP_UPPER_PORT_EDGE]
    rotatedCubeList[TOP_LOWER_MIDDLE] = cubeList[TOP_PORT]
    rotatedCubeList[TOP_LOWER_STBD_EDGE] = cubeList[TOP_LOWER_PORT_EDGE]
    
    #rotate top to right
    rotatedCubeList[BACK_UPPER_PORT_EDGE] = cubeList[RIGHT_UPPER_PORT_EDGE]
    rotatedCubeList[BACK_UPPER_MIDDLE] = cubeList[RIGHT_UPPER_MIDDLE]
    rotatedCubeList[BACK_UPPER_STBD_EDGE] = cubeList[RIGHT_UPPER_STBD_EDGE]
    
    #rotate right to bottom
    rotatedCubeList[RIGHT_UPPER_PORT_EDGE] = cubeList[FRONT_UPPER_PORT_EDGE]
    rotatedCubeList[RIGHT_UPPER_MIDDLE] = cubeList[FRONT_UPPER_MIDDLE]
    rotatedCubeList[RIGHT_UPPER_STBD_EDGE] = cubeList[FRONT_UPPER_STBD_EDGE]
    
    #rotate bottom to left
    rotatedCubeList[FRONT_UPPER_PORT_EDGE] = cubeList[LEFT_UPPER_PORT_EDGE]
    rotatedCubeList[FRONT_UPPER_MIDDLE] = cubeList[LEFT_UPPER_MIDDLE]
    rotatedCubeList[FRONT_UPPER_STBD_EDGE] = cubeList[LEFT_UPPER_STBD_EDGE]
    
    #rotate left to top
    rotatedCubeList[LEFT_UPPER_PORT_EDGE] = cubeList[BACK_UPPER_PORT_EDGE]
    rotatedCubeList[LEFT_UPPER_MIDDLE] = cubeList[BACK_UPPER_MIDDLE] 
    rotatedCubeList[LEFT_UPPER_STBD_EDGE] = cubeList[BACK_UPPER_STBD_EDGE]

    result['cube'] = rotatedCubeList
    result['letter'] = 'u'
    return result

#Rotate bottom (Downward) face clockwise (D)
def _rotateD(cube):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[BOTTOM_UPPER_PORT_EDGE] = cubeList[BOTTOM_LOWER_PORT_EDGE]
    rotatedCubeList[BOTTOM_UPPER_MIDDLE] = cubeList[BOTTOM_PORT]
    rotatedCubeList[BOTTOM_UPPER_STBD_EDGE] = cubeList[BOTTOM_UPPER_PORT_EDGE]
    rotatedCubeList[BOTTOM_PORT] = cubeList[BOTTOM_LOWER_MIDDLE]
    rotatedCubeList[BOTTOM_CENTER] = cubeList[BOTTOM_CENTER]
    rotatedCubeList[BOTTOM_STBD] = cubeList[BOTTOM_UPPER_MIDDLE]
    rotatedCubeList[BOTTOM_LOWER_PORT_EDGE] = cubeList[BOTTOM_LOWER_STBD_EDGE]
    rotatedCubeList[BOTTOM_LOWER_MIDDLE] = cubeList[BOTTOM_STBD]
    rotatedCubeList[BOTTOM_LOWER_STBD_EDGE] = cubeList[BOTTOM_UPPER_STBD_EDGE]
    
    #rotate top to left
    rotatedCubeList[FRONT_LOWER_PORT_EDGE] = cubeList[LEFT_LOWER_PORT_EDGE]
    rotatedCubeList[FRONT_LOWER_MIDDLE] = cubeList[LEFT_LOWER_MIDDLE]
    rotatedCubeList[FRONT_LOWER_STBD_EDGE] = cubeList[LEFT_LOWER_STBD_EDGE]
    
    #rotate right to top
    rotatedCubeList[RIGHT_LOWER_PORT_EDGE] = cubeList[FRONT_LOWER_PORT_EDGE]
    rotatedCubeList[RIGHT_LOWER_MIDDLE] = cubeList[FRONT_LOWER_MIDDLE]
    rotatedCubeList[RIGHT_LOWER_STBD_EDGE] = cubeList[FRONT_LOWER_STBD_EDGE]
    
    #rotate bottom to right
    rotatedCubeList[BACK_LOWER_PORT_EDGE] = cubeList[RIGHT_LOWER_PORT_EDGE]
    rotatedCubeList[BACK_LOWER_MIDDLE] = cubeList[RIGHT_LOWER_MIDDLE]
    rotatedCubeList[BACK_LOWER_STBD_EDGE] = cubeList[RIGHT_LOWER_STBD_EDGE]
    
    #rotate left to bottom
    rotatedCubeList[LEFT_LOWER_PORT_EDGE] = cubeList[BACK_LOWER_PORT_EDGE]
    rotatedCubeList[LEFT_LOWER_MIDDLE] = cubeList[BACK_LOWER_MIDDLE] 
    rotatedCubeList[LEFT_LOWER_STBD_EDGE] = cubeList[BACK_LOWER_STBD_EDGE]

    result['cube'] = rotatedCubeList
    result['letter'] = 'D'
    return result

#Rotate bottom (Downward) face counter-clockwise (d)
def _rotated(cube):
    result = {}
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[BOTTOM_LOWER_PORT_EDGE] = cubeList[BOTTOM_UPPER_PORT_EDGE]
    rotatedCubeList[BOTTOM_PORT] = cubeList[BOTTOM_UPPER_MIDDLE]
    rotatedCubeList[BOTTOM_UPPER_PORT_EDGE] = cubeList[BOTTOM_UPPER_STBD_EDGE]
    rotatedCubeList[BOTTOM_LOWER_MIDDLE] = cubeList[BOTTOM_PORT]
    rotatedCubeList[BOTTOM_CENTER] = cubeList[BOTTOM_CENTER]
    rotatedCubeList[BOTTOM_UPPER_MIDDLE] = cubeList[BOTTOM_STBD]
    rotatedCubeList[BOTTOM_LOWER_STBD_EDGE] = cubeList[BOTTOM_LOWER_PORT_EDGE]
    rotatedCubeList[BOTTOM_STBD] = cubeList[BOTTOM_LOWER_MIDDLE]
    rotatedCubeList[BOTTOM_UPPER_STBD_EDGE] = cubeList[BOTTOM_LOWER_STBD_EDGE]
    
    #rotate top to left
    rotatedCubeList[LEFT_LOWER_PORT_EDGE] = cubeList[FRONT_LOWER_PORT_EDGE]
    rotatedCubeList[LEFT_LOWER_MIDDLE] = cubeList[FRONT_LOWER_MIDDLE]
    rotatedCubeList[LEFT_LOWER_STBD_EDGE] = cubeList[FRONT_LOWER_STBD_EDGE]
    
    #rotate right to top
    rotatedCubeList[FRONT_LOWER_PORT_EDGE] = cubeList[RIGHT_LOWER_PORT_EDGE]
    rotatedCubeList[FRONT_LOWER_MIDDLE] = cubeList[RIGHT_LOWER_MIDDLE]
    rotatedCubeList[FRONT_LOWER_STBD_EDGE] = cubeList[RIGHT_LOWER_STBD_EDGE]
    
    #rotate bottom to right
    rotatedCubeList[RIGHT_LOWER_PORT_EDGE] = cubeList[BACK_LOWER_PORT_EDGE]
    rotatedCubeList[RIGHT_LOWER_MIDDLE] = cubeList[BACK_LOWER_MIDDLE]
    rotatedCubeList[RIGHT_LOWER_STBD_EDGE] = cubeList[BACK_LOWER_STBD_EDGE]
    
    #rotate left to bottom
    rotatedCubeList[BACK_LOWER_PORT_EDGE] = cubeList[LEFT_LOWER_PORT_EDGE]
    rotatedCubeList[BACK_LOWER_MIDDLE] = cubeList[LEFT_LOWER_MIDDLE] 
    rotatedCubeList[BACK_LOWER_STBD_EDGE] = cubeList[LEFT_LOWER_STBD_EDGE]

    result['cube'] = rotatedCubeList
    result['letter'] = 'd'
    return result
