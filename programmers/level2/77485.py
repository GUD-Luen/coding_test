def solution(rows, columns, queries):
    answer = []
    square = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(i * columns + j + 1)
        square.append(row)

    for query in queries:
        x1 = query[0] - 1
        y1 = query[1] - 1
        x2 = query[2] - 1
        y2 = query[3] - 1
        first_num = square[x1][y1]
        square[x1][y1] = square[x1 + 1][y1]
        min_num = square[x1][y1]
        next_num = first_num
        i = x1
        j = y1 + 1
        while not (i == x1 and j == y1):
            pre_num = next_num
            min_num = min(min_num, pre_num)
            next_num = square[i][j]
            square[i][j] = pre_num
            if i == x1:
                if j != y2:
                    j += 1
                else:
                    i += 1
            elif i != x2 and j == y2:
                i += 1
            elif j != y1:
                j -= 1
            else:
                i -= 1
        answer.append(min_num)
    return answer