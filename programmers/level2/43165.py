from itertools import combinations


def solution(numbers, target):
    answer = 0
    for i in range(len(numbers)):
        for index_list in list(combinations(range(len(numbers)), i)):
            num_list = list(numbers)
            for index in index_list:
                num_list[index] = -num_list[index]
            if sum(num_list) == target:
                answer += 1
    return answer