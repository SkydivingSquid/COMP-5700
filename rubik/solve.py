import rubik.cube as rubik
from codecs import EncodedFile

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    encodedCube = parms.get('cube',None)       #STUB:  get "cube" parameter if present
    result['solution'] = ""                 
    result['status'] = 'ok'
    result['cube'] = encodedCube
    status = result['status']     
    

    if rubik.Cube.isValidLengthCube(encodedCube) == False:
        result['status'] = 'error: Invalid Cube Length'
        status = result['status']
        return result
    
    if rubik.Cube.isValidCubeChar(encodedCube) == False:
        result['status'] = 'error: Invalid Cube Char'
        status = result['status']
        return result
    
    if rubik.Cube.isValidCenterColors(encodedCube) == False:
        result['status'] = 'error: Duplicate Center Colors'
        status = result['status']
        return result
        
    if rubik.Cube.isNineOfEachChar(encodedCube) == False:
        result['status'] = 'error: There May Only Be 9 Of Each Color'
        status = result['status']
        return result    
    
    if status == 'ok':
        result = _solveBottomCross(encodedCube)
                 
    print(result)
    return result


def _solveBottomCross(encodedCube):
    result = {}
    cubeList = list(encodedCube)
    rotatedCubeList = cubeList[:]
    result['solution'] = ""
    result['status'] = 'ok'
    
    #Check for bottom cross
    if (rotatedCubeList[46] == rotatedCubeList[49] and
    rotatedCubeList[48] == rotatedCubeList[49] and
    rotatedCubeList[50] == rotatedCubeList[49] and
    rotatedCubeList[52] == rotatedCubeList[49]):

            
        #Check for bottom cross alignment
        if (rotatedCubeList[4] == rotatedCubeList[7] and
            rotatedCubeList[13] == rotatedCubeList[16] and
            rotatedCubeList[22] == rotatedCubeList[25] and
            rotatedCubeList[31] == rotatedCubeList[34]):
            
            #Return solution for solved cube
            result['solution'] = ''
            result['status'] = 'ok'
            #These two are irrelevant, but here for future use
            rotatedCube = "".join(rotatedCubeList)
            result['cube'] = rotatedCube
            
            return result
        
        #Rotate unaligned bottom cross into top daisy
        else: 
            F_result = _rotateF(encodedCube)
            result['solution'] += F_result.get('letter')
            encodedCube = F_result.get('cube')
            
            F_result = _rotateF(encodedCube)
            result['solution'] += F_result.get('letter')
            encodedCube = F_result.get('cube')
            
            R_result = _rotateR(encodedCube)
            result['solution'] += R_result.get('letter')
            encodedCube = R_result.get('cube')
            
            R_result = _rotateR(encodedCube)
            result['solution'] += R_result.get('letter')
            encodedCube = R_result.get('cube')
            
            B_result = _rotateB(encodedCube)
            result['solution'] += B_result.get('letter')
            encodedCube = B_result.get('cube')
            
            B_result = _rotateB(encodedCube)
            result['solution'] += B_result.get('letter')
            encodedCube = B_result.get('cube')
            
            L_result = _rotateL(encodedCube)
            result['solution'] += L_result.get('letter')
            encodedCube = L_result.get('cube')
            
            L_result = _rotateL(encodedCube)
            result['solution'] += L_result.get('letter')
            encodedCube = L_result.get('cube')
            
            #DAISY HAS BEEN CREATAED
            
            daisySolution = _daisySolution(encodedCube)
            
            encodedCube = daisySolution.get('cube')
            
            result['cube'] = "".join(encodedCube)
            result['solution'] += daisySolution.get('solution')
            result['status'] = 'ok'
            
            return result
    
    
    #Check Top for Daisy  
    if (rotatedCubeList[37] == rotatedCubeList[49] and
        rotatedCubeList[39] == rotatedCubeList[49] and
        rotatedCubeList[41] == rotatedCubeList[49] and
        rotatedCubeList[43] == rotatedCubeList[49]):
    
        daisySolution = _daisySolution(encodedCube)
    
        encodedCube = daisySolution.get('cube')
    
        result['cube'] = "".join(encodedCube)
        result['solution'] += daisySolution.get('solution')
        result['status'] = 'ok'
    
        return result
        
    
