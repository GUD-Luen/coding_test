def m_function(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return n * 3 + 1


def solution(num):
    answer = 0
    if num == 1:
        return answer
    while answer < 500:
        num = m_function(num)
        answer += 1
        if num == 1:
            return answer
    return -1