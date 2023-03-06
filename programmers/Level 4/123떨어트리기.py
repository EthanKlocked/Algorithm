from collections import deque

level = {}
visitChk = {}
number = [3,2,1]

def nodeSrch(l): 
    if not l in level: return l
    next = level[l].popleft()
    level[l].append(next)
    return nodeSrch(next)

def divideChk(arr):
    chkOrder = [2,3]
    for c in chkOrder:
        if c in arr: 
            arr[arr.index(c)] = 1
            return c-1
    return False        

def solution(edges, target): 
    answer = []
    edges.sort()
    for i in edges :
        if not i[0] in level : level[i[0]] = deque([])
        level[i[0]].append(i[1])
    while any(target) : 
        endPoint = nodeSrch(1)-1
        maxPoint = 0
        answer.append(endPoint)
        for j in number:
            if target[endPoint] >= j: 
                maxPoint = j    
                break
        target[endPoint] = target[endPoint] - maxPoint
        if not endPoint in visitChk:
            if maxPoint == 0 : return [-1]
            visitChk[endPoint] = [maxPoint]
        else:
            if maxPoint == 0:
                maxPoint = divideChk(visitChk[endPoint])
                if not maxPoint : return [-1]
            visitChk[endPoint].append(maxPoint)
    for l in range(len(answer)):
        #if 0 in visitChk[answer[l]]: return [-1]
        minValue = min(visitChk[answer[l]])
        visitChk[answer[l]].remove(minValue)
        answer[l] = minValue
    return answer
