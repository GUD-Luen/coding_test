month_day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']


def solution(a, b):
    days = b
    if a != 1:
        for i in range(a - 1):
            days += month_day_list[i]
    answer = week[days % 7]
    return answer