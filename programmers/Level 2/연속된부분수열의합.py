def solution(sequence, k):
    last = len(sequence)-1
    sequence.reverse()
    total = 0
    start = -1
    for i, iv in enumerate(sequence):
        total += iv 
        if start < 0 : start = i
        if total > k : 
            total -= sequence[start]
            start += 1
        if total == k and (i == last or sequence[i+1] != sequence[start]): return [last-i, last-start]
