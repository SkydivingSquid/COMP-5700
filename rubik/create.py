import rubik.cube as rubik

def _create(parms):
    """Return sample unsolved cube"""
    DEFAULT_COLORS = "bogrwy"
    result={}
    colors = parms.get('colors',DEFAULT_COLORS)                         #STUB:  get possible colors
    cube = ""
    for color in colors:
        cube += color * 9
    result['cube'] = cube
    result['status'] = 'ok'
    return result