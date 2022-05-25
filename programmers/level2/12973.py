def solution(s):
    if len(s) % 2 == 1:
        return 0
    char_list = list(s)
    no_match_list = []
    char_list_length = len(char_list)
    for i in range(char_list_length):
        if not no_match_list:
            no_match_list.append(char_list.pop())
        else:
            last_no_match_char = no_match_list.pop()
            last_char = char_list.pop()
            if last_char == last_no_match_char:
                pass
            else:
                no_match_list.append(last_no_match_char)
                no_match_list.append(last_char)
    if not no_match_list:
        return 1
    else:
        return 0