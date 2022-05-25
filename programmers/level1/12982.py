def solution(d, budget):
    d.sort()
    answer = 0
    for a in d:
        if a <= budget:
            answer += 1
            budget -= a
        else:
            break
    return answer