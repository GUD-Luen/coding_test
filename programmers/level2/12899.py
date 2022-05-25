def solution(n):
    answer = []
    b = n
    while b != 0:
        if b % 3 == 0:
            a = 4
            b = b // 3 - 1
        else:
            a = b % 3
            b = b // 3
        answer.append(a)
    answer.reverse()
    return ''.join(str(num) for num in answer)