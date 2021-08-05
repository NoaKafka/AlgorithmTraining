from collections import defaultdict
def solution(board, nums):
    answer = 0

    dic = defaultdict(int)
    for num in nums:
        dic[num] += 1

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dic[board[i][j]] == 1:
                board[i][j] = 0

    #Bingo Check
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0 :
                break
        else:
            answer += 1

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[j][i] != 0 :
                break
        else:
            answer += 1

    for i in range(len(board)):
        if board[i][i] != 0 :
            break
    else:
        answer += 1

    for i in range(len(board)):
        if board[len(board) - 1 - i][i] != 0 :
            break
    else:
        answer += 1
    

    return answer
