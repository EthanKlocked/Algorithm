def solution(players, callings):
    memo = {iv:i for i,iv in enumerate(players)}
    for i in callings:
        nowId = memo[i]
        front = players[nowId-1]
        rear = players[nowId]
        players[nowId-1], players[nowId] = players[nowId], players[nowId-1]
        memo[front] = nowId
        memo[rear] = nowId-1
    return players
