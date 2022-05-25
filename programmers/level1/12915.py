def solution(strings, n):
    char_dic = {}
    for text in strings:
        if text[n] in char_dic:
            tmp = char_dic[text[n]]
            tmp.append(text)
            char_dic[text[n]] = tmp
        else:
            char_dic[text[n]] = [text]

    answer = []
    for char in sorted(list(char_dic.keys())):
        answer += sorted(char_dic[char])
    return answer