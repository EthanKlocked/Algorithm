import heapq

def solution(scoville, K): # execute func
    heapq.heapify(scoville)
    cnt = 0
    for i in range(len(scoville)):
        i = 0        
        if scoville[i] >= K :
            break
        elif len(scoville) == 1:
            cnt = -1
        else:
            heapq.heappush(scoville, (heapq.heappop(scoville) + heapq.heappop(scoville) * 2))
            cnt += 1
    return cnt