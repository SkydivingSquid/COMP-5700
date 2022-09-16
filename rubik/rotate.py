import rubik.cube as rubik

def _rotate(parms):
    """Return rotated cube""" 
    result = {}
    #frmMeth = {}
    
    cube = parms.get('cube')
    dir = parms.get('dir')
    
    if dir == 'F':
        result = _rotateF(cube, dir)
        
    elif dir == 'f'
        result = _rotatef(cube, dir)
        
        
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
    
    #rotate top to right
    rotatedCubeList[42] = cubeList[9]
    rotatedCubeList[43] = cubeList[12]
    rotatedCubeList[44] = cubeList[15]
    
    #rotate right to bottom
    rotatedCubeList[9] = cubeList[47]
    rotatedCubeList[12] = cubeList[46]
    rotatedCubeList[15] = cubeList[45]
    
    #rotate bottom to left
    rotatedCubeList[45] = cubeList[29]
    rotatedCubeList[46] = cubeList[32]
    rotatedCubeList[47] = cubeList[35]
    
    #rotate left to top
    rotatedCubeList[29] = cubeList[44]
    rotatedCubeList[32] = cubeList[43] 
    rotatedCubeList[35] = cubeList[42]
    
    rotatedCube = "".join(rotatedCubeList)
    
    result['cube'] = rotatedCube
    result['status'] = 'ok'
    return result
    
        
        

    