def _daisySolution(encodedCube):
    result = {}
    cubeList = list(encodedCube)
    rotatedCubeList = cubeList[:]
    result['solution'] = ""
    
    #Front Face Alignment
    if not (rotatedCubeList[4] == rotatedCubeList[7] and rotatedCubeList[49] == rotatedCubeList[46]):
        
        while rotatedCubeList[4]!= rotatedCubeList[1]:
            U_result = _rotateU(encodedCube) 
            result['solution'] += U_result.get('letter')
            encodedCube = U_result.get('cube')
            
            rotatedCubeList[4] = encodedCube[4]
            rotatedCubeList[1] = encodedCube[1]
        
        if rotatedCubeList[4] == rotatedCubeList[1]:
            F_result = _rotateF(encodedCube)
            result['solution'] += F_result.get('letter')
            encodedCube = F_result.get('cube')
        
            F_result = _rotateF(encodedCube)
            result['solution'] += F_result.get('letter')
            encodedCube = F_result.get('cube')
            
            result['cube'] = encodedCube
            

    #Right Face Alignment
    if not (rotatedCubeList[13] == rotatedCubeList[16] and rotatedCubeList[49] == rotatedCubeList[50]):
        
        while rotatedCubeList[13]!= rotatedCubeList[10]:
            U_result = _rotateU(encodedCube) 
            result['solution'] += U_result.get('letter')
            encodedCube = U_result.get('cube')
            
            rotatedCubeList[13] = encodedCube[13]
            rotatedCubeList[10] = encodedCube[10]

        if rotatedCubeList[13] == rotatedCubeList[10]:
            R_result = _rotateR(encodedCube)
            result['solution'] += R_result.get('letter')
            encodedCube = R_result.get('cube')
    
            R_result = _rotateR(encodedCube)
            result['solution'] += R_result.get('letter')
            encodedCube = R_result.get('cube')
    
            result['cube'] = encodedCube
    
    
    # #Back Face Alignment
    if not (rotatedCubeList[22] == rotatedCubeList[25] and rotatedCubeList[49] == rotatedCubeList[52]):
        
        while rotatedCubeList[22]!= rotatedCubeList[19]:
            U_result = _rotateU(encodedCube) 
            result['solution'] += U_result.get('letter')
            encodedCube = U_result.get('cube')
            
            rotatedCubeList[22] = encodedCube[22]
            rotatedCubeList[19] = encodedCube[19]
        
        if rotatedCubeList[22] == rotatedCubeList[19]:
            B_result = _rotateB(encodedCube)
            result['solution'] += B_result.get('letter')
            encodedCube = B_result.get('cube')
    
            B_result = _rotateB(encodedCube)
            result['solution'] += B_result.get('letter')
            encodedCube = B_result.get('cube')

            result['cube'] = encodedCube

    
    # #Left Face Alignment
    if not (rotatedCubeList[31] == rotatedCubeList[34] and rotatedCubeList[49] == rotatedCubeList[48]):
        
        while rotatedCubeList[31]!= rotatedCubeList[28]:
            U_result = _rotateU(encodedCube) 
            result['solution'] += U_result.get('letter')
            encodedCube = U_result.get('cube')
            
            rotatedCubeList[31] = encodedCube[31]
            rotatedCubeList[28] = encodedCube[28]
    
    
        if rotatedCubeList[31] == rotatedCubeList[28]:
            L_result = _rotateL(encodedCube)
            result['solution'] += L_result.get('letter')
            encodedCube = L_result.get('cube')
    
            L_result = _rotateL(encodedCube)
            result['solution'] += L_result.get('letter')
            encodedCube = L_result.get('cube')
    
            result['cube'] = encodedCube
            result['status'] = 'ok'
            
    return result

        
        



