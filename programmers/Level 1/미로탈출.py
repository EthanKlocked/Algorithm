from collections import deque 

def bfs(start, target, md):
    moveset = [(0,1),(1,0),(0,-1),(-1,0)]
    mc = {(i,j):-1 for i in range(len(md)) for j in range(len(md[0]))}
    mc[start] = 0
    dq = deque([start])
    while dq:
        p = dq.popleft()
        if p == target: return mc[p]
        for m in moveset:
            y, x = p[0]+m[0], p[1]+m[1]
            if not (0 <= y < len(md) and 0 <= x < len(md[0]) and md[y][x] != "X" and mc[y,x] == -1): continue
            mc[y,x] = mc[p]+1
            dq.append((y,x))
    return -1

def solution(maps):
    s, l, e = None, None, None
    for i, row in enumerate(maps):
        if "S" in row: s = (i, row.index("S"))
        if "L" in row: l = (i, row.index("L"))
        if "E" in row: e = (i, row.index("E"))
    sl = bfs(s, l, maps)
    le = bfs(l, e, maps)
    return sl+le if sl != -1 and le != -1 else -1
