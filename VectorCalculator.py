import math
import numpy as np

differenceSizesMessage = "All vectors must have the same size"

def CheckVectorSizes(arrayVectors) -> bool:
    sizes = [len(vector) for vector in arrayVectors]
    setSizes = set(sizes)
    if len(setSizes) != 1: #means there's different sizes 
        return False
    return True

def SumOfVectores(arrayVectors):

    if CheckVectorSizes(arrayVectors) is False:
        return differenceSizesMessage

    R = len(arrayVectors[0])
    finalVector = [0]*R

    for i in range(len(arrayVectors)):
        for k in range(R):
            finalVector[k] += arrayVectors[i][k]

    return finalVector

def NormOfVector(u) -> float:

    norm = 0
    for i in range(len(u)):
        norm += u[i]**2
    
    return norm**(1/2)

def ScalarProduct(arrayVectors):

    if CheckVectorSizes(arrayVectors) is False:
        return differenceSizesMessage
    
    R = len(arrayVectors[0])
    
    coord = [1]*R
    for i in range(len(arrayVectors)):
        for k in range(R):
            coord[k] *= arrayVectors[i][k]
    
    scalarProduct = sum(coord)
    return scalarProduct

def AngleBetweenVectors(arrayVectors):

    if CheckVectorSizes(arrayVectors) is False:
        return differenceSizesMessage

    scalarProduct = ScalarProduct(arrayVectors)

    normProduct = 1
    for vector in arrayVectors:
        normProduct *= NormOfVector(vector)
    
    cossineOfAngle = scalarProduct / normProduct

    angleRadians = math.acos(cossineOfAngle)
    angleDegress = math.degrees(angleRadians)

    return f"{angleRadians:.2f} rad || {angleDegress:.2f}\u00b0"

def CrossProduct(arrayVectors):

    if CheckVectorSizes(arrayVectors) is False:
        return differenceSizesMessage

    u, v = arrayVectors
    u1, u2= u[0], u[1]
    v1, v2 = v[0], v[1]

    if len(u) == 2:
        u3, v3 = 0, 0
    else:
        u3, v3 = u[2], v[2]
    
    x = u2 * v3 - u3 * v2
    y = u3 * v1 - u1 * v3
    z = u1 * v2 - u2 * v1
    
    return [x, y, z]

def ScalarTripleProduct(arrayVectors):

    if CheckVectorSizes(arrayVectors) is False:
        return differenceSizesMessage
    
    u, v, w = arrayVectors
    
    u1, u2, u3 = u
    v1, v2, v3 = v
    w1, w2, w3 = w

    arr = np.array([[u1, u2, u3], [v1, v2, v3], [w1, w2, w3]])
    scalarTripleProduct = np.linalg.det(arr)

    return scalarTripleProduct
