import rubik.cube as rubik

def _rotate(parms):
    """Return rotated cube""" 
    result = {}
    encodedCube = parms.get('cube',None)       #STUB:  get "cube" parameter if present
    rotatedCube = encodedCube                  #STUB:  rotate the cube
    result['cube'] = rotatedCube               
    result['status'] = 'ok'                     
    return result