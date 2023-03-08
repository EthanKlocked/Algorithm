def solution(s, skip, index):
    chkList = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in skip]
    return ''.join([chkList[(chkList.index(c) + index) % len(chkList)] if c not in skip else c for c in s])
