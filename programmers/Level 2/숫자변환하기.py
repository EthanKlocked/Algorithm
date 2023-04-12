def solution(x, y, n):
    li = [1000001]*(y+1)
    li[x] = 0
    for i in range(1, y+1):
        if i-n > 0 : li[i] = min(li[i], li[i-n]+1)
        if i%2 == 0 : li[i] = min(li[i], li[int(i/2)]+1)
        if i%3 == 0 : li[i] = min(li[i], li[int(i/3)]+1)
    return li[y] if li[y] < 1000001 else -1
