def solution(s):
    answer = []
    s = s.replace('{{', '').replace('}}', '')
    a_list = s.split('},{')
    set_len_dic = {}
    for a in a_list:
        tmp = eval('{' + a + '}')
        set_len_dic[len(tmp)] = tmp
    for i in range(len(a_list)):
        if i == 0:
            answer.append(list(set_len_dic[1])[0])
        else:
            tmp = set_len_dic[i+1] - set_len_dic[i]
            answer.append(list(tmp)[0])
    return answer