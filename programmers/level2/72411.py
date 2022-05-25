from itertools import combinations


def solution(orders, course):
    answer = []
    for num in course:
        course_dic = {}
        for order in orders:
            if len(order) < num:
                continue
            for order_com in list(combinations(list(order), num)):
                order_str = "".join(sorted(order_com))
                if order_str in course_dic:
                    tmp = course_dic[order_str]
                    tmp += 1
                    course_dic[order_str] = tmp
                else:
                    course_dic[order_str] = 1
        course_list = list(course_dic.items())
        max_num = 1
        for key, value in course_list:
            if value > max_num:
                max_num = value
        if max_num != 1:
            for key, value in course_list:
                if value == max_num:
                    answer.append(key)

    return sorted(answer)