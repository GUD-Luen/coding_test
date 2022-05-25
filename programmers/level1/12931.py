def solution(n):
    answer = 0
    is_continue = True
    while is_continue:
        answer += n % 10
        n = n // 10
        if n == 0:
            is_continue = False

    return answer