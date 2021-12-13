global cnt #global count
cnt = 0

def solution(numbers, target):
    graph = list([int(n), -int(n)] for n in numbers)
    search(0, graph, 0, target)
    answer = cnt
    return answer

def search(idx, gr, sum_chk, tar):
    if idx != len(gr)-1: # case : not the last
        for i in gr[idx]:
            new_sum = sum_chk
            new_sum += i
            search(idx+1, gr, new_sum, tar)
    else: # case : the last
        for i in gr[idx]:
            new_sum = sum_chk            
            new_sum += i
            if new_sum == tar:
                global cnt 
                cnt += 1