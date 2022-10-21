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

#INDIVIDUAL MIDDLES
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

#INDIVIDUAL SIDES
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

#3D EDGES
TOP_UPR_L_EDGE = {'Value': 3}
TOP_UPR_R_EDGE = {'Value': 2}
TOP_LWR_L_EDGE = {'Value': 4}  
TOP_LWR_R_EDGE = {'Value': 1}

BTTM_UPR_L_EDGE = {'Value': 7}
BTTM_UPR_R_EDGE = {'Value': 6}
BTTM_LWR_L_EDGE = {'Value': 8}  
BTTM_LWR_R_EDGE = {'Value': 5}


"""
#############################################################        
############### Main Method For Solving Cube ################
#############################################################
"""
def _solve(parms):
    """ Returns the solutions needed to solve a cube and the status of input. """
    result = {}
    FinalResult = {}
    encodedCube = parms.get('cube',None)
    
    #Verify If Input Is Valid and Return Status
    status = _verifyInput(encodedCube)
    
    #Solve for Bottom Cross and set rotations to the solution.
    if status == 'ok':
        FinalResult = _solveBottomCross(encodedCube) #Iteration 2
        
        FinalResult = _solveBottomFace(FinalResult.get('cube'), FinalResult.get('solution')) #Iteration 3
        
    result['rotations'] = FinalResult.get('solution')
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
    bottomToDaisyResult = {}
    bottomToDaisyResult['solution'] = solution
    bottomToDaisyResult['rotatedCubeList'] = encodedCube
    
    while encodedCube[bottomPetalIndex] == encodedCube[topPetalIndex]:
        bottomToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, bottomToDaisyResult, 'U')

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
            bottomToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, bottomToDaisyResult, char) 
        
        bottomToDaisyResult['rotatedCubeList'] = encodedCube
    return bottomToDaisyResult

def _horizontalCubesToDaisy(horizontalPetalIndex: int, topPetalIndex: int, solution, encodedCube):
    """ Moves horizontal pieces to top to begin forming a Daisy """
    horizontalToDaisyResult = {}
    horizontalToDaisyResult['solution'] = solution
    horizontalToDaisyResult['rotatedCubeList'] = encodedCube
    
    while encodedCube[horizontalPetalIndex] == encodedCube[topPetalIndex]:
        horizontalToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, horizontalToDaisyResult, 'U')

    if encodedCube[horizontalPetalIndex] != encodedCube[topPetalIndex]:
        
        if horizontalPetalIndex == FRONT_PORT:
            horizontalToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, horizontalToDaisyResult, 'l')
            
        if horizontalPetalIndex == FRONT_STBD:
            horizontalToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, horizontalToDaisyResult, 'R')
            
        if horizontalPetalIndex == RIGHT_PORT:
            horizontalToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, horizontalToDaisyResult, 'f')
            
        if horizontalPetalIndex == RIGHT_STBD:
            horizontalToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, horizontalToDaisyResult, 'B')
            
        if horizontalPetalIndex == BACK_PORT:
            horizontalToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, horizontalToDaisyResult, 'r')
            
        if horizontalPetalIndex == BACK_STBD:
            horizontalToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, horizontalToDaisyResult, 'L')

        if horizontalPetalIndex == LEFT_PORT:
            horizontalToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, horizontalToDaisyResult, 'b')
            
        if horizontalPetalIndex == LEFT_STBD:
            horizontalToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, horizontalToDaisyResult, 'F')
        
        horizontalToDaisyResult['rotatedCubeList'] = encodedCube
    return horizontalToDaisyResult

