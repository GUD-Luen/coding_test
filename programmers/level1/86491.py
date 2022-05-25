def solution(sizes):
    weight_max = 0
    height_max = 0
    for size in sizes:
        if size[0] < size[1]:
            tmp = size[0]
            size[0] = size[1]
            size[1] = tmp
        if weight_max < size[0]:
            weight_max = size[0]
        if height_max < size[1]:
            height_max = size[1]
    answer = weight_max * height_max
    return answer