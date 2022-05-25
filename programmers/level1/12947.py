def solution(arr):
    return arr % sum(int(num) for num in list(str(arr))) == 0