############ Rotate Methods For Solving Cube ###########


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
    rotatedCubeList[9] = cubeList[42]
    rotatedCubeList[12] = cubeList[43]
    rotatedCubeList[15] = cubeList[44]
    
    #rotate right to bottom
    rotatedCubeList[47] = cubeList[9]
    rotatedCubeList[46] = cubeList[12]
    rotatedCubeList[45] = cubeList[15]
    
    #rotate bottom to left
    rotatedCubeList[29] = cubeList[45]
    rotatedCubeList[32] = cubeList[46]
    rotatedCubeList[35] = cubeList[47]
    
    #rotate left to top
    rotatedCubeList[44] = cubeList[29]
    rotatedCubeList[43] = cubeList[32] 
    rotatedCubeList[42] = cubeList[35]
    
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
    rotatedCubeList[42] = cubeList[9]
    rotatedCubeList[43] = cubeList[12]
    rotatedCubeList[44] = cubeList[15]
    
    #rotate bottom to right
    rotatedCubeList[9] = cubeList[47]
    rotatedCubeList[12] = cubeList[46]
    rotatedCubeList[15] = cubeList[45]
    
    #rotate left to bottom
    rotatedCubeList[45] = cubeList[29]
    rotatedCubeList[46] = cubeList[32]
    rotatedCubeList[47] = cubeList[35]
    
    #rotate top to left
    rotatedCubeList[29] = cubeList[44]
    rotatedCubeList[32] = cubeList[43] 
    rotatedCubeList[35] = cubeList[42]
    
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
    rotatedCubeList[14] = cubeList[10]
    rotatedCubeList[17] = cubeList[11]
    rotatedCubeList[10] = cubeList[12]
    rotatedCubeList[13] = cubeList[13]
    rotatedCubeList[16] = cubeList[14]
    rotatedCubeList[9] = cubeList[15]
    rotatedCubeList[12] = cubeList[16]
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
    rotatedCubeList[10] = cubeList[14]
    rotatedCubeList[11] = cubeList[17]
    rotatedCubeList[12] = cubeList[10]
    rotatedCubeList[13] = cubeList[13]
    rotatedCubeList[14] = cubeList[16]
    rotatedCubeList[15] = cubeList[9]
    rotatedCubeList[16] = cubeList[12]
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
    rotatedCubeList[23] = cubeList[19]
    rotatedCubeList[26] = cubeList[20]
    rotatedCubeList[19] = cubeList[21]
    rotatedCubeList[22] = cubeList[22]
    rotatedCubeList[25] = cubeList[23]
    rotatedCubeList[18] = cubeList[24]
    rotatedCubeList[21] = cubeList[25]
    rotatedCubeList[24] = cubeList[26]

    #rotate top to right
    rotatedCubeList[27] = cubeList[38]
    rotatedCubeList[30] = cubeList[37]
    rotatedCubeList[33] = cubeList[36]

    #rotate right to bottom
    rotatedCubeList[51] = cubeList[27]
    rotatedCubeList[52] = cubeList[30]
    rotatedCubeList[53] = cubeList[33]

    #rotate bottom to left
    rotatedCubeList[17] = cubeList[51]
    rotatedCubeList[14] = cubeList[52]
    rotatedCubeList[11] = cubeList[53]

    #rotate left to top
    rotatedCubeList[36] = cubeList[11]
    rotatedCubeList[37] = cubeList[14] 
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
    rotatedCubeList[19] = cubeList[23]
    rotatedCubeList[20] = cubeList[26]
    rotatedCubeList[21] = cubeList[19]
    rotatedCubeList[22] = cubeList[22]
    rotatedCubeList[23] = cubeList[25]
    rotatedCubeList[24] = cubeList[18]
    rotatedCubeList[25] = cubeList[21]
    rotatedCubeList[26] = cubeList[24]

    #rotate top to right
    rotatedCubeList[38] = cubeList[27]
    rotatedCubeList[37] = cubeList[30]
    rotatedCubeList[36] = cubeList[33]

    #rotate right to bottom
    rotatedCubeList[27] = cubeList[51]
    rotatedCubeList[30] = cubeList[52]
    rotatedCubeList[33] = cubeList[53]

    #rotate bottom to left
    rotatedCubeList[51] = cubeList[17]
    rotatedCubeList[52] = cubeList[14]
    rotatedCubeList[53] = cubeList[11]

    #rotate left to top
    rotatedCubeList[11] = cubeList[36]
    rotatedCubeList[14] = cubeList[37] 
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
    rotatedCubeList[32] = cubeList[28]
    rotatedCubeList[35] = cubeList[29]
    rotatedCubeList[28] = cubeList[30]
    rotatedCubeList[31] = cubeList[31]
    rotatedCubeList[34] = cubeList[32]
    rotatedCubeList[27] = cubeList[33]
    rotatedCubeList[30] = cubeList[34]
    rotatedCubeList[33] = cubeList[35]

    #rotate top to right
    rotatedCubeList[0] = cubeList[36]
    rotatedCubeList[3] = cubeList[39]
    rotatedCubeList[6] = cubeList[42]

    #rotate right to bottom
    rotatedCubeList[45] = cubeList[0]
    rotatedCubeList[48] = cubeList[3]
    rotatedCubeList[51] = cubeList[6]

    #rotate bottom to left
    rotatedCubeList[26] = cubeList[45]
    rotatedCubeList[23] = cubeList[48]
    rotatedCubeList[20] = cubeList[51]

    #rotate left to top
    rotatedCubeList[42] = cubeList[20]
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
    rotatedCubeList[28] = cubeList[32]
    rotatedCubeList[29] = cubeList[35]
    rotatedCubeList[30] = cubeList[28]
    rotatedCubeList[31] = cubeList[31]
    rotatedCubeList[32] = cubeList[34]
    rotatedCubeList[33] = cubeList[27]
    rotatedCubeList[34] = cubeList[30]
    rotatedCubeList[35] = cubeList[33]
    
    #rotate top to right
    rotatedCubeList[36] = cubeList[0]
    rotatedCubeList[39] = cubeList[3]
    rotatedCubeList[42] = cubeList[6]
    
    #rotate right to bottom
    rotatedCubeList[0] = cubeList[45]
    rotatedCubeList[3] = cubeList[48]
    rotatedCubeList[6] = cubeList[51]
    
    #rotate bottom to left
    rotatedCubeList[51] = cubeList[20]
    rotatedCubeList[48] = cubeList[23]
    rotatedCubeList[45] = cubeList[26]
    
    #rotate left to top
    rotatedCubeList[20] = cubeList[42]
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
    rotatedCubeList[41] = cubeList[37]
    rotatedCubeList[44] = cubeList[38]
    rotatedCubeList[37] = cubeList[39]
    rotatedCubeList[40] = cubeList[40]
    rotatedCubeList[43] = cubeList[41]
    rotatedCubeList[36] = cubeList[42]
    rotatedCubeList[39] = cubeList[43]
    rotatedCubeList[42] = cubeList[44]
    
    #rotate top to right
    rotatedCubeList[9] = cubeList[18]
    rotatedCubeList[10] = cubeList[19]
    rotatedCubeList[11] = cubeList[20]
    
    #rotate right to bottom
    rotatedCubeList[0] = cubeList[9]
    rotatedCubeList[1] = cubeList[10]
    rotatedCubeList[2] = cubeList[11]
    
    #rotate bottom to left
    rotatedCubeList[27] = cubeList[0]
    rotatedCubeList[28] = cubeList[1]
    rotatedCubeList[29] = cubeList[2]
    
    #rotate left to top
    rotatedCubeList[18] = cubeList[27]
    rotatedCubeList[19] = cubeList[28] 
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
    rotatedCubeList[37] = cubeList[41]
    rotatedCubeList[38] = cubeList[44]
    rotatedCubeList[39] = cubeList[37]
    rotatedCubeList[40] = cubeList[40]
    rotatedCubeList[41] = cubeList[43]
    rotatedCubeList[42] = cubeList[36]
    rotatedCubeList[43] = cubeList[39]
    rotatedCubeList[44] = cubeList[42]
    
    #rotate top to right
    rotatedCubeList[18] = cubeList[9]
    rotatedCubeList[19] = cubeList[10]
    rotatedCubeList[20] = cubeList[11]
    
    #rotate right to bottom
    rotatedCubeList[9] = cubeList[0]
    rotatedCubeList[10] = cubeList[1]
    rotatedCubeList[11] = cubeList[2]
    
    #rotate bottom to left
    rotatedCubeList[0] = cubeList[27]
    rotatedCubeList[1] = cubeList[28]
    rotatedCubeList[2] = cubeList[29]
    
    #rotate left to top
    rotatedCubeList[27] = cubeList[18]
    rotatedCubeList[28] = cubeList[19] 
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
    rotatedCubeList[46] = cubeList[48]
    rotatedCubeList[47] = cubeList[45]
    rotatedCubeList[48] = cubeList[52]
    rotatedCubeList[49] = cubeList[49]
    rotatedCubeList[50] = cubeList[46]
    rotatedCubeList[51] = cubeList[53]
    rotatedCubeList[52] = cubeList[50]
    rotatedCubeList[53] = cubeList[47]
    
    #rotate top to left
    rotatedCubeList[6] = cubeList[33]
    rotatedCubeList[7] = cubeList[34]
    rotatedCubeList[8] = cubeList[35]
    
    #rotate right to top
    rotatedCubeList[15] = cubeList[6]
    rotatedCubeList[16] = cubeList[7]
    rotatedCubeList[17] = cubeList[8]
    
    #rotate bottom to right
    rotatedCubeList[24] = cubeList[15]
    rotatedCubeList[25] = cubeList[16]
    rotatedCubeList[26] = cubeList[17]
    
    #rotate left to bottom
    rotatedCubeList[33] = cubeList[24]
    rotatedCubeList[34] = cubeList[25] 
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
    rotatedCubeList[48] = cubeList[46]
    rotatedCubeList[45] = cubeList[47]
    rotatedCubeList[52] = cubeList[48]
    rotatedCubeList[49] = cubeList[49]
    rotatedCubeList[46] = cubeList[50]
    rotatedCubeList[53] = cubeList[51]
    rotatedCubeList[50] = cubeList[52]
    rotatedCubeList[47] = cubeList[53]
    
    #rotate top to left
    rotatedCubeList[33] = cubeList[6]
    rotatedCubeList[34] = cubeList[7]
    rotatedCubeList[35] = cubeList[8]
    
    #rotate right to top
    rotatedCubeList[6] = cubeList[15]
    rotatedCubeList[7] = cubeList[16]
    rotatedCubeList[8] = cubeList[17]
    
    #rotate bottom to right
    rotatedCubeList[15] = cubeList[24]
    rotatedCubeList[16] = cubeList[25]
    rotatedCubeList[17] = cubeList[26]
    
    #rotate left to bottom
    rotatedCubeList[24] = cubeList[33]
    rotatedCubeList[25] = cubeList[34] 
    rotatedCubeList[26] = cubeList[35]

    result['cube'] = rotatedCubeList
    result['letter'] = 'd'
    return result






    