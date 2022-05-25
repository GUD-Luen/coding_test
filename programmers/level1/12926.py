def solution(s, n):
    answer = ''
    for c in s:
        o = ord(c)
        if 96 < o < 123:
            answer += chr(((o + n - 97) % 26) + 97)
        elif 64 < o < 91:
            answer += chr(((o + n - 65) % 26) + 65)
        else:
            answer += c
    return answer