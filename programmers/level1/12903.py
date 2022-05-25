import math


def solution(s):
    return s[int(math.floor((len(s) - 1) / 2)):int(math.ceil((len(s) + 1) / 2))]