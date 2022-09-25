import rubik.cube as rubik

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    encodedCube = parms.get('cube',None)       #STUB:  get "cube" parameter if present
    result['solution'] = 'FfRrBbLlUuDd'        #STUB:  example rotations
    result['status'] = 'ok'        
    

    if rubik.Cube.isValidLengthCube(cube) == False:
        result['status'] = 'error: Invalid Cube Length'
        status = result['status']
        return result
    
    if rubik.Cube.isValidCubeChar(cube) == False:
        result['status'] = 'error: Invalid Cube Char'
        status = result['status']
        return result
    
    if rubik.Cube.isValidCenterColors(cube) == False:
        result['status'] = 'error: Duplicate Center Colors'
        status = result['status']
        return result
        
    if rubik.Cube.isNineOfEachChar(cube) == False:
        result['status'] = 'error: There May Only Be 9 Of Each Color'
        status = result['status']
        return result    
                 
    return result