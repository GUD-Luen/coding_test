def solution(dart_result):
    point = []
    i = 0
    while i < len(dart_result):
        if dart_result[i].isnumeric():
            if dart_result[i + 1].isnumeric():
                tmp = int(dart_result[i]) * 10 + int(dart_result[i + 1])
                point.append(tmp)
                i += 1
            else:
                point.append(int(dart_result[i]))
        elif dart_result[i] == 'D':
            tmp = point.pop()
            point.append(tmp ** 2)
        elif dart_result[i] == 'T':
            tmp = point.pop()
            point.append(tmp ** 3)
        elif dart_result[i] == '*':
            tmp1 = point.pop()
            if len(point) > 0:
                tmp2 = point.pop()
                point.append(tmp2 * 2)
            point.append(tmp1 * 2)
        elif dart_result[i] == '#':
            tmp1 = point.pop()
            point.append(-tmp1)
        i += 1

    return sum(point)