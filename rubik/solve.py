import rubik.cube as rubik
from codecs import EncodedFile

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    encodedCube = parms.get('cube',None)       #STUB:  get "cube" parameter if present
    result['solution'] = ""        #STUB:  example rotations
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
                 
    return result

def _solveBottomCross(encodedCube):
    result = {}
    cubeList = list(encodedCube)
    rotatedCubeList = cubeList[:]
    result['solution'] = ""
    result['status'] = 'ok'
    
    #Check for bottom cross
    for matchingColors in (rotatedCubeList[46], rotatedCubeList[48], 
                           rotatedCubeList[50], rotatedCubeList[52]):
        if matchingColors == rotatedCubeList[49]:
            
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
            
            else: 
                F_result = _rotateF(encodedCube)
                result['solution'] += F_result.get('letter')
                encodedCube = F_result.get('cube')
                
                F_result = _rotateF(encodedCube)
                result['solution'] += F_result.get('letter')
                encodedCube = F_result.get('cube')
                
                
                
                result['status'] = 'ok'
                return result 
                
                


############ Rotate Methods. . . ############


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
    
    rotatedCubeList
    
    result['cube'] = rotatedCubeList
    result['letter'] = 'F'
    return result








    