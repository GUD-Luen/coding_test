def solution(n):
    answer = []
    is_continue = True
    while is_continue:
        answer.append(n % 10)
        n = n // 10
        if n == 0:
            is_continue = False
    return answer