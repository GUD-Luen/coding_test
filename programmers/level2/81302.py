def solution(places):
    answer = []
    for place in places:
        is_break = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if i < 4:
                        if place[i + 1][j] == 'P':
                            answer.append(0)
                            is_break = True
                            break
                    if i < 3:
                        if place[i + 2][j] == 'P':
                            if place[i + 1][j] == 'X':
                                pass
                            else:
                                answer.append(0)
                                is_break = True
                                break
                    if j < 4:
                        if place[i][j + 1] == 'P':
                            answer.append(0)
                            is_break = True
                            break
                    if j < 3:
                        if place[i][j + 2] == 'P':
                            if place[i][j + 1] == 'X':
                                pass
                            else:
                                answer.append(0)
                                is_break = True
                                break
                    if i < 4 and j < 4:
                        if place[i + 1][j + 1] == 'P':
                            if place[i][j + 1] == 'X' and place[i + 1][j] == 'X':
                                pass
                            else:
                                answer.append(0)
                                is_break = True
                                break
                    if i < 4 and j > 0:
                        if place[i + 1][j - 1] == 'P':
                            if place[i][j - 1] == 'X' and place[i + 1][j] == 'X':
                                pass
                            else:
                                answer.append(0)
                                is_break = True
                                break
            if is_break:
                break
        if not is_break:
            answer.append(1)
    return answer