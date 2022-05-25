def solution(arr):
    answer = []
    pre = -1
    for num in arr:
        if num != pre:
            answer.append(num)
            pre = num
    return answer