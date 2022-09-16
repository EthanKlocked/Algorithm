from heapq import heapify, heappush, heappop

def solution(n, works):
    heap = [-a for a in works]
    heapify(heap)
    for i in range(n):    
        num = heappop(heap) + 1
        if(num > 0): return 0
        heappush(heap, num)
    answer = 0
    for i2 in heap: answer += i2 ** 2
    return answer
