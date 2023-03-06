def solution(n, m, section):
    painted = 0
    return sum(1 for v in section if v > painted and (painted := v + m - 1))