def _verticalCubesToDaisy(verticalPetalIndex: int, topPetalIndex: int, solution, encodedCube):
    """ Moves vertical pieces to top to begin forming a Daisy """
    veritcalToDaisyResult = {}
    veritcalToDaisyResult['solution'] = solution
    veritcalToDaisyResult['encodedCube'] = encodedCube
    
    while encodedCube[verticalPetalIndex] == encodedCube[topPetalIndex]:
        veritcalToDaisyResult['solution'], encodedCube = _functionalRotations(encodedCube, veritcalToDaisyResult, 'U')

    if encodedCube[verticalPetalIndex] != encodedCube[topPetalIndex]:
        
        if verticalPetalIndex == FRONT_UPPER_MIDDLE:
            encodedCube, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(encodedCube, veritcalToDaisyResult, "lfLDFF")
        
        if verticalPetalIndex == FRONT_LOWER_MIDDLE:
            encodedCube, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(encodedCube, veritcalToDaisyResult, "FFlfLDFF")
    
        if verticalPetalIndex == RIGHT_UPPER_MIDDLE:
            encodedCube, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(encodedCube, veritcalToDaisyResult, "frFDRR")
    
        if verticalPetalIndex == RIGHT_LOWER_MIDDLE:
            encodedCube, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(encodedCube, veritcalToDaisyResult, "RRfrFDRR")

        if verticalPetalIndex == BACK_UPPER_MIDDLE:
            encodedCube, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(encodedCube, veritcalToDaisyResult, "rbRDBB")
        
        if verticalPetalIndex == BACK_LOWER_MIDDLE:
            encodedCube, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(encodedCube, veritcalToDaisyResult, "BBrbRDBB")
            
        if verticalPetalIndex == LEFT_UPPER_MIDDLE: 
            encodedCube, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(encodedCube, veritcalToDaisyResult, "blBDLL")
            
        if verticalPetalIndex == LEFT_LOWER_MIDDLE:
            encodedCube, veritcalToDaisyResult['solution'] = _verticalCubeIntoDaisy(encodedCube, veritcalToDaisyResult, "LLblBDLL")
        
        veritcalToDaisyResult['rotatedCubeList'] = encodedCube
    return veritcalToDaisyResult

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
    daisyResult = {}
    daisyResult['solution'] = solution
    daisyResult['daisyCubeList'] = encodedCube
    
    while (encodedCube[uniqueCenter]!= encodedCube[topMiddle] or encodedCube[adjacentDaisy] != encodedCube[BOTTOM_CENTER]):
        
        daisyResult['solution'], encodedCube  = _functionalRotations(encodedCube, daisyResult, 'U')
        
    daisyResult['daisyCubeList'] = encodedCube
    return daisyResult
  
def _daisy_Rotations(uniqueCenter: int, topMiddle: int, encodedCube, solution):
    """ Sub-method for Integrated Daisy Method. Rotates the block a specific direction depending on its uniqueCenter. """
    daisyRotResult = {}
    daisyRotResult['solution'] = solution
    daisyRotResult['daisyCubeList'] = encodedCube
    
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
            daisyRotResult['solution'], encodedCube = _functionalRotations(encodedCube, daisyRotResult, char)
            
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
        numberOfPetalsFound, encodedCube, result = _moveEachBottomCubeToDaisy(result, encodedCube, numberOfPetalsFound, BOTTOM_UPPER_MIDDLE, TOP_LOWER_MIDDLE)
#Checking Left of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachBottomCubeToDaisy(result, encodedCube, numberOfPetalsFound, BOTTOM_PORT, TOP_PORT)
#Checking Right of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachBottomCubeToDaisy(result, encodedCube, numberOfPetalsFound, BOTTOM_STBD, TOP_STBD)
#Checking Bottom of Bottom Face
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachBottomCubeToDaisy(result, encodedCube, numberOfPetalsFound, BOTTOM_LOWER_MIDDLE, TOP_UPPER_MIDDLE)

    return numberOfPetalsFound, encodedCube

