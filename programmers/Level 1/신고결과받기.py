def solution(id_list, report, k):
    chk, cnt, report, answer = {}, {}, list(set(report)), []
    for key in id_list:
        chk[key], cnt[key] = set(), 0
        answer.append(0)
    for dt in report:
        dt_li = dt.split()
        chk[dt_li[0]].add(dt_li[1])
        cnt[dt_li[1]] += 1
    for i in dict(filter(lambda e: e[1] >=k, cnt.items())):
        for i2 in range(len(list(chk.values()))):
            if i in list(chk.values())[i2]: answer[i2] += 1
    return answer
