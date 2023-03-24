def solution(park, routes):
    moveSet = {"E":(0, 1), "W":(0, -1), "N":(-1, 0), "S":(1, 0)}
    answer = [[i, j.index('S')] for i, j in enumerate(park) if 'S' in j][0]
    for j in routes:
        direction = moveSet[j[0]]
        y, x = answer
        for _ in range(int(j[1:])):
            y += direction[0]
            x += direction[1]
            if not (0 <= y < len(park) and 0 <= x < len(park[0])) or park[y][x] == 'X':
                break
        else: answer = [y, x]
    return answer
