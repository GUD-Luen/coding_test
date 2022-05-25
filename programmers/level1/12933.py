def solution(n):
    num_list = []
    is_continue = True
    while is_continue:
        num_list.append(n % 10)
        n = n // 10
        if n == 0:
            is_continue = False
    num_list.sort()
    factor = 1
    answer = 0
    for num in num_list:
        answer += num * factor
        factor = factor * 10

    return answer