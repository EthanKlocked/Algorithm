from collections import deque 

def bfs(start, maps, chkList):
    total = int(maps[start[0]][start[1]])
    chkList[start[0]][start[1]] = True
    dq = deque([start])
    while dq:
        y, x = dq.popleft()
        for ny, nx in [(y+dy, x+dx) for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]]:
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not chkList[ny][nx] and maps[ny][nx] != "X":
                dq.append((ny, nx))
                chkList[ny][nx] = True
                total += int(maps[ny][nx])      
    return total            
        
def solution(maps):
    answer = []
    chkList = [[False]*len(maps[0]) for _ in range(len(maps))]
    for y, row in enumerate(maps):
        for x, val in enumerate(row):
            if not chkList[y][x] and val != "X":
                answer.append(bfs((y,x), maps, chkList))
    answer.sort()
    return answer if answer else [-1]
