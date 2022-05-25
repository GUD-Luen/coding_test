supo1 = [1, 2, 3, 4, 5]
supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    answer = []
    points = [0] * 3
    for i in range(len(answers)):
        if answers[i] == supo1[i % 5]:
            points[0] += 1
        if answers[i] == supo2[i % 8]:
            points[1] += 1
        if answers[i] == supo3[i % 10]:
            points[2] += 1
    for i in range(len(points)):
        if points[i] == max(points):
            answer.append(i + 1)
    return answer