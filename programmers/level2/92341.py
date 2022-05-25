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