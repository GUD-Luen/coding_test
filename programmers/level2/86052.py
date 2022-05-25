import time


def solution(grid):
    answer = []
    pos_dir_dic = {}
    max_x = len(grid)
    max_y = len(grid[0])
    for i in range(max_x):
        for j in range(max_y):
            pos_dir_dic[(i, j, 'U')] = 0
            pos_dir_dic[(i, j, 'D')] = 0
            pos_dir_dic[(i, j, 'L')] = 0
            pos_dir_dic[(i, j, 'R')] = 0
    pos_dir_list = list(pos_dir_dic.keys())
    for pos_dir in pos_dir_list:
        if pos_dir_dic[pos_dir] == 0:
            cnt = 1
            pos_dir_dic[pos_dir] = 1
            direction = pos_dir[2]
            position = move([pos_dir[0], pos_dir[1]], direction, max_x, max_y)
            direction = new_direction(grid[position[0]][position[1]], direction)
            pos_dir_dic[(position[0], position[1], direction)] = 1
            while position != [pos_dir[0], pos_dir[1]] or direction != pos_dir[2]:
                position = move(position, direction, max_x, max_y)
                direction = new_direction(grid[position[0]][position[1]], direction)
                pos_dir_dic[(position[0], position[1], direction)] = 1
                cnt += 1
            answer.append(cnt)
    return sorted(answer)


def move(position, direction, max_x, max_y):
    new_x = position[0]
    new_y = position[1]
    if direction == 'U':
        new_x -= 1
        if new_x < 0:
            new_x += max_x
    elif direction == 'D':
        new_x += 1
        if new_x == max_x:
            new_x -= max_x
    elif direction == 'L':
        new_y -= 1
        if new_y < 0:
            new_y += max_y
    elif direction == 'R':
        new_y += 1
        if new_y == max_y:
            new_y -= max_y
    return list([new_x, new_y])


def new_direction(indication, direction):
    if indication == 'S':
        pass
    elif indication == 'L':
        if direction == 'U':
            direction = 'L'
        elif direction == 'D':
            direction = 'R'
        elif direction == 'L':
            direction = 'D'
        elif direction == 'R':
            direction = 'U'
    elif indication == 'R':
        if direction == 'U':
            direction = 'R'
        elif direction == 'D':
            direction = 'L'
        elif direction == 'L':
            direction = 'U'
        elif direction == 'R':
            direction = 'D'
    return direction


test_case_list = [
    ["SL", "LR"],
    ["S"],
    ["R", "R"],
]

start_time = time.time()

for test_case in test_case_list:
    print(solution(test_case))

print(round((time.time() - start_time) * 1000, 6), 'ms')
