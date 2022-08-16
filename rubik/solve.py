import rubik.cube as rubik

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    encodedCube = parms.get('cube',None)       #STUB:  get "cube" parameter if present
    result['solution'] = 'FfRrBbLlUuDd'        #STUB:  example rotations
    result['status'] = 'ok'                     
    return result