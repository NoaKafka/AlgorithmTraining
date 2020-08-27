import copy

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def find_two(n_pad, num):
    cnt = 0
    #print(n_pad)
    for i in range(len(n_pad)):
        for j in range(len(n_pad)):
            if n_pad[i][j] == 1:
                #print('True :')
                cnt += 1
            elif n_pad[i][j] == 3 :
                #print('False :')
                return False
    if cnt == num:
        return True
    return False

def solution(key, lock):
    answer = False
    padding = len(key) - 1
    num = 0
    keys = 0
    pad  = [[-2 for i in range(len(lock)+ (2*len(key)) - 1)] for j in range(len(lock)+ (2*len(key)) - 1)]
    
    

    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 1:  
                pad[i + padding][j + padding]  = lock[i][j] + 1
            else :
                pad[i + padding][j + padding]  = lock[i][j]
                num += 1
    
    if num == 0 :
        return True
    
    
    for i in range(len(key)) :
        for j in range(len(key)) :
            if key[i][j] == 0:
                key[i][j] = 2
            else :
                keys += 1
    #print(keys,' ', num)
    if keys < num:
        return False
    
    for i in range(len(pad) - len(key)) :
        for j in range(len(pad) - len(key)) :
            #시작점 temp_pad[i][j]
            temp_pad = copy.deepcopy(pad)
                # temp_pad + key
            for a  in range(len(key)):
                for b  in range(len(key)):
                    temp_pad[a+i][b+j] += key[a][b]
            ans = find_two(temp_pad, num)
            if ans == True:
                answer = True
                return True
    if answer != True:
        key = rotate_90(key)
        for i in range(len(pad) - len(key)) :
            for j in range(len(pad) - len(key)) :
                #시작점 temp_pad[i][j]
                temp_pad = copy.deepcopy(pad)
                    # temp_pad + key
                for a  in range(len(key)):
                    for b  in range(len(key)):
                        temp_pad[a+i][b+j] += key[a][b]
                ans = find_two(temp_pad, num)
                if ans == True:
                    answer = True
                    return True
    if answer != True:
        key = rotate_90(key)
        for i in range(len(pad) - len(key)) :
            for j in range(len(pad) - len(key)) :
                #시작점 temp_pad[i][j]
                temp_pad = copy.deepcopy(pad)
                    # temp_pad + key
                for a  in range(len(key)):
                    for b  in range(len(key)):
                        temp_pad[a+i][b+j] += key[a][b]
                ans = find_two(temp_pad, num)
                if ans == True:
                    answer = True
                    return True
    if answer != True:
        key = rotate_90(key)
        for i in range(len(pad) - len(key)) :
            for j in range(len(pad) - len(key)) :
                #시작점 temp_pad[i][j]
                temp_pad = copy.deepcopy(pad)
                    # temp_pad + key
                for a  in range(len(key)):
                    for b  in range(len(key)):
                        temp_pad[a+i][b+j] += key[a][b]
                ans = find_two(temp_pad, num)
                if ans == True:
                    answer = True
                    return True
    return answer