def _moveEachBottomCubeToDaisy(result, encodedCube, numberOfPetalsFound, cubeOne, cubeTwo):
    if encodedCube[cubeOne] == encodedCube[BOTTOM_CENTER]:
        bottomToDaisyResult = _unalignedBottomToDaisy(cubeOne, cubeTwo, result['solution'], encodedCube)
        result['solution'] = bottomToDaisyResult.get('solution')
        encodedCube = bottomToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, encodedCube, result

""" Horizontal Moves """
def _moveHorizontalCubesToDaisy(result, encodedCube, numberOfPetalsFound):
#Check Front Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachFrontCubeToDaisy(result, encodedCube, numberOfPetalsFound, FRONT_PORT, TOP_PORT)
#Check Front Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachFrontCubeToDaisy(result, encodedCube, numberOfPetalsFound, FRONT_STBD, TOP_STBD)
#Check Right Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachFrontCubeToDaisy(result, encodedCube, numberOfPetalsFound, RIGHT_PORT, TOP_LOWER_MIDDLE)
#Check Right Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachFrontCubeToDaisy(result, encodedCube, numberOfPetalsFound, RIGHT_STBD, TOP_UPPER_MIDDLE)
#Check Back Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachFrontCubeToDaisy(result, encodedCube, numberOfPetalsFound, BACK_PORT, TOP_STBD)
#Check Back Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachFrontCubeToDaisy(result, encodedCube, numberOfPetalsFound, BACK_STBD, TOP_PORT)
#Check Left Face (Left Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachFrontCubeToDaisy(result, encodedCube, numberOfPetalsFound, LEFT_PORT, TOP_UPPER_MIDDLE)
#Check Left Face (Right Side Piece)
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachFrontCubeToDaisy(result, encodedCube, numberOfPetalsFound, LEFT_STBD, TOP_LOWER_MIDDLE)
  
    return numberOfPetalsFound, encodedCube

def _moveEachFrontCubeToDaisy(result, encodedCube, numberOfPetalsFound, cubeOne, cubeTwo):
    if encodedCube[cubeOne] == encodedCube[BOTTOM_CENTER]:
        horizontalToDaisyResult = _horizontalCubesToDaisy(cubeOne, cubeTwo, result['solution'], encodedCube)
        result['solution'] = horizontalToDaisyResult.get('solution')
        encodedCube = horizontalToDaisyResult.get('rotatedCubeList')
        numberOfPetalsFound += 1
    return numberOfPetalsFound, encodedCube, result

""" Vertical Moves """
def _moveVerticalCubesToDaisy(result, encodedCube, numberOfPetalsFound):
#Front Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachVerticalCubeToDaisy(result, encodedCube, numberOfPetalsFound, FRONT_UPPER_MIDDLE, TOP_LOWER_MIDDLE)
        #numberOfPetalsFound, encodedCube, result = _moveFrontUpperVerticalCubeToDaisy(result, encodedCube, numberOfPetalsFound)
#Front Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachVerticalCubeToDaisy(result, encodedCube, numberOfPetalsFound, FRONT_LOWER_MIDDLE, TOP_LOWER_MIDDLE)
#Right Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachVerticalCubeToDaisy(result, encodedCube, numberOfPetalsFound, RIGHT_UPPER_MIDDLE, TOP_STBD)
#Right Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachVerticalCubeToDaisy(result, encodedCube, numberOfPetalsFound, RIGHT_LOWER_MIDDLE, TOP_STBD)
# Back Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachVerticalCubeToDaisy(result, encodedCube, numberOfPetalsFound, BACK_UPPER_MIDDLE, TOP_UPPER_MIDDLE)
# Back Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachVerticalCubeToDaisy(result, encodedCube, numberOfPetalsFound, BACK_LOWER_MIDDLE, TOP_UPPER_MIDDLE)
#Left Face Vertical Top
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachVerticalCubeToDaisy(result, encodedCube, numberOfPetalsFound, LEFT_UPPER_MIDDLE, TOP_PORT)
#Left Face Vertical Bottom
    if (numberOfPetalsFound <= 3):
        numberOfPetalsFound, encodedCube, result = _moveEachVerticalCubeToDaisy(result, encodedCube, numberOfPetalsFound, LEFT_LOWER_MIDDLE, TOP_PORT)
        
    return numberOfPetalsFound, encodedCube

