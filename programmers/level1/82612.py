def solution(price, money, count):
    answer = count * (count + 1) / 2 * price - money
    return answer if answer > 0 else 0