def solution(numbers):
    hap_set = set([])
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            hap_set.add(numbers[i]+numbers[j])
    answer = list(hap_set)
    answer.sort()
    return answer