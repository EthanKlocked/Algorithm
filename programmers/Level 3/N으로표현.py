def solution(N, number):
    idx = ['+','-','*','/']
    box = ['']
    max_cnt = 9
    for i in range(1, 9):
        if int(str(N) * i) == number : return i
        box.append([str(N) * i])
    
    for j in range(1, len(box)-1): # outer
        for o in range(len(box[j])): # inner
            for k in range(1, len(box)-1): # outer
                if j+k >= max_cnt : break
                for h in range(len(box[k])): # inner
                    for m in idx:
                        now_form = box[j][o] + m + box[k][h]
                        if int(eval(now_form)) == number and max_cnt > j+k : max_cnt = j+k
                        if int(eval(now_form)) != 0 and str(int(eval(now_form))) not in box[j+k] : box[j+k].append(str(int(eval(now_form))))
    return max_cnt if max_cnt < 9 else -1
