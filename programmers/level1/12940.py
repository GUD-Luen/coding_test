def solution(n, m):
    a = max(n, m)
    b = min(n, m)
    r0 = a
    r1 = b
    while r1 != 0:
        tmp = r0 % r1
        r0 = r1
        r1 = tmp
    gcd = r0
    lcm = int(a * b / gcd)

    return [gcd, lcm]