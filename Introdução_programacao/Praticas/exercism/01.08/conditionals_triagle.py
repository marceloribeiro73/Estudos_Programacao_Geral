#%%
def checkIsTriangle(sides):
    output = False
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a+b+c == 0:
        return output
    elif (a+b >= c) and (b+c >= a) and (a+c >= b):
        output = True
    else:
        return output
    return output
    

def equilateral(sides):
    output = False
    if checkIsTriangle(sides) == False:
        return output
    if sides[0] == sides[1] and sides[1]==sides[2]:
        output = True
    return output


def isosceles(sides):
    output = False
    if checkIsTriangle(sides) == False:
        return output
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        output = True
    return output


def scalene(sides):
    output = False
    if checkIsTriangle(sides) == False:
        return output
    if sides[0] != sides[1] and sides[1] != sides[2] and sides[2] !=sides[0] :
        output = True
    return output
#%%
isosceles([1, 1, 3])