def _moveEachVerticalCubeToDaisy(result, encodedCube, numberOfPetalsFound, cubeOne, cubeTwo):
    if encodedCube[cubeOne] == encodedCube[BOTTOM_CENTER]:
        verticalToDaisyResult = _verticalCubesToDaisy(cubeOne, cubeTwo, result['solution'], encodedCube)
        result['solution'] = verticalToDaisyResult.get('solution')
        encodedCube = verticalToDaisyResult.get('rotatedCubeList')
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
####################################        
########### Bottom Edges ###########
####################################
"""
def _solveBottomFace(encodedCube, solution):
    '''Main method for solving the bottom edges (post bottom cross)'''
    #This will likely need to have the solution passed as an argument. 
    result = {}

#FIRST WILL SOLVE BOTTOM UPPER RIGHT CORNER (6). Find cube with desired colors. 
    cubeLctn = _findBottomEdge(encodedCube, BOTTOM_CENTER, FRONT_CENTER, RIGHT_CENTER) # <- UNIQUE
    
    #IF CUBE IN CORRECT SPOT AND ORIENTED CORRECTLY, GO TO NEXT SPOT
    if (cubeLctn == BTTM_UPR_R_EDGE['Value'] and encodedCube[BOTTOM_UPPER_STBD_EDGE] == encodedCube[BOTTOM_CENTER]):
        cubeLctn = _findBottomEdge(encodedCube, BOTTOM_CENTER, RIGHT_CENTER, BACK_CENTER)
 
    else:
        cubeLctn, encodedCube, solution = _unalighedBottomEdge(encodedCube, solution, result, cubeLctn, 
                                                                            TOP_LWR_R_EDGE['Value'], TOP_LOWER_STBD_EDGE, FRONT_UPPER_STBD_EDGE, BOTTOM_CENTER, RIGHT_CENTER, BACK_CENTER)

#SECOND WILL SOLVE BOTTOM LOWER RIGHT CORNER (7)
    if (cubeLctn == BTTM_LWR_R_EDGE['Value'] and encodedCube[BOTTOM_LOWER_STBD_EDGE] == encodedCube[BOTTOM_CENTER]):
        cubeLctn = _findBottomEdge(encodedCube, BOTTOM_CENTER, BACK_CENTER, LEFT_CENTER)
    
    else:
        cubeLctn, encodedCube, solution = _unalighedBottomEdge(encodedCube, solution, result, cubeLctn, 
                                                                            TOP_UPR_R_EDGE['Value'], TOP_UPPER_STBD_EDGE, RIGHT_UPPER_STBD_EDGE, BOTTOM_CENTER, BACK_CENTER, LEFT_CENTER)
        
#THIRD WILL SOLVE BOTTOM LOWER LEFT CORNER (8)    
    if (cubeLctn == BTTM_LWR_L_EDGE['Value'] and encodedCube[BOTTOM_LOWER_PORT_EDGE] == encodedCube[BOTTOM_CENTER]):
        cubeLctn = _findBottomEdge(encodedCube, BOTTOM_CENTER, LEFT_CENTER, FRONT_CENTER)
    
    else:
        cubeLctn, encodedCube, solution = _unalighedBottomEdge(encodedCube, solution, result, cubeLctn, 
                                                                            TOP_UPR_L_EDGE['Value'], TOP_UPPER_PORT_EDGE, BACK_UPPER_STBD_EDGE, BOTTOM_CENTER, LEFT_CENTER, FRONT_CENTER)

#FINALLY WILL SOLVE BOTTOM UPPER LEFT CORNER (5)
    if (cubeLctn == BTTM_UPR_L_EDGE['Value'] and encodedCube[BOTTOM_UPPER_PORT_EDGE] == encodedCube[BOTTOM_CENTER]):
        result['cube'], result['solution'] = encodedCube, solution # Runs this because its the final check..                    
     
    else:
        cubeLctn, encodedCube, solution = _unalighedBottomEdge(encodedCube, solution, result, cubeLctn, 
                                                                            TOP_LWR_L_EDGE['Value'], TOP_LOWER_PORT_EDGE, LEFT_UPPER_STBD_EDGE, None, None, None)
    
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
    result = {}
    result['solution'] = solution
    result['cube'] = encodedCube
    movementList = ''
    
    if cubeLctn == TOP_LWR_L_EDGE['Value']: #4
        if colorMarker == 1:
            movementList = 'luuLUluLU' #Valid for test 302
        elif colorMarker == 2:
            movementList = 'luLU'   
        else:
            movementList = 'ulUL' #Valid for test 306
            
    if cubeLctn == TOP_LWR_R_EDGE['Value']: #3
        if colorMarker == 1:
            movementList = 'fuuFUfuFU' #Valid for test 303
        elif colorMarker == 2:
            movementList = 'fuFU'
        else:
            movementList = 'ufUF' #Valid for test 307
    
    if cubeLctn == TOP_UPR_R_EDGE['Value']: #2
        if colorMarker == 1:
            movementList = 'ruuRUruRU' #Valid for test 304
        elif colorMarker == 2:
            movementList = 'ruRU' 
        else:
            movementList = 'urUR' #Valid for test 308
        
    if cubeLctn == TOP_UPR_L_EDGE['Value']: #1
        if colorMarker == 1:
            movementList = 'buuBUbuBU' #Valid for test 305
        elif colorMarker == 2:
            movementList = 'buBU'   
        else:
            movementList = 'ubUB' #Valid for test 309
            
    for letter in movementList:
        result['solution'], result['cube'] = _functionalRotations(encodedCube, result, letter)
        encodedCube = result['cube']
    
    return result

def _moveBottomEdgeToTopEdge(encodedCube, solution, cubeLocation):     
    '''Based on cube location, rotate bottom edge to top edge'''              
    result = {}
    result['cube'] = encodedCube
    result['solution'] = solution
    movementList = ""
    value = cubeLocation
    
    #These four if statements direct movement of edge from bottom to top 
    if value == BTTM_LWR_R_EDGE['Value']: #7
        movementList = 'ruRU' 
        cubeLocation = TOP_UPR_R_EDGE['Value'] #2

    if value == BTTM_LWR_L_EDGE['Value']: #8
        movementList = 'buBU'
        cubeLocation = TOP_UPR_L_EDGE['Value'] #1

    if value == BTTM_UPR_L_EDGE['Value']: #5
        movementList = 'luLU'
        cubeLocation = TOP_LWR_L_EDGE['Value'] #4

    if value == BTTM_UPR_R_EDGE['Value']: #6
        movementList = 'fuFU' 
        cubeLocation = TOP_LWR_R_EDGE['Value'] #3
    
    for letter in movementList:
        result['solution'], result['cube'] = _functionalRotations(encodedCube, result, letter)
        encodedCube = result['cube']
    
    result['cubeLocation'] = cubeLocation
    return result

def _findBottomEdge(encodedCube, zCube, yCube, xCube):
    '''This method finds the correct edge based on x,y,z cube colors and returns 1 of 8 edge locations'''
    rcl = encodedCube # This is just for ease of typing
    triangulatedBottomEdge = {rcl[zCube], rcl[yCube], rcl[xCube]}

    #EDGES WITH TOP THEN SIDE AND THEN FACE (Ordered, for orientation with bottom)
    TOP_UPR_L_EDGE = {'Value': 3, 'Colors': {rcl[TOP_UPPER_PORT_EDGE], rcl[LEFT_UPPER_PORT_EDGE], rcl[BACK_UPPER_STBD_EDGE]}}
    TOP_UPR_R_EDGE = {'Value': 2, 'Colors': {rcl[TOP_UPPER_STBD_EDGE], rcl[BACK_UPPER_PORT_EDGE], rcl[RIGHT_UPPER_STBD_EDGE]}}
    TOP_LWR_L_EDGE = {'Value': 4, 'Colors': {rcl[TOP_LOWER_PORT_EDGE], rcl[FRONT_UPPER_PORT_EDGE], rcl[LEFT_UPPER_STBD_EDGE]}}
    TOP_LWR_R_EDGE = {'Value': 1, 'Colors': {rcl[TOP_LOWER_STBD_EDGE], rcl[RIGHT_UPPER_PORT_EDGE], rcl[FRONT_UPPER_STBD_EDGE]}}

    #EDGES WITH BOTTOM THEN FACE AND THEN SIDE (Ordered)
    BTTM_UPR_L_EDGE = {'Value': 7, 'Colors': {rcl[BOTTOM_UPPER_PORT_EDGE], rcl[FRONT_LOWER_PORT_EDGE], rcl[LEFT_LOWER_STBD_EDGE]}}
    BTTM_UPR_R_EDGE = {'Value': 6, 'Colors': {rcl[BOTTOM_UPPER_STBD_EDGE], rcl[RIGHT_LOWER_PORT_EDGE], rcl[FRONT_LOWER_STBD_EDGE]}}
    BTTM_LWR_L_EDGE = {'Value': 8, 'Colors': {rcl[BOTTOM_LOWER_PORT_EDGE], rcl[LEFT_LOWER_PORT_EDGE], rcl[BACK_LOWER_STBD_EDGE]}}  
    BTTM_LWR_R_EDGE = {'Value': 5, 'Colors': {rcl[BOTTOM_LOWER_STBD_EDGE], rcl[BACK_LOWER_PORT_EDGE], rcl[RIGHT_LOWER_STBD_EDGE]}}

    EdgeList = (TOP_UPR_L_EDGE, TOP_UPR_R_EDGE, TOP_LWR_L_EDGE, TOP_LWR_R_EDGE, BTTM_LWR_L_EDGE, BTTM_LWR_R_EDGE, BTTM_UPR_L_EDGE, BTTM_UPR_R_EDGE)

    EdgeNumber = 0

    while EdgeNumber < 8:
        if (triangulatedBottomEdge != EdgeList[EdgeNumber]['Colors']):
            EdgeNumber += 1

        else:
            return EdgeList[EdgeNumber]['Value']

"""
####################################        
########### Middle Edges ###########
####################################
"""
def _findMiddleEdge(encodedCube, yCube, xCube):
    '''This method finds the correct edge based on x,y,z cube colors and returns 1 of 8 edge locations'''
    rcl = encodedCube # This is just for ease of typing
    triangulatedMiddleEdge = {rcl[yCube], rcl[xCube]}

    #EDGES WITH TOP THEN SIDE AND THEN FACE (Ordered, for orientation with bottom)
    TOP_FRONT_SIDE = {'Value': 1, 'Colors': {rcl[TOP_LOWER_MIDDLE], rcl[FRONT_UPPER_MIDDLE]}}
    TOP_RIGHT_SIDE = {'Value': 2, 'Colors': {rcl[TOP_STBD], rcl[RIGHT_UPPER_MIDDLE]}}
    TOP_BACK_SIDE = {'Value': 3, 'Colors': {rcl[TOP_UPPER_MIDDLE], rcl[BACK_UPPER_MIDDLE]}}
    TOP_LEFT_SIDE = {'Value': 4, 'Colors': {rcl[TOP_PORT], rcl[LEFT_UPPER_MIDDLE]}}

    #EDGES WITH BOTTOM THEN FACE AND THEN SIDE (Ordered)
    MIDL_FRONT_EDGE = {'Value': 5, 'Colors': {rcl[FRONT_STBD], rcl[RIGHT_PORT]}}
    MIDL_RIGHT_EDGE = {'Value': 6, 'Colors': {rcl[RIGHT_STBD], rcl[BACK_PORT]}}
    MIDL_BACK_EDGE = {'Value': 7, 'Colors': {rcl[BACK_STBD], rcl[LEFT_PORT]}}
    MIDL_LEFT_EDGE = {'Value': 8, 'Colors': {rcl[LEFT_STBD], rcl[FRONT_PORT]}}

    edgeList = (TOP_FRONT_SIDE, TOP_RIGHT_SIDE, TOP_BACK_SIDE, TOP_LEFT_SIDE, MIDL_FRONT_EDGE, MIDL_RIGHT_EDGE, MIDL_BACK_EDGE, MIDL_LEFT_EDGE)

    edgeNumber = 0

    while edgeNumber < 8:
        if (triangulatedMiddleEdge != edgeList[edgeNumber]['Colors']):
            edgeNumber += 1

        else:
            return edgeList[edgeNumber]['Value']


"""
##################################################################        
########### Shared Methods for Bottom and Middle Edges ###########
##################################################################
"""
def _edgeList(location):

    if (location == 'Bottom'):
        return BTTM_UPR_L_EDGE['Value'], BTTM_UPR_R_EDGE['Value'], BTTM_LWR_L_EDGE['Value'], BTTM_LWR_R_EDGE['Value']

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

def _setTopResult(encodedCube, solution, result, colorMarker, cubeLctn, moveTopDownAlgo):
    '''variable setter method that calls on _topToBottomEdgeAlgoritm'''
    topResult = moveTopDownAlgo(encodedCube, solution, cubeLctn, colorMarker)
    result['solution'] = topResult.get('solution')
    result['cube'] = topResult.get('cube')
    
    solution = result['solution']
    encodedCube = result['cube']
    return encodedCube, solution

def _setMarker(encodedCube,edge1,edge2,center):
    '''variable setter method that sets colorMarkers for if/else in _topToBottomEdgeAlgo'''
    if encodedCube[edge1] == encodedCube[center]: 
        colorMarker = 1
    elif encodedCube[edge2] == encodedCube[center]: 
        colorMarker = 2
    else:
        colorMarker = 0
    return colorMarker
             
def _moveTopByDifference(difference):
    '''Calculates difference between where edge is and where it needs to be. Gives rotation moves for later method'''
    if (difference == 0):
        movementList = '' 
    elif (difference == 1 or difference == -3): #Clockwise rotation
        movementList = 'U'
    elif (difference == -1 or difference == 3): #Counter Clockwise Rotation
        movementList = 'u'
    elif (difference == 2 or difference == -2): #Double CLockwise
        movementList = 'UU'
    return movementList

def _solveEdges(encodedCube, solution, cubeLocation, correctLocation, edgeList, moveToTopAlgo):
    '''Moves unaligned edges (anywhere) to top, rotates to corresponding top, then moves into bottom.
    This is one of the main working methods in solving the bottom edges.'''

    result = {}
    result['cube'] = encodedCube
    result['solution'] = solution
    result['cubeLocation'] = cubeLocation
    edgeSolutionSet = {}

    #Rotate edge out of bottom into top
    for value in (edgeList):
        if value == cubeLocation:
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

    for letter in movementList:
        result['solution'], result['cube'] = _functionalRotations(encodedCube, result, letter)
        encodedCube = result['cube']
    result['cubeLocation'] = correctLocation
    return result

"""
####################################################################################        
############ Rotation Function and Updates to Cube and Solution String #############
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
###########################################################        
############## Unidirectional Rotate Methods ##############
###########################################################
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