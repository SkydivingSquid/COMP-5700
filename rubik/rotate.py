import rubik.cube as rubik

def _rotate(parms):
    """Return rotated cube""" 
    result = {}
    #encodedCube = parms.get('cube',None)       #STUB:  get "cube" parameter if present
    #rotatedCube = encodedCube                  #STUB:  rotate the cube
    
    #alt1
    #result['cube'] = 'gggggggggyooyooyoobbbbbbbbbrrwrrwrrwyyyyyyrrrooowwwwww'   
    
    
    #alt2.1
    cube = parms.get('cube')
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    
    #Change values below to cubeList[i]
    
    #Six Single Unchanging Center Cubes
    
    Front_Single = {5:cubeList[4]}
    Right_Single = {14:cubeList[13]}
    Back_Single = {23:cubeList[22]}
    Left_Single = {32:cubeList[31]}
    Top_Single = {41:cubeList[40]}
    Bottom_Single = {50:cubeList[49]}
    
    #Twelve Double Cubes
    Front_upper_Double = {2:cubeList[1], 44:cubeList[43]}
    Front_stbd_Double = {6:cubeList[5], 13:cubeList[12]}
    Front_port_Double = {4:cubeList[3], 33:cubeList[32]}
    Front_lower_Double = {8:cubeList[7], 47:cubeList[46]}
    
    Right_upper_Double = {11:cubeList[10],42:cubeList[41]}
    Right_stbd_Double = {15:cubeList[14],22:cubeList[21]}
    Right_lower_Double = {17:cubeList[16],51:cubeList[50]}

    Back_upper_Double = {20:cubeList[19],38:cubeList[37]}
    Back_lower_Double = {26:cubeList[26],53:cubeList[52]}
    
    Left_upper_Double = {29:cubeList[28],40:cubeList[39]}
    Left_port_Double = {31:cubeList[30],24:cubeList[23]}
    Left_lower_Double = {35:cubeList[34],48:cubeList[47]}
    
    #Eight Triple Cubes
    Top_Front_Right = {3:cubeList[2],10:cubeList[9],45:cubeList[44]}
    Top_Front_Left = {1:cubeList[0],30:cubeList[29],43:cubeList[42]}
    Top_Back_Right = {19:cubeList[18],12:cubeList[11],39:cubeList[38]}
    Top_Back_Left = {21:cubeList[20],28:cubeList[27],37:cubeList[36]}
    
    Bottom_Front_Right = {9:cubeList[8],16:cubeList[15],48:cubeList[47]}
    Bottom_Front_Left = {7:cubeList[6],36:cubeList[35],46:cubeList[45]}
    Bottom_Back_Right = {25:cubeList[24],18:cubeList[17],54:cubeList[53]}
    Bottom_Back_Left = {27:cubeList[26],34:cubeList[33],52:cubeList[51]}
    
    
    
    #alt2
    # cube = parms.get('cube')
    # cubeList = list(cube)
    # rotatedCubeList = cubeList[:]
    #
    # #rotate front face
  
    # rotatedCubeList[5] = cubeList[1]
    # rotatedCubeList[8] = cubeList[2]
    # rotatedCubeList[1] = cubeList[3]
    # rotatedCubeList[4] = cubeList[4]
    # rotatedCubeList[7] = cubeList[5]
    # rotatedCubeList[0] = cubeList[6]
    # rotatedCubeList[3] = cubeList[7]
    # rotatedCubeList[6] = cubeList[8]
    #
    # #rotate top to right
    # rotatedCubeList[9] = cubeList[42]
    # rotatedCubeList[12] = cubeList[43]
    # rotatedCubeList[]15 = cubeList[44]
    #
    # #rotate right to bottom
    # rotatedCubeList[47] = cubeList[9]
    # rotatedCubeList[46] = cubeList[12]
    # rotatedCubeList[45] = cubeList[15]
    #
    # #rotate bottom to left
    # rotatedCubeList[29] = cubeList[45]
    # rotatedCubeList[32] = cubeList[46]
    # rotatedCubeList[35] = cubeList[47]
    #
    # #rotate left to top
    # rotatedCubeList[44] = cubeList[29]
    # rotatedCubeList[43] = cubeList[32]
    # rotatedCubeList[42] = cubeList[36]
    #
    # rotate = "".join(rotatedCubeList)
    
    
    #alt3
    # myCube = rubik.Cube(parms.get('cube'))
    # myCube.rotate(parms.get('dir'))
    # result['cube'] = myCube.toString()
    #
    # result['status'] = 'ok'                     
    # return result