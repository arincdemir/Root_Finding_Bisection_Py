import math

# Give a lambda function such as:
# lambda x: x**4 - math.cos(x) - 5
def rootfinder(func, startX: float=-1000000, endX: float=1000000, maxIterations: int=120):
    positive = 0
    negative = 0
    midXVal = 0
    if(func(startX) > 0):
        positive = startX
        negative = endX
    else:
        positive = endX
        negative = startX

    for i in range(maxIterations):
        midX = (positive + negative) / 2
        midXVal = func(midX)
        if(midXVal > 0):
            positive = midX
        elif(midXVal < 0):
            negative = midX
        else:
            break

    return midX
