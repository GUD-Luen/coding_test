def solution(s):
    word_list = s.split(' ')
    for index, word in enumerate(word_list):
        char_list = []
        for i, char in enumerate(word):
            if i % 2 == 0:
                char_list.append(char.upper())
            else:
                char_list.append(char.lower())
        word_list[index] = ''.join(char_list)

    return ' '.join(word_list)