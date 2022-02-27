import numpy as np
import math
# Starting Convex Hull
def myConvexHull(arrayPoints):
    s1 = np.array([])
    s2 = np.array([])
    idxMin, idxMax = myMinMax(arrayPoints)
    s1, s2 = divide(idxMin, idxMax, range(len(arrayPoints)), arrayPoints)
    hull1 = myConvexHullRec(idxMin, idxMax, s1, arrayPoints)
    hull2 = myConvexHullRec(idxMax, idxMin, s2, arrayPoints)
    tempHull = np.concatenate(([idxMin], hull1, [idxMax], hull2))
    HullObject = connectPoints(tempHull)
    HullObject = np.int_(HullObject)
    return HullObject
# make array of connected points (indexes)
def connectPoints(arrayIndexes):
    tempArray = []
    for i in range(len(arrayIndexes)-1):
        tempArray.append([int(arrayIndexes[i]), int(arrayIndexes[i+1])])
    tempArray.append([int(arrayIndexes[len(arrayIndexes)-1]), int(arrayIndexes[0])])
    tempArray = np.array(tempArray)
    return tempArray

# Recursive function of ConvexHull
def myConvexHullRec(i1, i2, s, arrayPoints):
    # return array of indexes
    if len(s) == 0 or len(s) == 1:
        return s
    else:
        p1 = arrayPoints[i1]
        p2 = arrayPoints[i2]
        #farthest distance
        farIdx = s[0]
        fardistance = PointToLineDistance(p1, p2, arrayPoints[s[0]])
        for i in s:
            distance = PointToLineDistance(p1, p2, arrayPoints[i])
            if distance > fardistance:
                fardistance = distance
                farIdx = i
        s1, s1_dump = divide(i1, farIdx, s, arrayPoints)
        s2, s2_dump = divide(farIdx, i2, s, arrayPoints)
        hull1 = myConvexHullRec(i1, farIdx, s1, arrayPoints)
        hull2 = myConvexHullRec(farIdx, i2, s2, arrayPoints)
        hullR = np.concatenate((hull1, [farIdx], hull2))
        return hullR
        
def myMinMax(arrayPoints):
    idxMin = 0
    idxMax = 0
    for i in range(1, len(arrayPoints)):
        # Min check
        if arrayPoints[i, 0] < arrayPoints[idxMin, 0]:
            idxMin = i
        elif arrayPoints[i, 0] == arrayPoints[idxMin, 0]:
            if arrayPoints[i, 1] < arrayPoints[idxMin, 1]:
                idxMin = i
            # Max check
        if arrayPoints[i, 0] > arrayPoints[idxMax, 0]:
            idxMax = i
        elif arrayPoints[i, 0] == arrayPoints[idxMin, 0]:
            if arrayPoints[i, 1] > arrayPoints[idxMin, 1]:
                idxMin = i
    return idxMin, idxMax

# return left and right indexes
def divide(i1, i2, s, arrayPoints):
    s1 = []
    s2 = []
    p1 = arrayPoints[i1]
    p2 = arrayPoints[i2]
    for i3 in s:
        p3 = arrayPoints[i3]
        # left
        if determinant(p1, p2, p3) > 0.0000001: # avoid calculation error
            s1.append(i3)
        # right
        elif determinant(p1, p2, p3) < -0.0000001: # avoid calculation error
            s2.append(i3)
    s1 = np.array(s1)
    s2 = np.array(s2)
    return s1, s2            

# Return determinant of 3 points (1 line & 1 point)
def determinant(p1, p2, p3):
    x1 = p1[0]
    x2 = p2[0]
    x3 = p3[0]
    y1 = p1[1]
    y2 = p2[1]
    y3 = p3[1]
    return x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3

# Calculate distance of point to line
def PointToLineDistance(p1, p2, px):

    # equation of line
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = -(a*(p1[0]) + b*(p1[1]))
    # ax + by + C = 0
    a /= b
    c /= b
    b = 1
    xx = px[0]
    yx = px[1]
    return abs(a*xx + b*yx + c)/math.sqrt(a**2 + b**2)
