def solution(lottos, win_nums):
    d = [0]*45
    min_cnt = 7
    max_cnt = 7
    for win in win_nums:
        d[win-1] += 1
        
    for my in lottos:
        if my == 0:
            max_cnt -= 1
        elif d[my-1] == 1:
            min_cnt -= 1
            max_cnt -= 1
    min_cnt = 6 if min_cnt == 7 else min_cnt
    max_cnt = 6 if max_cnt == 7 else max_cnt
    answer = [max_cnt, min_cnt]
    return answer