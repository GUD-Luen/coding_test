import re


def solution(new_id):
    old_id = new_id.lower()
    patten = re.compile('[a-z-_.0-9]+')
    answer = ''
    for x in patten.findall(old_id):
        answer += x
    while answer.count('..') > 0:
        answer = answer.replace('..', '.')
    if len(answer) != 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[len(answer)-1] == '.':
        answer = answer[:len(answer)-1]
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[len(answer)-1] == '.':
        answer = answer[:len(answer)-1]
    while len(answer) <= 2:
        answer += answer[len(answer)-1]
    return answer