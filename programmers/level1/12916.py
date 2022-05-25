def solution(s):
    s = s.lower()
    a = 0
    for c in s:
        if c == 'p':
            a += 1
        elif c == 'y':
            a += -1
    return a == 0