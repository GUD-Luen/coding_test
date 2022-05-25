position_dic = {1: [1, 1], 2: [1, 2], 3: [1, 3], 4: [2, 1], 5: [2, 2], 6: [2, 3], 7: [3, 1], 8: [3, 2], 9: [3, 3], 0: [4, 2]}


def solution(numbers, hand):
    answer = ''
    left_position = [4, 1]
    right_position = [4, 3]

    def measure(position1, position2):
        distance = abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])
        return distance

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left_position = position_dic[number]
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right_position = position_dic[number]
        else:
            left_right_diff = measure(position_dic[number], left_position) - measure(position_dic[number], right_position)
            if left_right_diff > 0:
                answer += 'R'
                right_position = position_dic[number]
            elif left_right_diff < 0:
                answer += 'L'
                left_position = position_dic[number]
            else:
                if hand == "right":
                    answer += 'R'
                    right_position = position_dic[number]
                else:
                    answer += 'L'
                    left_position = position_dic[number]

    return answer