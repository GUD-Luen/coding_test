def solution(N, stages):
    stage_dic = {}
    stage_arrive_list = [0] * N
    for stage in stages:
        for i in range(stage if stage <= N else N):
            tmp = stage_arrive_list[i] + 1
            stage_arrive_list[i] = tmp
        if stage in stage_dic:
            tmp = stage_dic.get(stage) + 1
            stage_dic[stage] = tmp
        else:
            stage_dic[stage] = 1

    stage_fail_dic = {}

    for i in range(N):
        fail = 0
        if stage_arrive_list[i] != 0:
            fail = stage_dic.get(i + 1, 0) / stage_arrive_list[i]
        tmp = stage_fail_dic.get(fail, [])
        tmp += [i + 1]
        stage_fail_dic[fail] = tmp

    stage_fail_list = list(stage_fail_dic.items())
    stage_fail_list.sort()
    stage_fail_list.reverse()
    answer = []
    for stage_fail in stage_fail_list:
        stage_list = stage_fail[1]
        stage_list.sort()
        answer += stage_list
    return answer