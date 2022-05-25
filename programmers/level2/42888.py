def solution(record):
    id_nick_dic = {}
    in_out_id_list = []
    for info in record:
        info_list = info.split(' ')
        if info_list[0] == 'Change':
            id_nick_dic[info_list[1]] = info_list[2]
        elif info_list[0] == 'Enter':
            id_nick_dic[info_list[1]] = info_list[2]
            in_out_id_list.append(['in', info_list[1]])
        else:
            in_out_id_list.append(['out', info_list[1]])

    answer = []
    for in_out_id in in_out_id_list:
        if in_out_id[0] == 'in':
            answer.append(id_nick_dic[in_out_id[1]] + '님이 들어왔습니다.')
        else:
            answer.append(id_nick_dic[in_out_id[1]] + '님이 나갔습니다.')
    return answer