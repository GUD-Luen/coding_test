def solution(n):
    is_prime_list = [1] * (n + 1)
    is_prime_list[0] = 0
    is_prime_list[1] = 0
    for i in range(1, int(n ** 0.5)+1):
        if is_prime_list[i] == 1:
            j = 2 * i
            while j < len(is_prime_list):
                is_prime_list[j] = 0
                j += i

    return sum(is_prime_list)