import rubik.cube as rubik

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    encodedCube = parms.get('cube',None)       #STUB:  get "cube" parameter if present
    result['solution'] = ''        #STUB:  example rotations
    result['status'] = 'ok'
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
    
    for matchingColors in (rotatedCubeList[46], rotatedCubeList[48], 
                           rotatedCubeList[50], rotatedCubeList[52]):
        if matchingColors == rotatedCubeList[49]:
            
            if (rotatedCubeList[4] == rotatedCubeList[7] and
                rotatedCubeList[13] == rotatedCubeList[16] and
                rotatedCubeList[22] == rotatedCubeList[25] and
                rotatedCubeList[31] == rotatedCubeList[34]):
                
                result['solution'] = ''
                result['status'] = 'ok'
                return result
    
    