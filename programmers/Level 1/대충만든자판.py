def solution(keymap, targets):
    inf = 100
    answer = []
    memo = {}
    def search(t):
        total = 0
        for letter in t:
            cnt = inf
            if letter in memo: cnt = memo[letter]
            else:
                for key in keymap:
                    keyIndex = key.find(letter)+1
                    if keyIndex > 0: cnt = min(cnt, keyIndex)
                memo[letter] = cnt
            if cnt == inf: return -1
            total += cnt
        return total                
    for target in targets:
        answer.append(search(target))
    return answer
