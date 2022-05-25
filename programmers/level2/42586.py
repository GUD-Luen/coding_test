def solution(progresses, speeds):
    answer = []
    progress_speed_list = []
    for i in range(len(progresses)):
        progress_speed_list.append([progresses[i], speeds[i]])

    yet_count = len(progress_speed_list)
    in_progress = 0
    while yet_count > 0:
        for progress_speed in progress_speed_list:
            if progress_speed[0] < 100:
                progress_speed[0] += progress_speed[1]
        if progress_speed_list[in_progress][0] >= 100:
            update_count = 0
            while progress_speed_list[in_progress][0] >= 100:
                update_count += 1
                yet_count -= 1
                if yet_count > 0:
                    in_progress += 1
                else:
                    break
            answer.append(update_count)

    return answer