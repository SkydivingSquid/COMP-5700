import rubik.create as create
import rubik.rotate as rotate
import rubik.solve as solve
import rubik.verify as verify

ERROR01 = 'error: no op is specified'
ERROR02 = 'error: parameter is not a dictionary'
ERROR03 = 'error: op is not legal'
STATUS = 'status'
OP = 'op'
OPS = {
    'create' : create._create,
    'rotate': rotate._rotate,
    'solve' : solve._solve,
    'verify': verify._verify,
    }

def _dispatch(parms = None):
    """Dispatch based on value of 'op' key"""

    result = {}
    
    # Validate parm
    if(parms == None):
        result = {STATUS: ERROR01}
    elif(not(isinstance(parms, dict))):
        result = {STATUS: ERROR02}
    elif (not(OP in parms)):
        result = {STATUS: ERROR01}
    elif(not(parms[OP] in OPS)):
        result[STATUS] = ERROR03
    else:
        result = OPS[parms[OP]](parms)
    return result
