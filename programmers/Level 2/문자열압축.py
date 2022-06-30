def solution(s):
    answer = len(s)
    for i in range(int(len(s)/2)):
        unit = i+1
        cnt = 1
        encoded = ''
        for k in range(0, len(s), unit):     
            now = s[k:k+unit]
            after = s[k+unit:k+unit*2]
            if(now == after) : cnt += 1                
            else:
                encoded += (str(cnt) if cnt > 1 else '') + now
                cnt = 1
            if(not s[k+unit*2:]) : 
                encoded += str(cnt) + now if(now == after) else after
                break
        if len(encoded) < answer : answer = len(encoded)
    return answer
