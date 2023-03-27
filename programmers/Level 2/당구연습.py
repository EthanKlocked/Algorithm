def solution(m, n, startX, startY, balls):
    answer = []
    for b in balls:
        left = (startX+b[0])**2 + abs(startY - b[1])**2 if not (startY == b[1] and startX > b[0]) else 12500000
        right = (2*m-(startX+b[0]))**2 + abs(startY - b[1])**2 if not (startY == b[1] and startX < b[0]) else 12500000
        up = (2*n-(startY+b[1]))**2 + abs(startX - b[0])**2 if not (startX == b[0] and startY < b[1]) else 12500000
        down = (startY+b[1])**2 + abs(startX - b[0])**2 if not (startX == b[0] and startY > b[1]) else 12500000
        answer.append(min(left, right, up, down))    
    return answer
