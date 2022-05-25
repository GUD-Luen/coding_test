import time


def solution(lottos, win_nums):
    match_count = 0
    for num in win_nums:
        match_count += lottos.count(num)
    min_rank = 7 - match_count
    max_rank = 7 - match_count - lottos.count(0)

    if min_rank > 6:
        min_rank = 6
    if max_rank > 6:
        max_rank = 6

    answer = [max_rank, min_rank]

    return answer


test_case_list = [
    [[44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]],
]

start_time = time.time()

for test_case in test_case_list:
    print(solution(test_case[0], [1]))

print(round((time.time() - start_time) * 1000, 6), 'ms')

