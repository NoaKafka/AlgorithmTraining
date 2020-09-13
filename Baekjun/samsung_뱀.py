from collections import deque

N = int(input())
time = 1
n_apple = int(input())
board = [[0 for i in range(N)] for i in range(N)]
for i in range(n_apple):
    [a,b] = map(int,input().split())
    board[a-1][b-1] = 1     # 1 is apple

n_change = int(input())
changes = {}
for i in range(n_change):
    [t, move] = map(str,input().split())
    changes[t] = move

snake = deque()
snake.append([0,0])
snake_dict = {"00":1}
direction = "R"     # 머리가 가리키는 방향
x = 0
y = 0

while True:
    
    
    #print(time)
    
    #print(board)
        #print('타임')


    
    # 벽에 부딛치는 경우
    if direction == "R":
        if y == N-1:
            print(time)
            break
    elif direction == "L":
        if y == 0:
            print(time)
            break
    elif direction == "U":
        if x == 0:
            print(time)
            break
    else:
        if x == N-1:
            print(time)
            break

    # 내 몸에 부딛치는 경우
    
    if direction == "R":
        y += 1
        #print(board[x][y])
        if board[x][y] == 1:
            board[x][y]=0
            
        elif board[x][y] == 0:
            [p,q] = snake.popleft()
            if str(str(x)+str(y)) in snake_dict:
                print(time)
                break
            del snake_dict[str(str(p)+str(q))]
            
        if str(str(x)+str(y)) in snake_dict:
            print(time)
            break
        snake.append([x,y])
        snake_dict[str(x)+str(y)] = 1
            
    elif direction == "L":
        y -= 1
        if board[x][y] == 1:
            board[x][y] = 0
            
        elif board[x][y] == 0:
            [p,q] = snake.popleft()
            if str(str(x)+str(y)) in snake_dict:
                print(time)
                break
            del snake_dict[str(str(p)+str(q))]
            
        if str(str(x)+str(y)) in snake_dict:
            print(time)
            break
        snake.append([x,y])
        snake_dict[str(x)+str(y)] = 1
    elif direction == "U":
        x -= 1
        if board[x][y] == 1:
            board[x][y] = 0
            
        elif board[x][y] == 0:
            [p,q] = snake.popleft()
            if str(str(x)+str(y)) in snake_dict:
                print(time)
                break
            del snake_dict[str(str(p)+str(q))]
            
        if str(str(x)+str(y)) in snake_dict:
            print(time)
            break
        snake.append([x,y])
        snake_dict[str(x)+str(y)] = 1
    else:
        x += 1
        if board[x][y] == 1:
            board[x][y] = 0
            
        elif board[x][y] == 0:
            [p,q] = snake.popleft()
            if str(str(x)+str(y)) in snake_dict:
                print(time)
                break
            del snake_dict[str(str(p)+str(q))]
            
        if str(str(x)+str(y)) in snake_dict:
            print(time)
            break
        snake.append([x,y])
        snake_dict[str(x)+str(y)] = 1


    #print(snake)
    #print(x, ' ', y)


    time += 1
    
    if str(time-1) in changes:
        #print(changes)
        #print('방향전환')
        if changes[str(time-1)] == "D":
            if direction == "R":
                direction = "D"
            elif direction == "L":
                direction = "U"
            elif direction == "U":
                direction = "R"
            else :
                direction = "L"
        else :
            if direction == "R":
                direction = "U"
            elif direction == "L":
                direction = "D"
            elif direction == "U":
                direction = "L"
            else :
                direction = "R"
    
    


