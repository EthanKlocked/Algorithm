def solution(wallpaper):
    pList = [(i, j) for i, row in enumerate(wallpaper) for j, char in enumerate(row) if char == "#"]
    return [min(p[0] for p in pList), min(p[1] for p in pList), max(p[0] for p in pList)+1, max(p[1] for p in pList)+1]
