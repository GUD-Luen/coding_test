def solution(expression):
    expression_list = []
    s_index = 0
    for i in range(len(expression)):
        if expression[i].isnumeric():
            pass
        else:
            expression_list.append(expression[s_index:i])
            expression_list.append(expression[i])
            s_index = i + 1
        if i == len(expression) - 1:
            expression_list.append(expression[s_index:])
    print(expression_list)
    operator_priority_list = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '+', '-'], ['*', '-', '+']]
    answer = []
    for operator_priority in operator_priority_list:
        tmp_expression_list = list(expression_list)
        for operator in operator_priority:
            if operator == '+':
                do_next = True
                while do_next:
                    if '+' in tmp_expression_list:
                        index = tmp_expression_list.index('+')
                        tmp = tmp_expression_list[:index - 1] + [int(tmp_expression_list[index - 1]) + int(tmp_expression_list[index + 1])] + tmp_expression_list[index + 2:]
                        tmp_expression_list = list(tmp)
                    else:
                        do_next = False
            if operator == '-':
                do_next = True
                while do_next:
                    if '-' in tmp_expression_list:
                        index = tmp_expression_list.index('-')
                        tmp = tmp_expression_list[:index - 1] + [int(tmp_expression_list[index - 1]) - int(tmp_expression_list[index + 1])] + tmp_expression_list[index + 2:]
                        tmp_expression_list = list(tmp)
                    else:
                        do_next = False
            if operator == '*':
                do_next = True
                while do_next:
                    if '*' in tmp_expression_list:
                        index = tmp_expression_list.index('*')
                        tmp = tmp_expression_list[:index - 1] + [int(tmp_expression_list[index - 1]) * int(tmp_expression_list[index + 1])] + tmp_expression_list[index + 2:]
                        tmp_expression_list = list(tmp)
                    else:
                        do_next = False
        answer.append(abs(int(tmp_expression_list[0])))
    return max(answer)