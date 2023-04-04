def solution(plans):
    answer = []
    stack = []
    plans.sort(key=lambda x:x[1])
    for i in range(len(plans)):
        if i == len(plans)-1:
            answer.append(plans[i][0])
            finalStack = [j[0] for j in stack]
            finalStack.reverse()
            if stack : answer += finalStack
            return answer
        n1 = 60*int(plans[i][1][0:2]) + int(plans[i][1][3:])
        n2 = 60*int(plans[i+1][1][0:2]) + int(plans[i+1][1][3:])
        gap = n2 - (n1 + int(plans[i][2]))
        if gap < 0 : stack.append((plans[i][0], gap))
        else:
            answer.append(plans[i][0])
            if gap > 0 : 
                while stack:
                    item = stack.pop()
                    offset = item[1] + gap
                    if offset > 0:
                        answer.append(item[0])        
                        gap = offset
                    else :                    
                        if offset < 0 : stack.append((item[0], offset))
                        if offset == 0 : answer.append(item[0])        
                        break
