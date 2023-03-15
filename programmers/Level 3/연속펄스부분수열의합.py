def solution(sequence):
    dp = [0]
    init = 1
    for i in range(len(sequence)):
        init = -init
        dp.append(dp[-1]+(init*sequence[i]))
    return abs(max(dp)-min(dp))
