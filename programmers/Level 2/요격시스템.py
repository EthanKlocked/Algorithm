def solution(targets):
    targets.sort(key=lambda x : x[1])
    end = targets[0][1]
    answer = 1
    for i, iv in enumerate(targets):
        if iv[0] >= end : 
            end = iv[1]
            answer += 1        
    return answer
