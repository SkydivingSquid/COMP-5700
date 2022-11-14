import rubik.cube as rubik
import hashlib
import random

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

#3D CUBES
TOP_UPR_L_EDGE = {'value': 3}
TOP_UPR_R_EDGE = {'value': 2}
TOP_LWR_L_EDGE = {'value': 4}
TOP_LWR_R_EDGE = {'value': 1}

BTTM_UPR_L_EDGE = {'value': 7}
BTTM_UPR_R_EDGE = {'value': 6}
BTTM_LWR_L_EDGE = {'value': 8}
BTTM_LWR_R_EDGE = {'value': 5}

#2D CUBES
TOP_FRONT_SIDE = {'value': 1}
TOP_RIGHT_SIDE = {'value': 2}
TOP_BACK_SIDE = {'value': 3}
TOP_LEFT_SIDE = {'value': 4}

MIDL_FRONT_EDGE = {'value': 5}
MIDL_RIGHT_EDGE = {'value': 6}
MIDL_BACK_EDGE = {'value': 7}
MIDL_LEFT_EDGE = {'value': 8}

#FLAGS
SINGLE_CUBE = 0 
ARM_LOWER_LEFT = 1
ARM_LOWER_RIGHT = 2 
ARM_UPPER_RIGHT = 3
ARM_UPPER_LEFT = 4
HORITZONAL_BAR = 5
VERTICAL_BAR = 6

#FACES
FRONT = 0
RIGHT = 1
BACK = 2
LEFT = 3

"""
#############################################################        
############### Main Method For Solving Cube ################
#############################################################
"""
def _solve(parms):
    """ Returns the solutions needed to solve a cube and the status of input. """
    result = {}
    result['rotations'] = ''
    result['status'] = ''
    FinalResult = {}
    encodedCube = parms.get('cube', None)

    #Verify If Input Is Valid and Return Status
    status = _verifyInput(encodedCube)

    #Solve for Bottom Cross and set rotations to the solution.
    if status == 'ok':
        FinalResult = _solveBottomCross(encodedCube) #Iteration 2

        FinalResult = _solveBottomFace(FinalResult.get('cube'), FinalResult.get('solution')) #Iteration 3

        FinalResult = _solveMiddleLayer(FinalResult.get('cube'), FinalResult.get('solution')) #Iteration 4
        
        FinalResult = _solveTopCross(FinalResult.get('cube'), FinalResult.get('solution')) #Iteration 5
        
        FinalResult = _solveTopFace(FinalResult.get('cube'), FinalResult.get('solution')) #Iteration 5a
        
        #FinalResult = _solveTopCorners(FinalResult.get('cube'), FinalResult.get('solution')) #Iteration 6a
        
        #FinalResult = _solveTopEdges(FinalResult.get('cube'), FinalResult.get('solution')) #Iteration 6b

        result['rotations'] = FinalResult.get('solution')
        
        result['rotations'] = _stringOptimizer(result['rotations'])
        
        result['token'] = _hashResult(encodedCube, result['rotations'])
    
    result['status'] = status

    return result

"""
########################################    
############### Hashing ################
########################################
"""
def _hashResult(encodedCube, solution):

    itemToTokenize = ''.join(encodedCube) + solution

    sha256Hash = hashlib.sha256()
    sha256Hash.update(itemToTokenize.encode())
    fullToken = sha256Hash.hexdigest()
    # Selects a random starting point in fullToken
    randToken = random.randint(1, len(fullToken)-8) 
    #selects a random 8 char substring of fullToken 
    subToken = fullToken[randToken:randToken+8] 
    #return a 8 char of hash token
    return subToken

"""
######################################################    
############### Solution Optimization ################
######################################################
"""

def _stringOptimizer(solution):
    
    initialLength = len(solution)
    flag = True
    
    solutionOptimizationDict = {
        'FFFF' : '',
        
        'UUU' : 'u', 'uuu' : 'U',
        
        'Ff' : '', 'fF' : '',
        'Rr' : '', 'rR' : '',
        'Bb' : '', 'bB' : '',
        'Ll' : '', 'lL' : '',
        'Uu' : '', 'uU' : '',
        'Dd' : '', 'dD' : '',
    }
    
    while (flag):
        for key, value in solutionOptimizationDict.items():
            solution = solution.replace(key, value)
        updatedSolutionLength = len(solution)
      
        if updatedSolutionLength == initialLength:
            flag = False
        else:
            initialLength = updatedSolutionLength
            
    return(solution)

