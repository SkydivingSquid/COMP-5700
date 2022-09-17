import rubik.cube as rubik

def _rotate(parms):
    """Return rotated cube""" 
    result = {}
    #frmMeth = {}
    
    cube = parms.get('cube')
    dir = parms.get('dir')
    
    if dir == 'F':
        result = _rotateF(cube, dir)
        
    elif dir == 'f':
        result = _rotatef(cube, dir)
        
    elif dir == 'R':
        result = _rotateR(cube, dir)
        
    elif dir == 'r':
        result = _rotater(cube, dir)
        
    elif dir == 'B':
        result = _rotateB(cube, dir)
        
    elif dir == 'b':
        result = _rotateb(cube, dir)
        
    elif dir == 'L':
        result = _rotateL(cube, dir)
        
    elif dir == 'l':
        result = _rotatel(cube, dir)
        
    elif dir == 'U':
        result = _rotateU(cube, dir)
        
    elif dir == 'u':
        result = _rotateu(cube, dir)

    elif dir == 'D':
        result = _rotateD(cube, dir)
        
        
        
        
    result['cube'] = result.get('cube')
    result['status'] = result.get('status')
    return result
    
#Rotate front face clockwise (F)
def _rotateF(cube, dir):
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
    
    rotatedCube = "".join(rotatedCubeList)
    
    result['cube'] = rotatedCube
    result['status'] = 'ok'
    return result

#Rotate front face counter-clockwise (f)
def _rotatef(cube, dir):
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
    
    rotatedCube = "".join(rotatedCubeList)
    
    result['cube'] = rotatedCube
    result['status'] = 'ok'
    return result

#Rotate right face clockwise (R)
def _rotateR(cube, dir):
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
    
    rotatedCube = "".join(rotatedCubeList)
    
    result['cube'] = rotatedCube
    result['status'] = 'ok'
    
    return result

#Rotate right face clockwise (R)
def _rotater(cube, dir):
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
    
    rotatedCube = "".join(rotatedCubeList)
    
    result['cube'] = rotatedCube
    result['status'] = 'ok'
    
    return result
def _rotateB(cube, dir):
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
    rotatedCube = "".join(rotatedCubeList)

    result['cube'] = rotatedCube
    result['status'] = 'ok'

    return result
def _rotateb(cube, dir):
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
    rotatedCube = "".join(rotatedCubeList)

    result['cube'] = rotatedCube
    result['status'] = 'ok'

    return result
def _rotateL(cube, dir):
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
#
    rotatedCube = "".join(rotatedCubeList)

    result['cube'] = rotatedCube
    result['status'] = 'ok'

    return result
def _rotatel(cube, dir):
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

    rotatedCube = "".join(rotatedCubeList)

    result['cube'] = rotatedCube
    result['status'] = 'ok'

    return result
def _rotateU(cube, dir):
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

    rotatedCube = "".join(rotatedCubeList)

    result['cube'] = rotatedCube
    result['status'] = 'ok'

    return result
def _rotateu(cube, dir):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[36] = cubeList[48]
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

    rotatedCube = "".join(rotatedCubeList)

    result['cube'] = rotatedCube
    result['status'] = 'ok'

    return result


def _rotated(cube, dir):
    result = {}

    cubeList = list(cube)
    rotatedCubeList = cubeList[:]

    #rotate front face
    rotatedCubeList[47] = cubeList[45]
    rotatedCubeList[50] = cubeList[46]
    rotatedCubeList[53] = cubeList[47]
    rotatedCubeList[46] = cubeList[48]
    rotatedCubeList[49] = cubeList[49]
    rotatedCubeList[52] = cubeList[50]
    rotatedCubeList[45] = cubeList[51]
    rotatedCubeList[47] = cubeList[52]
    rotatedCubeList[51] = cubeList[53]
    
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

    rotatedCube = "".join(rotatedCubeList)

    result['cube'] = rotatedCube
    result['status'] = 'ok'

    return result
#
# def _rotateD(cube, dir):
#     result = {}
#
#     cubeList = list(cube)
#     rotatedCubeList = cubeList[:]
#
#         #rotate front face
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#
#     #rotate top to right
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#
#     #rotate right to bottom
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#
#     #rotate bottom to left
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[]
#
#     #rotate left to top
#     rotatedCubeList[] = cubeList[]
#     rotatedCubeList[] = cubeList[] 
#     rotatedCubeList[] = cubeList[]
#
#     rotatedCube = "".join(rotatedCubeList)
#
#     result['cube'] = rotatedCube
#     result['status'] = 'ok'
#
#     return result
    
        
        

    