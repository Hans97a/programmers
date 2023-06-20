def solution(board):
    board_str = "".join(board)
    check = board_str.count("O") - board_str.count("X")
    if check not in [0, 1]:
        return 0

    column = list(zip(*board))
    o_cnt = x_cnt = 0
    for i in range(3):
        if column[i].count("O") == 3 or board[i].count("O") == 3:
            o_cnt += 1
        if column[i].count("X") == 3 or board[i].count("X") == 3:
            x_cnt += 1
    for i in range(0, 3, 2):
        if board[0][i] == board[1][1] == board[2][2 - i] == "O":
            o_cnt += 1
        if board[0][i] == board[1][1] == board[2][2 - i] == "X":
            x_cnt += 1

    if o_cnt and x_cnt:
        return 0
    if o_cnt == 1 and check == 0:
        return 0
    if x_cnt == 1 and check >= 1:
        return 0
    return 1
