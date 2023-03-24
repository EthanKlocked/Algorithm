def solution(picks, minerals):
    level = {"diamond" : [25, picks[0]], "iron" : [5, picks[1]], "stone" : [1, picks[2]]}
    groupNum = []
    order = []
    eachSum = 0
    oIndex = 0
    answer = 0
    order = [''] * sum(picks)
    
    for i in range(0, len(minerals), 5):
        group_sum = sum(level[mineral][0] for mineral in minerals[i:i+5])
        groupNum.append((group_sum, len(groupNum)))
    groupNum.sort(reverse=True)
    
    for group_sum, group_index in groupNum:
        if group_index >= len(order): continue
        for pick in ["diamond", "iron", "stone"]:
            if level[pick][1] > 0:
                level[pick][1] -= 1
                order[group_index] = pick
                break
    
    for mi, mineral in enumerate(minerals):
        key = order[oIndex]
        addPoint = level[mineral][0] // level[key][0]
        if addPoint == 0 : addPoint = 1
        answer += addPoint
        if(mi+1)%5 == 0 : oIndex += 1
        if oIndex >= len(order) : break
        
    return answer
