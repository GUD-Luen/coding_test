def solution(n):
    sam_list = []
    while n != 0:
        sam_list.append(n % 3)
        n = n // 3
    sam_list.reverse()
    factor = 1
    answer = 0
    for sam in sam_list:
        answer += sam * factor
        factor = factor * 3

    return answer