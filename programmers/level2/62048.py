def solution(w, h):
    a = max(w, h)
    b = min(w, h)
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return w * h - w - h + a