"""
############################################       
############## Verify Inputs ###############
############################################
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
    result['solution'] = ""

    #Check for bottom cross
    if (_bottomCrossExists(encodedCube)):

        #Check for bottom cross alignment
        if (_bottomCrossAligned(encodedCube)):
            result['solution'] = ''
            result['cube'] = encodedCube
            return result

        #Rotate unaligned bottom cross into top daisy
        else:
            encodedCube = _bottomCrossToDaisy(encodedCube, result)
            daisySolution = _daisySolution(encodedCube)
            result['solution'] += daisySolution.get('solution')
            result['cube'] = encodedCube
            return result

    #Check Top for Daisy
    elif (_daisyExists(encodedCube)):
        daisySolution = _daisySolution(encodedCube)
        result['solution'] += daisySolution.get('solution')
        result['cube'] = encodedCube
        return result

    #If Not a Daisy
    else:
        encodedCube = _notDaisyCase(result, encodedCube)

    #TIME FOR DAISY SOLUTION HERE
    daisySolution = _daisySolution(encodedCube)
    encodedCube = daisySolution.get('cube')

    result['solution'] += daisySolution.get('solution')
    result['cube'] = encodedCube

    return result

def _bottomCrossToDaisy(encodedCube, result):
    """ Rotate an unaligned Bottom-Cross into a Daisy """

    algorithm = 'FFRRBBLL'

    for char in algorithm:
        result['solution'], encodedCube = _functionalRotations(encodedCube, result, char)

    return encodedCube

def _unalignedBottomToDaisy(bottomPetalIndex: int, topPetalIndex: int, solution, encodedCube):
    """ Moves unaligned bottom pieces to top to begin forming a Daisy """
    result = argsResult(encodedCube, solution)

    while encodedCube[bottomPetalIndex] == encodedCube[topPetalIndex]:
        result['solution'], encodedCube = _functionalRotations(encodedCube, result, 'U')

    if encodedCube[bottomPetalIndex] != encodedCube[topPetalIndex]:

        if bottomPetalIndex == BOTTOM_UPPER_MIDDLE:
            letters = 'FF'

        elif bottomPetalIndex == BOTTOM_PORT:
            letters = 'LL'

        elif bottomPetalIndex == BOTTOM_STBD:
            letters = 'RR'

        elif bottomPetalIndex == BOTTOM_LOWER_MIDDLE:
            letters = 'BB'

        for char in letters:
            result['solution'], encodedCube = _functionalRotations(encodedCube, result, char)

        result['rotatedCubeList'] = encodedCube
    return result

def _horizontalCubesToDaisy(horizontalPetalIndex: int, topPetalIndex: int, solution, encodedCube):
    """ Moves horizontal pieces to top to begin forming a Daisy """
    result = argsResult(encodedCube, solution)

    while encodedCube[horizontalPetalIndex] == encodedCube[topPetalIndex]:
        result['solution'], encodedCube = _functionalRotations(encodedCube, result, 'U')

    if encodedCube[horizontalPetalIndex] != encodedCube[topPetalIndex]:

        if horizontalPetalIndex == FRONT_PORT:
            result['solution'], encodedCube = _functionalRotations(encodedCube, result, 'l')

        if horizontalPetalIndex == FRONT_STBD:
            result['solution'], encodedCube = _functionalRotations(encodedCube, result, 'R')

        if horizontalPetalIndex == RIGHT_PORT:
            result['solution'], encodedCube = _functionalRotations(encodedCube, result, 'f')

        if horizontalPetalIndex == RIGHT_STBD:
            result['solution'], encodedCube = _functionalRotations(encodedCube, result, 'B')

        if horizontalPetalIndex == BACK_PORT:
            result['solution'], encodedCube = _functionalRotations(encodedCube, result, 'r')

        if horizontalPetalIndex == BACK_STBD:
            result['solution'], encodedCube = _functionalRotations(encodedCube, result, 'L')

        if horizontalPetalIndex == LEFT_PORT:
            result['solution'], encodedCube = _functionalRotations(encodedCube, result, 'b')

        if horizontalPetalIndex == LEFT_STBD:
            result['solution'], encodedCube = _functionalRotations(encodedCube, result, 'F')

        result['rotatedCubeList'] = encodedCube
    return result

def _verticalCubesToDaisy(verticalPetalIndex: int, topPetalIndex: int, solution, encodedCube):
    """ Moves vertical pieces to top to begin forming a Daisy """
    result = argsResult(encodedCube, solution)

    while encodedCube[verticalPetalIndex] == encodedCube[topPetalIndex]:
        result['solution'], encodedCube = _functionalRotations(encodedCube, result, 'U')

    if encodedCube[verticalPetalIndex] != encodedCube[topPetalIndex]:

        if verticalPetalIndex == FRONT_UPPER_MIDDLE:
            encodedCube, result['solution'] = _verticalCubeIntoDaisy(encodedCube, result, "lfLDFF")

        if verticalPetalIndex == FRONT_LOWER_MIDDLE:
            encodedCube, result['solution'] = _verticalCubeIntoDaisy(encodedCube, result, "FFlfLDFF")

        if verticalPetalIndex == RIGHT_UPPER_MIDDLE:
            encodedCube, result['solution'] = _verticalCubeIntoDaisy(encodedCube, result, "frFDRR")

        if verticalPetalIndex == RIGHT_LOWER_MIDDLE:
            encodedCube, result['solution'] = _verticalCubeIntoDaisy(encodedCube, result, "RRfrFDRR")

        if verticalPetalIndex == BACK_UPPER_MIDDLE:
            encodedCube, result['solution'] = _verticalCubeIntoDaisy(encodedCube, result, "rbRDBB")

        if verticalPetalIndex == BACK_LOWER_MIDDLE:
            encodedCube, result['solution'] = _verticalCubeIntoDaisy(encodedCube, result, "BBrbRDBB")

        if verticalPetalIndex == LEFT_UPPER_MIDDLE:
            encodedCube, result['solution'] = _verticalCubeIntoDaisy(encodedCube, result, "blBDLL")

        if verticalPetalIndex == LEFT_LOWER_MIDDLE:
            encodedCube, result['solution'] = _verticalCubeIntoDaisy(encodedCube, result, "LLblBDLL")

        result['rotatedCubeList'] = encodedCube
    return result

"""  
########################################################       
############## Methods for Solving Daisy ###############
########################################################
"""
def _daisyVariableUpdate(result, daisyResult):
    """ Sets variables post daisyIntegrated. Forgot to refactor this into it originally. """
    result['solution'] = daisyResult.get('solution')
    encodedCube = daisyResult.get('daisyCubeList')

    return encodedCube

def _daisySolution(encodedCube):
    """ When a daisy is made, align colors and rotate into Bottom Cross solution. """
    result = {}
    daisyResult = {}
    result['solution'] = ""

    #Front Face
    if not (encodedCube[FRONT_CENTER] == encodedCube[FRONT_LOWER_MIDDLE] and encodedCube[BOTTOM_CENTER] == encodedCube[BOTTOM_UPPER_MIDDLE]):

        daisyResult = _daisyIntegrated(FRONT_CENTER, FRONT_UPPER_MIDDLE, TOP_LOWER_MIDDLE, encodedCube, result['solution'])
        encodedCube = _daisyVariableUpdate(result, daisyResult)

    #Right Face
    if not (encodedCube[RIGHT_CENTER] == encodedCube[RIGHT_LOWER_MIDDLE] and encodedCube[BOTTOM_CENTER] == encodedCube[BOTTOM_STBD]):

        daisyResult = _daisyIntegrated(RIGHT_CENTER, RIGHT_UPPER_MIDDLE, TOP_STBD, encodedCube, result['solution'])
        encodedCube = _daisyVariableUpdate(result, daisyResult)

    # #Back Face
    if not (encodedCube[BACK_CENTER] == encodedCube[BACK_LOWER_MIDDLE] and encodedCube[BOTTOM_CENTER] == encodedCube[BOTTOM_LOWER_MIDDLE]):

        daisyResult = _daisyIntegrated(BACK_CENTER, BACK_UPPER_MIDDLE, TOP_UPPER_MIDDLE, encodedCube, result['solution'])
        encodedCube = _daisyVariableUpdate(result, daisyResult)

    # #Left Face
    if not (encodedCube[LEFT_CENTER] == encodedCube[LEFT_LOWER_MIDDLE] and encodedCube[BOTTOM_CENTER] == encodedCube[BOTTOM_PORT]):

        daisyResult = _daisyIntegrated(LEFT_CENTER, LEFT_UPPER_MIDDLE, TOP_PORT, encodedCube, result['solution'])
        encodedCube = _daisyVariableUpdate(result, daisyResult)

    result['cube'] = encodedCube
    return result

def _daisyURotations(uniqueCenter: int, topMiddle: int, adjacentDaisy: int, encodedCube, solution):
    """ Sub-method for Integrated Daisy Method. Rotates U until alignment found. """
    result = argsResult(encodedCube, solution)

    while (encodedCube[uniqueCenter]!= encodedCube[topMiddle] or encodedCube[adjacentDaisy] != encodedCube[BOTTOM_CENTER]):

        result['solution'], encodedCube  = _functionalRotations(encodedCube, result, 'U')

    result['daisyCubeList'] = encodedCube
    return result

def _daisy_Rotations(uniqueCenter: int, topMiddle: int, encodedCube, solution):
    """ Sub-method for Integrated Daisy Method. Rotates the block a specific direction depending on its uniqueCenter. """
    result = argsResult(encodedCube, solution)

    if encodedCube[uniqueCenter] == encodedCube[topMiddle]:
        if uniqueCenter == FRONT_CENTER:
            letters = 'FF'

        if uniqueCenter == RIGHT_CENTER:
            letters = 'RR'

        if uniqueCenter == BACK_CENTER:
            letters = 'BB'

        if uniqueCenter == LEFT_CENTER:
            letters = 'LL'

        for char in letters:
            result['solution'], encodedCube = _functionalRotations(encodedCube, result, char)

    result['daisyCubeList'] = encodedCube

    return result

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
def _verticalCubeIntoDaisy(encodedCube, veritcalToDaisyResult, algorithm):

    for char in algorithm:
        veritcalToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, veritcalToDaisyResult, char)

    return encodedCube, veritcalToDaisyResult['solution']

"""
#############################################################        
########### Bottom-Cross Methods For Solving Cube ###########
#############################################################
"""

""" Bottom Moves """
def _moveBottomCubesToDaisy(result, encodedCube, numberOfPetalsFound):
    #Checking Top of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, BOTTOM_UPPER_MIDDLE, TOP_LOWER_MIDDLE, _unalignedBottomToDaisy)
    #Checking Left of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, BOTTOM_PORT, TOP_PORT, _unalignedBottomToDaisy)
    #Checking Right of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, BOTTOM_STBD, TOP_STBD, _unalignedBottomToDaisy)
    #Checking Bottom of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, BOTTOM_LOWER_MIDDLE, TOP_UPPER_MIDDLE, _unalignedBottomToDaisy)

    return numberOfPetalsFound, encodedCube

""" Horizontal Moves """
def _moveHorizontalCubesToDaisy(result, encodedCube, numberOfPetalsFound):
    #Check Front Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, FRONT_PORT, TOP_PORT, _horizontalCubesToDaisy)
    #Check Front Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, FRONT_STBD, TOP_STBD, _horizontalCubesToDaisy)
    #Check Right Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, RIGHT_PORT, TOP_LOWER_MIDDLE, _horizontalCubesToDaisy)
    #Check Right Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, RIGHT_STBD, TOP_UPPER_MIDDLE, _horizontalCubesToDaisy)
    #Check Back Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, BACK_PORT, TOP_STBD, _horizontalCubesToDaisy)
    #Check Back Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, BACK_STBD, TOP_PORT, _horizontalCubesToDaisy)
    #Check Left Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, LEFT_PORT, TOP_UPPER_MIDDLE, _horizontalCubesToDaisy)
    #Check Left Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, LEFT_STBD, TOP_LOWER_MIDDLE, _horizontalCubesToDaisy)

    return numberOfPetalsFound, encodedCube

""" Vertical Moves """
def _moveVerticalCubesToDaisy(result, encodedCube, numberOfPetalsFound):
    #Front Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, FRONT_UPPER_MIDDLE, TOP_LOWER_MIDDLE, _verticalCubesToDaisy)
        #numberOfPetalsFound, encodedCube, result = _moveFrontUpperVerticalCubeToDaisy(result, encodedCube, numberOfPetalsFound)
    #Front Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, FRONT_LOWER_MIDDLE, TOP_LOWER_MIDDLE, _verticalCubesToDaisy)
    #Right Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, RIGHT_UPPER_MIDDLE, TOP_STBD, _verticalCubesToDaisy)
    #Right Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, RIGHT_LOWER_MIDDLE, TOP_STBD, _verticalCubesToDaisy)
    # Back Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, BACK_UPPER_MIDDLE, TOP_UPPER_MIDDLE, _verticalCubesToDaisy)
    # Back Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, BACK_LOWER_MIDDLE, TOP_UPPER_MIDDLE, _verticalCubesToDaisy)
    #Left Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, LEFT_UPPER_MIDDLE, TOP_PORT, _verticalCubesToDaisy)
    #Left Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, LEFT_LOWER_MIDDLE, TOP_PORT, _verticalCubesToDaisy)

    return numberOfPetalsFound, encodedCube

def _moveEachToDaisy(result, encodedCube, numberOfPetalsFound, cubeOne, cubeTwo, algo):
    if encodedCube[cubeOne] == encodedCube[BOTTOM_CENTER]:
        toDaisyResult = algo(cubeOne, cubeTwo, result['solution'], encodedCube)
        result['solution'] = toDaisyResult.get('solution')
        encodedCube = toDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, encodedCube, result

"""
###############################################################        
########### Bottom Cross / Daisy Orientation Checks ###########
###############################################################
"""
def _countTopPetals(encodedCube):
    numberOfPetalsFound = 0
    if encodedCube[TOP_UPPER_MIDDLE] == encodedCube[BOTTOM_CENTER]:
        numberOfPetalsFound += 1
    if encodedCube[TOP_PORT] == encodedCube[BOTTOM_CENTER]:
        numberOfPetalsFound += 1
    if encodedCube[TOP_STBD] == encodedCube[BOTTOM_CENTER]:
        numberOfPetalsFound += 1
    if encodedCube[TOP_LOWER_MIDDLE] == encodedCube[BOTTOM_CENTER]:
        numberOfPetalsFound += 1
    return numberOfPetalsFound

def _notDaisyCase(result, encodedCube):
    #Count Number of Top Petals
    numberOfPetalsFound = _countTopPetals(encodedCube)
    while numberOfPetalsFound <= 3:
        #Bottom Cubes To Daisy
        numberOfPetalsFound, encodedCube = _moveBottomCubesToDaisy(result, encodedCube, numberOfPetalsFound)
        #Horizontal Cubes To Daisy
        numberOfPetalsFound, encodedCube = _moveHorizontalCubesToDaisy(result, encodedCube, numberOfPetalsFound)
        #Vertical Cubes To Daisy
        numberOfPetalsFound, encodedCube = _moveVerticalCubesToDaisy(result, encodedCube, numberOfPetalsFound)

    return encodedCube

def _bottomCrossExists(encodedCube):
    return (encodedCube[BOTTOM_UPPER_MIDDLE] == encodedCube[BOTTOM_CENTER]
            and encodedCube[BOTTOM_PORT] == encodedCube[BOTTOM_CENTER]
            and encodedCube[BOTTOM_STBD] == encodedCube[BOTTOM_CENTER]
            and encodedCube[BOTTOM_LOWER_MIDDLE] == encodedCube[BOTTOM_CENTER])

def _bottomCrossAligned(encodedCube):
    return (encodedCube[FRONT_CENTER] == encodedCube[FRONT_LOWER_MIDDLE]
            and encodedCube[RIGHT_CENTER] == encodedCube[RIGHT_LOWER_MIDDLE]
            and encodedCube[BACK_CENTER] == encodedCube[BACK_LOWER_MIDDLE]
            and encodedCube[LEFT_CENTER] == encodedCube[LEFT_LOWER_MIDDLE])

def _daisyExists(encodedCube):
    return (encodedCube[TOP_UPPER_MIDDLE] == encodedCube[BOTTOM_CENTER]
            and encodedCube[TOP_PORT] == encodedCube[BOTTOM_CENTER]
            and encodedCube[TOP_STBD] == encodedCube[BOTTOM_CENTER]
            and encodedCube[TOP_LOWER_MIDDLE] == encodedCube[BOTTOM_CENTER])
"""
############################################        
########### Solving Bottom Edges ###########
############################################
"""
def _solveBottomFace(encodedCube, solution):
    '''Main method for solving the bottom edges (post bottom cross)'''
    #This will likely need to have the solution passed as an argument.
    result = {}

    #FIRST WILL SOLVE BOTTOM UPPER RIGHT CORNER (6). Find cube with desired colors.
    cubeLctn = _findBottomEdge(encodedCube, BOTTOM_CENTER, FRONT_CENTER, RIGHT_CENTER) # <- UNIQUE

    #IF CUBE IN CORRECT SPOT AND ORIENTED CORRECTLY, GO TO NEXT SPOT
    if (cubeLctn == BTTM_UPR_R_EDGE['value'] and encodedCube[BOTTOM_UPPER_STBD_EDGE] == encodedCube[BOTTOM_CENTER]):
        cubeLctn = _findBottomEdge(encodedCube, BOTTOM_CENTER, RIGHT_CENTER, BACK_CENTER)

    else:
        cubeLctn, encodedCube, solution = _unalighedBottomEdge(encodedCube, solution, result, cubeLctn,
                                                               TOP_LWR_R_EDGE['value'], TOP_LOWER_STBD_EDGE, FRONT_UPPER_STBD_EDGE, BOTTOM_CENTER, RIGHT_CENTER, BACK_CENTER)

    #SECOND WILL SOLVE BOTTOM LOWER RIGHT CORNER (7)
    if (cubeLctn == BTTM_LWR_R_EDGE['value'] and encodedCube[BOTTOM_LOWER_STBD_EDGE] == encodedCube[BOTTOM_CENTER]):
        cubeLctn = _findBottomEdge(encodedCube, BOTTOM_CENTER, BACK_CENTER, LEFT_CENTER)

    else:
        cubeLctn, encodedCube, solution = _unalighedBottomEdge(encodedCube, solution, result, cubeLctn,
                                                               TOP_UPR_R_EDGE['value'], TOP_UPPER_STBD_EDGE, RIGHT_UPPER_STBD_EDGE, BOTTOM_CENTER, BACK_CENTER, LEFT_CENTER)

    #THIRD WILL SOLVE BOTTOM LOWER LEFT CORNER (8)
    if (cubeLctn == BTTM_LWR_L_EDGE['value'] and encodedCube[BOTTOM_LOWER_PORT_EDGE] == encodedCube[BOTTOM_CENTER]):
        cubeLctn = _findBottomEdge(encodedCube, BOTTOM_CENTER, LEFT_CENTER, FRONT_CENTER)

    else:
        cubeLctn, encodedCube, solution = _unalighedBottomEdge(encodedCube, solution, result, cubeLctn,
                                                               TOP_UPR_L_EDGE['value'], TOP_UPPER_PORT_EDGE, BACK_UPPER_STBD_EDGE, BOTTOM_CENTER, LEFT_CENTER, FRONT_CENTER)

    #FINALLY WILL SOLVE BOTTOM UPPER LEFT CORNER (5)
    if (cubeLctn == BTTM_UPR_L_EDGE['value'] and encodedCube[BOTTOM_UPPER_PORT_EDGE] == encodedCube[BOTTOM_CENTER]):
        result['cube'], result['solution'] = encodedCube, solution # Runs this because its the final check..

    else:
        cubeLctn, encodedCube, solution = _unalighedBottomEdge(encodedCube, solution, result, cubeLctn,
                                                               TOP_LWR_L_EDGE['value'], TOP_LOWER_PORT_EDGE, LEFT_UPPER_STBD_EDGE, None, None, None)

    return result

def _unalighedBottomEdge(encodedCube, solution, result, cubeLctn, initialEdge, markerEdge1, markerEdge2, triEdge1, triEdge2, triEdge3):
    '''The major 'shot caller' for the main method (_solveBottomFace). This was made from refactoring for LOC limitation purposes'''
    encodedCube, solution, cubeLctn = _setBottomOrTopResult(encodedCube, solution, result, cubeLctn, initialEdge, _edgeList('Bottom'), _moveBottomEdgeToTopEdge)

    colorMarker = _setMarker(encodedCube, markerEdge1, markerEdge2, BOTTOM_CENTER)

    encodedCube, solution = _setTopResult(encodedCube, solution, result, colorMarker, cubeLctn, _topToBottomEdgeAlgorithm)

    if (triEdge1 != None): #This is to avoid setting an irrelevant variable on edge 4.
        cubeLctn = _findBottomEdge(encodedCube, triEdge1, triEdge2, triEdge3)

    return cubeLctn, encodedCube, solution

def _topToBottomEdgeAlgorithm(encodedCube,solution,cubeLctn, colorMarker):
    '''Moves correct top cube to correct bottom cube'''
    result = argsResult(encodedCube, solution)
    movementList = ''

    if cubeLctn == TOP_LWR_L_EDGE['value']: #4
        if colorMarker == 1:
            movementList = 'luuLUluLU' #Valid for test 302
        elif colorMarker == 2:
            movementList = 'luLU'
        else:
            movementList = 'ulUL' #Valid for test 306

    if cubeLctn == TOP_LWR_R_EDGE['value']: #3
        if colorMarker == 1:
            movementList = 'fuuFUfuFU' #Valid for test 303
        elif colorMarker == 2:
            movementList = 'fuFU'
        else:
            movementList = 'ufUF' #Valid for test 307

    if cubeLctn == TOP_UPR_R_EDGE['value']: #2
        if colorMarker == 1:
            movementList = 'ruuRUruRU' #Valid for test 304
        elif colorMarker == 2:
            movementList = 'ruRU'
        else:
            movementList = 'urUR' #Valid for test 308

    if cubeLctn == TOP_UPR_L_EDGE['value']: #1
        if colorMarker == 1:
            movementList = 'buuBUbuBU' #Valid for test 305
        elif colorMarker == 2:
            movementList = 'buBU'
        else:
            movementList = 'ubUB' #Valid for test 309

    movementListMethod(encodedCube, result, movementList)

    return result

def _moveBottomEdgeToTopEdge(encodedCube, solution, cubeLocation):
    '''Based on cube location, rotate bottom edge to top edge'''
    result = argsResult(encodedCube, solution)
    movementList = ""
    value = cubeLocation

    #These four if statements direct movement of edge from bottom to top
    if value == BTTM_LWR_R_EDGE['value']: #7
        movementList = 'ruRU'
        cubeLocation = TOP_UPR_R_EDGE['value'] #2

    if value == BTTM_LWR_L_EDGE['value']: #8
        movementList = 'buBU'
        cubeLocation = TOP_UPR_L_EDGE['value'] #1

    if value == BTTM_UPR_L_EDGE['value']: #5
        movementList = 'luLU'
        cubeLocation = TOP_LWR_L_EDGE['value'] #4

    if value == BTTM_UPR_R_EDGE['value']: #6
        movementList = 'fuFU'
        cubeLocation = TOP_LWR_R_EDGE['value'] #3

    movementListMethod(encodedCube, result, movementList)

    result['cubeLocation'] = cubeLocation
    return result

def _findBottomEdge(encodedCube, zCube, yCube, xCube):
    '''This method finds the correct edge based on x,y,z cube colors and returns 1 of 8 edge locations'''
    rcl = encodedCube # This is just for ease of typing
    triangulatedBottomEdge = {rcl[zCube], rcl[yCube], rcl[xCube]}

    #EDGES WITH TOP THEN SIDE AND THEN FACE (Ordered, for orientation with bottom)
    TOP_UPR_L_EDGE = {'value': 3, 'Colors': {rcl[TOP_UPPER_PORT_EDGE], rcl[LEFT_UPPER_PORT_EDGE], rcl[BACK_UPPER_STBD_EDGE]}}
    TOP_UPR_R_EDGE = {'value': 2, 'Colors': {rcl[TOP_UPPER_STBD_EDGE], rcl[BACK_UPPER_PORT_EDGE], rcl[RIGHT_UPPER_STBD_EDGE]}}
    TOP_LWR_L_EDGE = {'value': 4, 'Colors': {rcl[TOP_LOWER_PORT_EDGE], rcl[FRONT_UPPER_PORT_EDGE], rcl[LEFT_UPPER_STBD_EDGE]}}
    TOP_LWR_R_EDGE = {'value': 1, 'Colors': {rcl[TOP_LOWER_STBD_EDGE], rcl[RIGHT_UPPER_PORT_EDGE], rcl[FRONT_UPPER_STBD_EDGE]}}

    #EDGES WITH BOTTOM THEN FACE AND THEN SIDE (Ordered)
    BTTM_UPR_L_EDGE = {'value': 7, 'Colors': {rcl[BOTTOM_UPPER_PORT_EDGE], rcl[FRONT_LOWER_PORT_EDGE], rcl[LEFT_LOWER_STBD_EDGE]}}
    BTTM_UPR_R_EDGE = {'value': 6, 'Colors': {rcl[BOTTOM_UPPER_STBD_EDGE], rcl[RIGHT_LOWER_PORT_EDGE], rcl[FRONT_LOWER_STBD_EDGE]}}
    BTTM_LWR_L_EDGE = {'value': 8, 'Colors': {rcl[BOTTOM_LOWER_PORT_EDGE], rcl[LEFT_LOWER_PORT_EDGE], rcl[BACK_LOWER_STBD_EDGE]}}
    BTTM_LWR_R_EDGE = {'value': 5, 'Colors': {rcl[BOTTOM_LOWER_STBD_EDGE], rcl[BACK_LOWER_PORT_EDGE], rcl[RIGHT_LOWER_STBD_EDGE]}}

    EdgeList = (TOP_UPR_L_EDGE, TOP_UPR_R_EDGE, TOP_LWR_L_EDGE, TOP_LWR_R_EDGE, BTTM_LWR_L_EDGE, BTTM_LWR_R_EDGE, BTTM_UPR_L_EDGE, BTTM_UPR_R_EDGE)

    EdgeNumber = 0

    while EdgeNumber < 8:
        if (triangulatedBottomEdge != EdgeList[EdgeNumber]['Colors']):
            EdgeNumber += 1

        else:
            return EdgeList[EdgeNumber]['value']

"""
############################################        
########### Solving Middle Edges ###########
############################################
"""
def _solveMiddleLayer(encodedCube, solution):
    '''Main method for solving the bottom edges (post bottom cross)'''

    result = {}
    #FIRST WILL SOLVE FRONT RIGHT CORNER (5). Find cube with desired colors.
    cubeLctn = _findMiddleEdge(encodedCube, FRONT_CENTER, RIGHT_CENTER) # <- UNIQUE

    #IF CUBE IN CORRECT SPOT AND ORIENTED CORRECTLY, GO TO NEXT SPOT
    if (cubeLctn == MIDL_FRONT_EDGE['value'] and encodedCube[FRONT_STBD] == encodedCube[FRONT_CENTER]):
        cubeLctn = _findMiddleEdge(encodedCube, RIGHT_CENTER, BACK_CENTER)

    else: 
        cubeLctn, encodedCube, solution = _unalighedMiddleEdge(encodedCube, solution, result, cubeLctn,
                                                               TOP_FRONT_SIDE['value'], TOP_LOWER_MIDDLE, FRONT_UPPER_MIDDLE, FRONT_CENTER, RIGHT_CENTER, BACK_CENTER)

    #SECOND WILL RIGHT RIGHT CORNER (6)
    if (cubeLctn == MIDL_RIGHT_EDGE['value'] and encodedCube[RIGHT_STBD] == encodedCube[RIGHT_CENTER]):
        cubeLctn = _findMiddleEdge(encodedCube, BACK_CENTER, LEFT_CENTER)

    else:
        cubeLctn, encodedCube, solution = _unalighedMiddleEdge(encodedCube, solution, result, cubeLctn,
                                                               TOP_RIGHT_SIDE['value'], TOP_STBD, RIGHT_UPPER_MIDDLE, RIGHT_CENTER, BACK_CENTER, LEFT_CENTER)

    #THIRD WILL SOLVE BACK RIGHT CORNER (7)
    if (cubeLctn == MIDL_BACK_EDGE['value'] and encodedCube[BACK_STBD] == encodedCube[BACK_CENTER]):
        cubeLctn = _findMiddleEdge(encodedCube, LEFT_CENTER, FRONT_CENTER)

    else:
        cubeLctn, encodedCube, solution = _unalighedMiddleEdge(encodedCube, solution, result, cubeLctn,
                                                               TOP_BACK_SIDE['value'], TOP_UPPER_MIDDLE, BACK_UPPER_MIDDLE, BACK_CENTER, LEFT_CENTER, FRONT_CENTER)

    #FINALLY WILL SOLVE LEFT RIGHT CORNER (8)
    if (cubeLctn == MIDL_LEFT_EDGE['value'] and encodedCube[LEFT_STBD] == encodedCube[LEFT_CENTER]):
        result['cube'], result['solution'] = encodedCube, solution # Runs this because its the final check..

    else:
        cubeLctn, encodedCube, solution = _unalighedMiddleEdge(encodedCube, solution, result, cubeLctn,
                                                               TOP_LEFT_SIDE['value'], TOP_PORT, LEFT_UPPER_MIDDLE, LEFT_CENTER, None, None)

    return result

def _unalighedMiddleEdge(encodedCube, solution, result, cubeLctn, initialEdge, markerEdge1, markerEdge2, center, sideEdge1, sideEdge2):
    '''The major 'shot caller' for the main method (_solveMiddleLayer).'''
    encodedCube, solution, cubeLctn = _setBottomOrTopResult(encodedCube, solution, result, cubeLctn, initialEdge, _edgeList('Middle'), _moveMiddleEdgeToTopSide)

    colorMarker = _setMarker(encodedCube, markerEdge1, markerEdge2, center)

    encodedCube, solution = _setTopResult(encodedCube, solution, result, colorMarker, cubeLctn, _topToMiddleEdgeAlgorithm)

    if (sideEdge1 != None): #This is to avoid setting an irrelevant variable
        cubeLctn = _findMiddleEdge(encodedCube, sideEdge1, sideEdge2)
    
    return cubeLctn, encodedCube, solution

def _moveMiddleEdgeToTopSide(encodedCube, solution, cubeLocation):
    '''Based on cube location, rotate bottom edge to top edge'''
    result = argsResult(encodedCube, solution)
    movementList = ""
    value = cubeLocation

    #These four if statements direct movement of edge from middle to top and set new location. 
    if value == MIDL_FRONT_EDGE['value']:
        movementList = 'URurufUF'
        cubeLocation = TOP_BACK_SIDE['value']

    if value == MIDL_RIGHT_EDGE['value']:
        movementList = 'UBuburUR'
        cubeLocation = TOP_LEFT_SIDE['value']

    if value == MIDL_BACK_EDGE['value']:
        movementList = 'ULulubUB'
        cubeLocation = TOP_FRONT_SIDE['value']

    if value == MIDL_LEFT_EDGE['value']:
        movementList = 'uFufulUL'
        cubeLocation = TOP_RIGHT_SIDE['value']

    movementListMethod(encodedCube, result, movementList)

    result['cubeLocation'] = cubeLocation
    return result

def _topToMiddleEdgeAlgorithm(encodedCube,solution,cubeLctn,colorMarker):
    '''Moves correct top cube to correct middle cube'''
    result = argsResult(encodedCube, solution)
    movementList = ''

    if cubeLctn == TOP_FRONT_SIDE['value']:
        if colorMarker == 1:
            movementList = 'uufUFURur' #LEFT Rotation
        elif colorMarker == 2:
            movementList = 'URurufUF'  #RIGHT Rotation

    if cubeLctn == TOP_RIGHT_SIDE['value']:
        if colorMarker == 1:
            movementList = 'uurURUBub' 
        elif colorMarker == 2:
            movementList = 'UBuburUR'

    if cubeLctn == TOP_BACK_SIDE['value']:
        if colorMarker == 1:
            movementList = 'uubUBULul'
        elif colorMarker == 2:
            movementList = 'ULulubUB'

    if cubeLctn == TOP_LEFT_SIDE['value']:
        if colorMarker == 1:
            movementList = 'uulULUFuf'
        elif colorMarker == 2:
            movementList = 'UFufulUL'

    movementListMethod(encodedCube, result, movementList)

    return result

def _findMiddleEdge(encodedCube, yCube, xCube):
    '''This method finds the correct edge based on x,y cube colors and returns 1 of 8 edge locations'''
    rcl = encodedCube # This is just for ease of typing
    triangulatedMiddleEdge = {rcl[yCube], rcl[xCube]}

    #EDGES WITH TOP THEN FACE
    TOP_FRONT_SIDE = {'value': 1, 'Colors': {rcl[TOP_LOWER_MIDDLE], rcl[FRONT_UPPER_MIDDLE]}}
    TOP_RIGHT_SIDE = {'value': 2, 'Colors': {rcl[TOP_STBD], rcl[RIGHT_UPPER_MIDDLE]}}
    TOP_BACK_SIDE = {'value': 3, 'Colors': {rcl[TOP_UPPER_MIDDLE], rcl[BACK_UPPER_MIDDLE]}}
    TOP_LEFT_SIDE = {'value': 4, 'Colors': {rcl[TOP_PORT], rcl[LEFT_UPPER_MIDDLE]}}

    #EDGES WITH FACE THEN SIDE
    MIDL_FRONT_EDGE = {'value': 5, 'Colors': {rcl[FRONT_STBD], rcl[RIGHT_PORT]}}
    MIDL_RIGHT_EDGE = {'value': 6, 'Colors': {rcl[RIGHT_STBD], rcl[BACK_PORT]}}
    MIDL_BACK_EDGE = {'value': 7, 'Colors': {rcl[BACK_STBD], rcl[LEFT_PORT]}}
    MIDL_LEFT_EDGE = {'value': 8, 'Colors': {rcl[LEFT_STBD], rcl[FRONT_PORT]}}

    edgeList = (TOP_FRONT_SIDE, TOP_RIGHT_SIDE, TOP_BACK_SIDE, TOP_LEFT_SIDE, MIDL_FRONT_EDGE, MIDL_RIGHT_EDGE, MIDL_BACK_EDGE, MIDL_LEFT_EDGE)

    edgeNumber = 0

    while edgeNumber < 8:
        if (triangulatedMiddleEdge != edgeList[edgeNumber]['Colors']):
            edgeNumber += 1

        else:
            return edgeList[edgeNumber]['value']

"""
##################################################################        
########### Shared Methods for Bottom and Middle Edges ###########
##################################################################
"""
def _edgeList(location):
    if (location == 'Middle'): #For Middle Layer
        return MIDL_FRONT_EDGE['value'], MIDL_RIGHT_EDGE['value'], MIDL_BACK_EDGE['value'], MIDL_LEFT_EDGE['value']

    elif (location == 'Bottom'): #For Bottom Face
        return BTTM_UPR_L_EDGE['value'], BTTM_UPR_R_EDGE['value'], BTTM_LWR_L_EDGE['value'], BTTM_LWR_R_EDGE['value']

def _moveTopByDifference(difference):
    '''Calculates difference between where edge is and where it needs to be. Gives rotation moves for later method'''
    if (difference == 0): #No rotation
        movementList = '' 
    elif (difference == 1 or difference == -3): #Clockwise rotation
        movementList = 'U'
    elif (difference == -1 or difference == 3): #Counter Clockwise Rotation
        movementList = 'u'
    elif (difference == 2 or difference == -2): #Double CLockwise
        movementList = 'UU'
    return movementList

def _solveEdges(encodedCube, solution, cubeLocation, correctLocation, edgeList, moveToTopAlgo):
    '''Moves unaligned edges (anywhere) to top, rotates to corresponding top, then moves into bottom or middle.
    This is one of the main working methods in solving the bottom and middle edges.'''

    result = argsResult(encodedCube, solution)
    result['cubeLocation'] = cubeLocation
    edgeSolutionSet = {}

    #Rotate edge out of bottom/middle into top
    for value in (edgeList): #This is a unique list found in _edgeList
        if value == cubeLocation:
            #Unique Algorithm Goes Here
            edgeSolutionSet = moveToTopAlgo(encodedCube,solution,cubeLocation)
            result['cube'] = edgeSolutionSet.get('cube')
            result['solution'] = edgeSolutionSet.get('solution')
            result['cubeLocation'] = edgeSolutionSet.get('cubeLocation')

    solution = result['solution']
    encodedCube = result['cube']
    cubeLocation = result['cubeLocation']

    #Rotate into correct top spot
    difference = (cubeLocation - correctLocation)
    movementList = _moveTopByDifference(difference)

    movementListMethod(encodedCube, result, movementList)
        
    result['cubeLocation'] = correctLocation
    
    return result

def _setBottomOrTopResult(encodedCube, solution, result, cubeLctn, edge, edgeList, moveToTopAlgo):
    '''variable setter method that calls on _solveEdges'''
    methodResult = _solveEdges(encodedCube, solution, cubeLctn, edge, edgeList, moveToTopAlgo)
    result['solution'] = methodResult.get('solution')
    result['cube'] = methodResult.get('cube')
    result['cubeLocation'] = methodResult.get('cubeLocation')

    solution = result['solution']
    encodedCube = result['cube']
    cubeLctn = result['cubeLocation']
    
    return encodedCube, solution, cubeLctn

def _setTopResult(encodedCube, solution, result, colorMarker, cubeLctn, topToEdgeAlgo):
    '''variable setter method that calls on _topToBottomEdgeAlgoritm or _topToMiddleAlgorithm'''
    topResult = topToEdgeAlgo(encodedCube, solution, cubeLctn, colorMarker)
    result['solution'] = topResult.get('solution')
    result['cube'] = topResult.get('cube')

    solution = result['solution']
    encodedCube = result['cube']
    return encodedCube, solution

def _setMarker(encodedCube,edge1,edge2, center):
    '''variable setter method that sets colorMarkers which
    helps to determine orientation of cube to solve Bottom / Middle Edges'''
    if encodedCube[edge1] == encodedCube[center]: 
        colorMarker = 1
        
    elif encodedCube[edge2] == encodedCube[center]: 
        colorMarker = 2
        
    else:
        colorMarker = 0
        
    return colorMarker

"""
#########################################        
########### Solving Top Cross ###########
#########################################
"""
#Check for (and solve) Top Cross
def _solveTopCross(encodedCube, solution):
    result = argsResult(encodedCube, solution)
    
    if (encodedCube[TOP_UPPER_MIDDLE] == encodedCube[TOP_PORT] == encodedCube[TOP_LOWER_MIDDLE] == encodedCube[TOP_STBD] == encodedCube[TOP_CENTER]):
        return result
    
    else:
        result =  _checkForTopBar(encodedCube, solution)
      
    return result
    
#Check for bar
def _checkForTopBar(encodedCube, solution):
    result = argsResult(encodedCube, solution)
    
    #Horizontal Bar
    if (encodedCube[TOP_PORT] == encodedCube[TOP_STBD] == encodedCube[TOP_CENTER]):
        result = _topAlgorithms(encodedCube, solution, 5)
        
    #Vertical Bar
    elif (encodedCube[TOP_UPPER_MIDDLE] == encodedCube[TOP_LOWER_MIDDLE] == encodedCube[TOP_CENTER]):
        result = _topAlgorithms(encodedCube, solution, 6)
        
    else:
        #Check for Arm or single cube
        result = _checkForTopArm(encodedCube, solution)
    
    return result
        
#Check for arm
def _checkForTopArm(encodedCube, solution):
    result = argsResult(encodedCube, solution)
    flag = SINGLE_CUBE #Single Cube Case
    
    #Lower Left Arm
    if (encodedCube[TOP_PORT] == encodedCube[TOP_LOWER_MIDDLE] == encodedCube[TOP_CENTER]):
        flag = ARM_LOWER_LEFT
    
    #Lower Right Arm
    elif (encodedCube[TOP_STBD] == encodedCube[TOP_LOWER_MIDDLE] == encodedCube[TOP_CENTER]):
        flag = ARM_LOWER_RIGHT
        
    #Upper Right Arm
    elif (encodedCube[TOP_UPPER_MIDDLE] == encodedCube[TOP_STBD] == encodedCube[TOP_CENTER]):
        flag = ARM_UPPER_RIGHT
        
    #Upper Left Arm (desired)
    elif (encodedCube[TOP_UPPER_MIDDLE] == encodedCube[TOP_PORT] == encodedCube[TOP_CENTER]):
        flag = ARM_UPPER_LEFT
        
    if flag == SINGLE_CUBE: #This is recursive.. that is scary.. 

        result = _topAlgorithms(encodedCube, solution, flag)
        
        result = _checkForTopArm(result['cube'], result['solution'])
        return result
        
    result = _topAlgorithms(result['cube'], result['solution'], flag)
    
    return result
        
#Top Cross Algorithms
def _topAlgorithms(encodedCube, solution, flag):
    result = argsResult(encodedCube, solution)
    movementList = ''
    
    if flag == ARM_LOWER_LEFT: #Bottom Left Arm
        movementList = 'U' #Now Left Arm
        flag = ARM_UPPER_LEFT
        
    elif flag == ARM_LOWER_RIGHT: #Bottom Right Arm
        movementList = 'UU' #Now Left Arm
        flag = ARM_UPPER_LEFT

    elif flag == ARM_UPPER_RIGHT: #Upper Right Arm
        movementList = 'u' #Now Left Arm
        flag = ARM_UPPER_LEFT
        
    if flag == ARM_UPPER_LEFT: # Upper Left Arm
        flag = HORITZONAL_BAR
        movementList = movementList + 'FRUruf' #Now a Horizontal Bar    

    if flag == HORITZONAL_BAR or flag == SINGLE_CUBE: #Horizontal Bar (or single cube)
        movementList = movementList + 'FRUruf' #Now a Top Cross (or an arm in the case of single cube)
        
    elif flag == VERTICAL_BAR: #Vertical Bar
        movementList = 'UFRUruf'
        
    movementListMethod(encodedCube, result, movementList)

    return result

"""
########################################        
########### Solving Top Face ###########
########################################
"""

def _solveTopFace(encodedCube, solution):
    result = argsResult(encodedCube, solution)
    movementList = ''
    corners, flag = _countCorners(result['cube'])
    while corners <=3: 
        
        #None case
        if flag == 'noCorners':
            movementList = _topFaceMovementCases(encodedCube, LEFT_UPPER_PORT_EDGE,FRONT_UPPER_PORT_EDGE,RIGHT_UPPER_PORT_EDGE,BACK_UPPER_PORT_EDGE)
                
        #One case
        elif flag == 'fish':
            movementList = _topFaceMovementCases(encodedCube, TOP_LOWER_PORT_EDGE,TOP_LOWER_STBD_EDGE,TOP_UPPER_STBD_EDGE,TOP_UPPER_PORT_EDGE)
        
        #Two Case
        elif flag == 'doubleCorners':         
            movementList = _topFaceMovementCases(encodedCube, FRONT_UPPER_PORT_EDGE,RIGHT_UPPER_PORT_EDGE, BACK_UPPER_PORT_EDGE,LEFT_UPPER_PORT_EDGE)
        
        movementList = movementList + 'RUrURUUr'
        
        #This is a unique movementList (NOT THE SHARED METHOD!)
        for letter in movementList:
            result['solution'], result['cube'] =  _functionalRotations(result['cube'], result, letter)
            encodedCube = result['cube']
        
        #SETS FOR NEXT ITERATION
        movementList = '' #reset
        flag = '' #reset
        corners, flag = _countCorners(encodedCube) #recount and find orientation
        
    return result

def _topFaceMovementCases(encodedCube, base, pos, neg, dbl):
    if encodedCube[base] == encodedCube[TOP_CENTER]:
        movementList = ''
    elif encodedCube[pos] == encodedCube[TOP_CENTER]:
        movementList = 'U'
    elif encodedCube[neg] == encodedCube[TOP_CENTER]:
        movementList = 'UU'
    elif encodedCube[dbl] == encodedCube[TOP_CENTER]:
        movementList = 'u'
    return movementList

def _countCorners(encodedCube):
    corners = 0
    flag = 1 #no corners case
    
    if encodedCube[TOP_LOWER_PORT_EDGE] == encodedCube[TOP_CENTER]:
        corners += corners + 1
        flag = flag * 2 #2
        
    if encodedCube[TOP_LOWER_STBD_EDGE] == encodedCube[TOP_CENTER]:
        corners += corners + 1
        flag = flag * 3 #3 or 6
        
    if encodedCube[TOP_UPPER_STBD_EDGE] == encodedCube[TOP_CENTER]:
        corners += corners + 1
        flag = flag * 4 #4 or 8 or 12
        
    if encodedCube[TOP_UPPER_PORT_EDGE] == encodedCube[TOP_CENTER]:
        corners += corners + 1
        flag = flag * 5 #5 or 10 or 15 or 20
        
    if flag == 1:
        flag = 'noCorners'
        
    elif (flag == 2 or flag == 3 or flag == 4 or flag == 5):
        flag = 'fish'
        
    else: 
        flag = 'doubleCorners'
        
    return corners, flag

"""
###########################################        
########### Solving Top Corners ###########
###########################################
"""

def _solveTopCorners(encodedCube, solution):
    result = argsResult(encodedCube, solution)
    movementList = ''
    flag = ''
    
    while flag != "quad":
        flag, hornColor, hornLocation = _countHorns(result['cube'])
        
        if flag == 'none':
            movementList = 'rFrBBRfrBBRRUrFrBBRfrBBRR'
        
        elif flag == 'single':

            movementList = _moveHornsToBack(encodedCube, hornColor, hornLocation)
            movementList = movementList + 'rFrBBRfrBBRRu'
            
        encodedCube = movementListMethod(encodedCube, result, movementList)
                
        flag, hornColor, hornLocation = _countHorns(result['cube'])

    movementList = _moveHornsToFinal(encodedCube, hornColor, hornLocation)
    
    encodedCube = movementListMethod(encodedCube, result, movementList)
            
    return result

def _countHorns(encodedCube):
    horns = 0
    hornColor = None
    hornLocation = None
    
    if encodedCube[FRONT_UPPER_PORT_EDGE] == encodedCube[FRONT_UPPER_STBD_EDGE]:
        horns = horns + 1
        hornColor = encodedCube[FRONT_UPPER_STBD_EDGE]
        hornLocation = FRONT
        
    if encodedCube[RIGHT_UPPER_PORT_EDGE] == encodedCube[RIGHT_UPPER_STBD_EDGE]:
        horns = horns + 1
        hornColor = encodedCube[RIGHT_UPPER_STBD_EDGE]
        hornLocation = RIGHT
        
    if encodedCube[BACK_UPPER_PORT_EDGE] == encodedCube[BACK_UPPER_STBD_EDGE]:
        horns = horns + 1
        hornColor = encodedCube[BACK_UPPER_STBD_EDGE]
        hornLocation = BACK
        
    if encodedCube[LEFT_UPPER_PORT_EDGE] == encodedCube[LEFT_UPPER_STBD_EDGE]:
        horns = horns + 1
        hornColor = encodedCube[LEFT_UPPER_STBD_EDGE]
        hornLocation = LEFT
    
    if horns == 0:
            flag = 'none'
            
    elif horns == 1:
            flag = 'single'
            
    elif horns == 4:
            flag = 'quad'
            
    return flag, hornColor, hornLocation

    
def _moveHornsToBack(encodedCube, hornColor, hornLocation): 
    # if 0 on back, if -2 UU, if 1 U, if -1 u
    movementList = ''
    
    if hornColor == encodedCube[FRONT_CENTER]:
        difference = hornLocation - BACK
        
    if hornColor == encodedCube[RIGHT_CENTER]:
        difference = hornLocation - BACK
    
    if hornColor == encodedCube[BACK_CENTER]:
        difference = hornLocation - BACK
        
    if hornColor == encodedCube[LEFT_CENTER]:
        difference = hornLocation - BACK
    
    if difference == 1:
        movementList = 'U'
        
    elif difference == -1:
        movementList = 'u'
        
    elif difference == -2:
        movementList = 'UU'
        
    return movementList

def _moveHornsToFinal(encodedCube, hornColor, hornLocation): 
    #This finds where a matching edge is and returns the difference. 0 is correct, -1/3 needs a u, -3/1 needs a U
    movementList = ''
    
    if hornColor == encodedCube[FRONT_CENTER]:
        location = FRONT
        difference = location - hornLocation
        
    if hornColor == encodedCube[RIGHT_CENTER]:
        location = RIGHT
        difference = location - hornLocation
    
    if hornColor == encodedCube[BACK_CENTER]:
        location = BACK
        difference = location - hornLocation
        
    if hornColor == encodedCube[LEFT_CENTER]:
        location = LEFT
        difference = location - hornLocation
        
    if (difference == 1 or difference == -3):
        movementList = 'u'
        
    elif (difference == -1 or difference == 3):
        movementList = 'U'
        
    elif difference == -2:
        movementList = 'UU'
    
    return movementList   

"""
###########################################        
############ Solving Top Edges ############
###########################################
"""

def _faceCheck(encodedCube):
    foundFaces = 0
    location = None
    
    #Technically after the 'and' is redundant from 6a, but this eliminates inherent risk. Can remove if desired. 
    if (encodedCube[FRONT_UPPER_MIDDLE] == encodedCube[FRONT_UPPER_PORT_EDGE] and encodedCube[FRONT_UPPER_PORT_EDGE] == encodedCube[FRONT_UPPER_STBD_EDGE]):
        foundFaces = foundFaces + 1
        location = FRONT
        
    if (encodedCube[RIGHT_UPPER_MIDDLE] == encodedCube[RIGHT_UPPER_PORT_EDGE] and encodedCube[RIGHT_UPPER_PORT_EDGE] == encodedCube[RIGHT_UPPER_STBD_EDGE]):

        foundFaces = foundFaces + 1
        location =  RIGHT
        
    if (encodedCube[BACK_UPPER_MIDDLE] == encodedCube[BACK_UPPER_PORT_EDGE] and encodedCube[BACK_UPPER_PORT_EDGE] == encodedCube[BACK_UPPER_STBD_EDGE]):
        foundFaces = foundFaces + 1
        location = BACK
        
    if (encodedCube[LEFT_UPPER_MIDDLE] == encodedCube[LEFT_UPPER_PORT_EDGE] and encodedCube[LEFT_UPPER_PORT_EDGE] == encodedCube[LEFT_UPPER_STBD_EDGE]):
        foundFaces = foundFaces + 1
        location = LEFT

    return foundFaces, location

def _rotateTopRowToBack(location):
    movementList = ''

    if location == FRONT:
        movementList = 'UU'
        
    elif location == RIGHT:

        movementList = 'u'
        
    elif location == BACK:
        movementList = ''
        
    elif location == LEFT:
        movementList = 'U'
            
    return movementList


"""
##############################################################       
############ Shared Function for Result{} setting ############
############################################################## 
"""
def argsResult(encodedCube, solution):
    result = {}
    result['cube'] = encodedCube
    result['solution'] = solution
    return result

"""
##############################################################       
############## Shared Function for movementList ##############
############################################################## 
"""

def movementListMethod(encodedCube, result, movementList):
    for letter in movementList:
        result['solution'], result['cube'] = _functionalRotations(encodedCube, result, letter)
        encodedCube = result['cube']
    
    return encodedCube
        
"""
####################################################################################        
############ Rotation Function and Updates to Cube and Solution String ############
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
    rotatedCubeList = Direct_result.get('cube')

    return result['solution'], rotatedCubeList

