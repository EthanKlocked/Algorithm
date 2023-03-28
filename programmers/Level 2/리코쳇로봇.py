from collections import deque

def straight(p, d, board):
    point = p
    while True:
        y = point[0] + d[0]
        x = point[1] + d[1]
        if not (0<=y<len(board) and 0<=x<len(board[0])) or board[y][x] == "D": return (point[0], point[1])
        point = (y, x)
        
def solution(board):
    moveSet = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for i, iv in enumerate(board):
        if "R" in iv : 
            start = (i, iv.index("R"), 1)
            break
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in moveSet:
            point = (v[0], v[1])
            edge = straight(point, i, board)
            if point != edge :
                if board[edge[0]][edge[1]] == "G" : return v[2]
                if board[edge[0]][edge[1]] in ["C", "R"] : continue
                board[edge[0]] = board[edge[0]][:edge[1]] + "C" + board[edge[0]][edge[1]+1:]
                queue.append(edge+tuple([v[2]+1]))
    return -1
