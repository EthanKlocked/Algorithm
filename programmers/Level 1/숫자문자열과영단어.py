def solution(s):
    chk_box = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = ''
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            for k in range(len(chk_box)):
                if chk_box[k][0] == s[i] and chk_box[k][1] == s[i+1]:
                    answer += str(k)
                    i += len(chk_box[k])
                    if i >= len(s):
                        return int(answer)
                    break
    return int(answer)