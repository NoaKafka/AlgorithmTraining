
# 0 - 5 / 1 - 4 / 2 - 3

[n, m, x, y, num] = map(int,input().split())
dice = [0,0,0,0,0,0]
floor = 0
# n x m array
board = []
for i in range(n):
    board.append(list(map(int,(input().split()))))
arr = list(map(int,input().split()))

#print(board)
#print(arr)

floor = 1
up = 0
left = 3
answer = []
for idx in arr:
    #이동가능한지
    if idx == 1:
        if y  >= len(board[0]) - 1:
            continue
        else :
            temp_f = floor
            floor = abs(5 - left)
            left =  temp_f
            y += 1
    elif idx == 2:
        if y <= 0:
            continue
        else :
            temp_f = floor
            floor = left
            left = abs(5 - temp_f)
            y -= 1
    elif idx == 3:
        if x <= 0:
             continue
        else :
            temp_f = floor
            floor = up
            up = abs(5 - temp_f)
            x -= 1
    else :
        if x >= len(board)-1:
            continue
        else :
            temp_f = floor
            floor = abs(5 - up)
            up = temp_f
            x += 1

    
    if board[x][y] == 0:
        board[x][y] = dice[floor]
        
    else :
        dice[floor] = board[x][y]
        board[x][y] = 0

   
    print('f: ', floor, ' up : ', up, ' left : ', left)
    
    print(board)
    print('------------------')


    answer.append(dice[abs(5-floor)])
for i in answer:
    print(i)
