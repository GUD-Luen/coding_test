def solution(s):
    unit = len(s) // 2
    answer = len(s)
    while unit > 0:
        min_length = len(s)
        start = 0
        end = start + unit
        pre = ''
        continue_count = 1
        while end <= len(s):
            tmp = s[start:end]
            if tmp == pre:
                min_length -= unit
                continue_count += 1
            else:
                pre = tmp
                if continue_count != 1:
                    min_length += len(str(continue_count))
                    continue_count = 1
            start = end
            end = start + unit

        if continue_count != 1:
            min_length += len(str(continue_count))

        if min_length < answer:
            answer = min_length
        unit -= 1

    return answer