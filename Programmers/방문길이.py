from collections import defaultdict
def solution(dirs):
    answer = 0
    x = 5
    y = 5
    dic = {}
    for i in range(11):
        for j in range(11):
            dic[(i,j)] = [0,0,0,0]
    # up, down, left, right
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for d in dirs:
        print(x)
        print(y)
        print('--------')
        if d == "U":
            if y + dy[0] >= 0 :
                if dic[(x,y)][0] == 0 and dic[(x, y + dy[0])][1] == 0:
                    answer += 1
                    dic[(x,y)][0] = 1
                    dic[(x, y + dy[0])][1] = 1
                y += dy[0]
                
        elif d == "D":
            if y + dy[1] < 11 :
                if dic[(x,y)][1] == 0 and dic[(x, y + dy[1])][0] == 0:
                    answer += 1
                    dic[(x,y)][1] = 1
                    dic[(x, y + dy[1])][0] = 1
                y += dy[1]
                
        elif d == "L":
            if x + dx[2] >= 0 :
                if dic[(x,y)][2] == 0 and dic[(x + dx[2], y)][3] == 0:
                    answer += 1
                    dic[(x,y)][2] = 1
                    dic[(x + dx[2], y)][3] = 1
                x += dx[2]
                
        else:
            if x + dx[3] < 11 :
                if dic[(x,y)][3] == 0 and dic[(x + dx[3], y)][2] == 0:
                    answer += 1
                    dic[(x,y)][3] = 1
                    dic[(x + dx[3], y)][2] = 1
                x += dx[3]
                
                
    return answer

    
