def is_square(num):
    hex_num = num & 0xf  # 16진수 일의 자리만 추출
    if hex_num == 0 or hex_num == 1 or hex_num == 4 or hex_num == 9:
        tmp = num ** 0.5
        if int(tmp) ** 2 == num:
            return -1
    return 1


def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        answer += is_square(num) * num
    return answer