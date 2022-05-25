def solution(n, lost, reserve):
    answer = n - len(lost)
    reserve_dic = {}
    for res in reserve:
        reserve_dic[res] = 1

    for i in reversed(range(len(lost))):
        if reserve_dic.get(lost[i], 0) == 1:
            answer += 1
            reserve_dic[lost[i]] = 0
            del lost[i]

    lost.sort()

    for num in lost:
        if reserve_dic.get(num - 1, 0) == 1:
            answer += 1
            reserve_dic[num - 1] = 0
            continue
        if reserve_dic.get(num + 1, 0) == 1:
            answer += 1
            reserve_dic[num + 1] = 0

    return answer