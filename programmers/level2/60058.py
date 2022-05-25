def solution(p):
    if p == '':
        return p
    answer = ''
    u = ''
    v = ''
    is_wrong = False
    factor = 0
    for i in range(len(p)):
        if p[i] == '(':
            factor += 1
        else:
            factor -= 1
        if factor < 0:
            is_wrong = True
        elif factor == 0:
            u = p[:i+1]
            v = p[i+1:]
            break

    if is_wrong:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in range(len(u)):
            if i == 0 or i == len(u) - 1:
                pass
            else:
                if u[i] == '(':
                    answer += ')'
                else:
                    answer += '('
    else:
        answer = u + solution(v)

    return answer