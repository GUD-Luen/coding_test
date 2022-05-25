import time


def solution(fees, records):
    basic_time = fees[0]
    basic_fee = fees[1]
    over_time_unit = fees[2]
    over_fee = fees[3]

    car_set = set()
    car_time_dic = {}

    for record in records:
        record_time = record[0:5]
        record_car = record[6:10]
        car_set.add(record_car)
        if record_car in car_time_dic:
            tmp_list = car_time_dic[record_car]
            tmp_list.append(record_time)
            car_time_dic[record_car] = tmp_list
        else:
            car_time_dic[record_car] = [record_time]

    car_list = list(car_set)
    car_list.sort()
    answer = []

    for car in car_list:
        total_fee = basic_fee
        total_time = 0
        time_list = car_time_dic[car]
        for i in range(len(time_list)):
            if i % 2 == 0:
                total_time -= int(time_list[i][:2]) * 60 + int(time_list[i][3:])
            else:
                total_time += int(time_list[i][:2]) * 60 + int(time_list[i][3:])

        if len(time_list) % 2 == 1:
            total_time += 23 * 60 + 59
        total_time -= basic_time
        if total_time > 0:
            over_time_fact = total_time // over_time_unit if total_time % over_time_unit == 0 else total_time // over_time_unit + 1
            total_fee += over_fee * over_time_fact

        answer.append(total_fee)

    return answer


test_case_list = [
    [[180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]],
    [[120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]],
    [[1, 461, 1, 10], ["00:00 1234 IN"]],
]

start_time = time.time()

for test_case in test_case_list:
    print(solution(test_case[0], test_case[1]))

print(round((time.time() - start_time) * 1000, 6), 'ms')
