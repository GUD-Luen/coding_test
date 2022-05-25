def solution(s):
    s_list = list(s)
    s_list.sort()
    s_list.reverse()
    answer = ''
    for c in s_list:
        answer += c
    return answer