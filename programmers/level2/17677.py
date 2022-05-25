import re
from math import floor


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = []
    str2_list = []
    p = re.compile('[a-z]{2}')
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        m = p.match(tmp)
        if m:
            str1_list.append(tmp)
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        m = p.match(tmp)
        if m:
            str2_list.append(tmp)
    if not str1_list and not str2_list:
        return 65536

    union_cnt = len(str1_list)
    intersection_cnt = 0
    for cs in str2_list:
        if cs in str1_list:
            str1_list.remove(cs)
            intersection_cnt += 1
        else:
            union_cnt += 1
    answer = intersection_cnt / union_cnt * 65536
    return floor(answer)