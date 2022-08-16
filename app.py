import os
import sys
from flask import Flask, request, render_template
import sbom.info as sbom
import rubik.dispatch as dispatch

app = Flask(__name__)

def getAbout():
    return {'platform': sys.platform,
            'version': sys.version,
            'developer': sbom.info()}
    

#-----------------------------------
#  Default entry point.  It results in a
#  HTML-friendly confirmation that the microservice is active.
#  
#
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    aboutInfo = getAbout()
    
    return render_template('index.html',
        message = "Microservice deployed",
        Developer = aboutInfo['developer'],
        Platform = aboutInfo['platform'],
        Version = aboutInfo['version'])
    
#-----------------------------------
#  The following code is invoked with the path portion of the URL matches
#         /about
#  It results in 
#
@app.route('/about')
def about():
    """Return about information"""
    return str(getAbout())
    
    
#-----------------------------------
#  The following code is invoked when the path portion of the URL matches 
#         /rubik
#
#  Parameters are passed as a URL query:
#        /rubik?parm1=value1&parm2=value2
#
@app.route('/rubik')
def server():
    """Return dispatched solution."""
    try:
        userParms = {}
        for key in request.args:
            userParms[key] = str(request.args.get(key, ''))
        result=dispatch._dispatch(userParms)
        print("Response -->", str(result))
        return str(result)
    except Exception as e:
        return str(e)
    
    
#-----------------------------------
if __name__ == "__main__":
    port = os.getenv('PORT', '8080')
    app.run(debug=False, host = '0.0.0.0', port = int(port))

