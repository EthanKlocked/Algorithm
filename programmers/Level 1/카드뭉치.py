def solution(cards1, cards2, goal):
    for c in goal:
        if cards1 and c == cards1[0]: cards1 = cards1[1:]
        elif cards2 and c == cards2[0]: cards2 = cards2[1:]
        else: return "No"
    return "Yes"
