import rubik.cube as rubik

def _verify(parms):
    """Determines if the provided cube is physically valid. Returns:
       {'status': 'ok'} if valid 
       {'status': 'error: xxx} if invalid"""
    result = {}
    encodedCube = parms.get('cube',None)       #STUB:  get "cube" parameter if present
    result['status'] = 'ok'                     
    return result