import math


def score(x, y):
    toss_score = 0
    d_circle = math.sqrt((x**2) + (y**2))
    if d_circle <= 1:
        toss_score = 10
    elif d_circle <= 5:
        toss_score = 5
    elif d_circle <= 10:
        toss_score = 1
    return toss_score

print(score(-9, 9))
