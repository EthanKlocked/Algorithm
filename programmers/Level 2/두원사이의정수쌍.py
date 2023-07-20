import math
def solution(r1, r2):
    cnt = 0
    for i in range(1, r2):
        top = math.ceil(math.sqrt(r2**2 - i**2))
        if math.sqrt(r2**2 - i**2).is_integer() : top += 1
        bottom = 0
        if i < r1 : bottom = math.ceil(math.sqrt(r1**2 - i**2))
        cnt += top - bottom
    return 4*(cnt+1)
