def solution(board):    
    oSet = set([(i, j) for i, row in enumerate(board) for j, char in enumerate(row) if char == "O"])
    xSet = set([(i, j) for i, row in enumerate(board) for j, char in enumerate(row) if char == "X"])
    winList = [set([(0, 0),(1, 1),(2, 2)]), set([(0, 2),(1, 1),(2, 0)])]
    for i in range(3):
        winList.append(set([(i, j) for j in range(3)]))
        winList.append(set([(j, i) for j in range(3)]))
    def check(o, x):
        ol = len(o)
        xl = len(x)
        if ol < xl : return 0
        if ol - xl > 1: return 0
        for i in winList:
            if (o and i-o == set()) and ol == xl: return 0
            if (x and i-x == set()) and ol > xl: return 0            
        return 1
    return check(oSet, xSet)