"""
#############################################################        
############## Unidirectional Rotation Methods ##############
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
    rotatedCubeList[FRONT_UPPER_PORT_EDGE]  = cubeList[FRONT_UPPER_STBD_EDGE]
    rotatedCubeList[FRONT_UPPER_MIDDLE]     = cubeList[FRONT_STBD]
    rotatedCubeList[FRONT_UPPER_STBD_EDGE]  = cubeList[FRONT_LOWER_STBD_EDGE]
    rotatedCubeList[FRONT_PORT]             = cubeList[FRONT_UPPER_MIDDLE]
    rotatedCubeList[FRONT_CENTER]           = cubeList[FRONT_CENTER]
    rotatedCubeList[FRONT_STBD]             = cubeList[FRONT_LOWER_MIDDLE]
    rotatedCubeList[FRONT_LOWER_PORT_EDGE]  = cubeList[FRONT_UPPER_PORT_EDGE]
    rotatedCubeList[FRONT_LOWER_MIDDLE]     = cubeList[FRONT_PORT]
    rotatedCubeList[FRONT_LOWER_STBD_EDGE]  = cubeList[FRONT_LOWER_PORT_EDGE]

    #rotate right to top
    rotatedCubeList[TOP_LOWER_PORT_EDGE]    = cubeList[RIGHT_UPPER_PORT_EDGE]
    rotatedCubeList[TOP_LOWER_MIDDLE]       = cubeList[RIGHT_PORT]
    rotatedCubeList[TOP_LOWER_STBD_EDGE]    = cubeList[RIGHT_LOWER_PORT_EDGE]

    #rotate bottom to right
    rotatedCubeList[RIGHT_UPPER_PORT_EDGE]  = cubeList[BOTTOM_UPPER_STBD_EDGE]
    rotatedCubeList[RIGHT_PORT]             = cubeList[BOTTOM_UPPER_MIDDLE]
    rotatedCubeList[RIGHT_LOWER_PORT_EDGE]  = cubeList[BOTTOM_UPPER_PORT_EDGE]

    #rotate left to bottom
    rotatedCubeList[BOTTOM_UPPER_PORT_EDGE] = cubeList[LEFT_UPPER_STBD_EDGE]
    rotatedCubeList[BOTTOM_UPPER_MIDDLE]    = cubeList[LEFT_STBD]
    rotatedCubeList[BOTTOM_UPPER_STBD_EDGE] = cubeList[LEFT_LOWER_STBD_EDGE]

    #rotate top to left
    rotatedCubeList[LEFT_UPPER_STBD_EDGE]   = cubeList[TOP_LOWER_STBD_EDGE]
    rotatedCubeList[LEFT_STBD]              = cubeList[TOP_LOWER_MIDDLE]
    rotatedCubeList[LEFT_LOWER_STBD_EDGE]   = cubeList[TOP_LOWER_PORT_EDGE]

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
