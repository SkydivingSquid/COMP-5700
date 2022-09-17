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
        
    elif dir == 'r'
        result = _rotate(cube, dir):    
        
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
    
    # #rotate front face
    # rotatedCubeList[9] = cubeList[11]
    # rotatedCubeList[10] = cubeList[14]
    # rotatedCubeList[11] = cubeList[17]
    # rotatedCubeList[12] = cubeList[10]
    # rotatedCubeList[13] = cubeList[13]
    # rotatedCubeList[14] = cubeList[16]
    # rotatedCubeList[15] = cubeList[9]
    # rotatedCubeList[16] = cubeList[12]
    # rotatedCubeList[17] = cubeList[15]
    #
    # #rotate top to right
    # rotatedCubeList[44] = cubeList[18]
    # rotatedCubeList[41] = cubeList[21]
    # rotatedCubeList[38] = cubeList[24]
    #
    # #rotate right to bottom
    # rotatedCubeList[18] = cubeList[53]
    # rotatedCubeList[21] = cubeList[50]
    # rotatedCubeList[24] = cubeList[47]
    #
    # #rotate bottom to left
    # rotatedCubeList[47] = cubeList[2]
    # rotatedCubeList[50] = cubeList[5]
    # rotatedCubeList[53] = cubeList[8]
    #
    # #rotate left to top
    # rotatedCubeList[2] = cubeList[38]
    # rotatedCubeList[5] = cubeList[41] 
    # rotatedCubeList[8] = cubeList[44]
    
    rotatedCube = "".join(rotatedCubeList)
    
    result['cube'] = rotatedCube
    result['status'] = 'ok'
    
    return result

#
# def _rotateB(cube, dir):
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
#
# def _rotateL(cube, dir):
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
#
# def _rotateU(cube, dir):
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
    
        
        

    