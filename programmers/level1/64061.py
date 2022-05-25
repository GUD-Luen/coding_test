def solution(board, moves):
    answer = 0
    baguni = []

    for position in moves:
        position -= 1
        for i in range(len(board)):
            if board[i][position] != 0:
                if len(baguni) == 0 or baguni[len(baguni)-1] != board[i][position]:
                    baguni.append(board[i][position])
                elif baguni[len(baguni)-1] == board[i][position]:
                    del baguni[len(baguni)-1]
                    answer += 2
                board[i][position] = 0
                break

    return answer