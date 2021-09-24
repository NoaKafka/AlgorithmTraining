def search(graph):
    figures = []
    result = []
    stack = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1:
                x_max = i
                x_min = i
                y_max = j
                y_min = j
                stack.append([i,j])
                history = []
                history.append([i,j])
                # make figure
                # By DFS
                while len(stack) != 0:
                    cur = stack.pop()
                    x,y = cur[0], cur[1]
                    graph[x][y] = 1
                    for k in range(4):
                        if x + dx[k] >= 0 and x + dx[k] < len(graph) and  y+dy[k] >= 0 and y+dy[k] < len(graph):
                            if graph[x+dx[k]][y+dy[k]] == 0:
                                stack.append([x+dx[k],y+dy[k]])
                                history.append([x+dx[k],y+dy[k]])
                                # max,min x value
                                if x + dx[k] < x_min:
                                    x_min = x + dx[k]
                                if x + dx[k] > x_max:
                                    x_max = x + dx[k]
                                # max,min y value
                                if y + dy[k] < y_min:
                                    y_min = y + dy[k]
                                if y + dy[k] > y_max:
                                    y_max = y + dy[k]
                arr = [[0] * (y_max - y_min + 1) for _ in range(x_max - x_min + 1)]
                print(x_max-x_min+1)
                print(x_max-y_min+1)
                for k in range(len(history)):
                    x,y = history[k][0], history[k][1]
                    arr[x-x_min-1][y-y_min-1] = 1
                print(arr)
                print('-------')

                
def solution(game_board, table):
    answer = -1

    arr1 = search(game_board)
    #arr2 = search(table)
    return answer
