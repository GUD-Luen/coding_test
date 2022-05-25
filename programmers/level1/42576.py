def solution(participant, completion):
    name_dic = {}
    for name in participant:
        if name in name_dic:
            tmp = name_dic[name]
            tmp += 1
            name_dic[name] = tmp
        else:
            name_dic[name] = 1

    for name in completion:
        if name_dic[name] == 1:
            del name_dic[name]
        else:
            tmp = name_dic[name]
            tmp -= 1
            name_dic[name] = tmp
    tmp_list = list(name_dic.keys())
    answer = tmp_list[0]
    return answer