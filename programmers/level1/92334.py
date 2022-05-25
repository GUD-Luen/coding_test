import time


def solution(id_list, reports, k):

    report_set = set(reports)
    report_list = list(report_set)

    id_report_dic = {}
    id_mail_dic = {}
    for user_id in id_list:
        id_report_dic[user_id] = []
        id_mail_dic[user_id] = 0

    for report in report_list:
        _report = report.split(' ')
        tmp_list = id_report_dic[_report[1]]
        tmp_list.append(_report[0])
        id_report_dic[_report[1]] = tmp_list

    for user_id in id_list:
        if len(id_report_dic[user_id]) >= k:
            for report_id in id_report_dic[user_id]:
                id_mail_dic[report_id] += 1

    answer = []
    for user_id in id_list:
        answer.append(id_mail_dic[user_id])

    return answer


test_case_list = [
    [["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2],
    [["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3],
]

start_time = time.time()

for test_case in test_case_list:
    print(solution(test_case[0], test_case[1], test_case[2]))

print(round((time.time() - start_time) * 1000, 6), 'ms')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
