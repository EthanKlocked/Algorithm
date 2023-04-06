def solution(weights):
    answer = 0
    memo = {}
    keyCnt = {}
    li = [[i, 2*i, 3*i, 4*i] for i in weights]
    for i in li:
        if i[0] in keyCnt : keyCnt[i[0]] += 1
        else: keyCnt[i[0]] = 0
        for j in i[1:]:
            if j in memo: 
                answer += memo[j]
                memo[j] += 1
            else: memo[j] = 1
    for i in keyCnt.values(): 
        if i > 0 : answer -= (i+1)*i
    return answer
