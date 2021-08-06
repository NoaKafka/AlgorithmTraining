def solution(key, lock):


    for _ in range(4):
        ret = [[0] * len(key) for __ in range(len(key))]
        for i in range(len(key)):
            for j in range(len(key)):
                ret[j][len(key) -1 -i] = key[i][j]
        key = ret
        
        # key를 lock에 꽂아보기
        # Set Padding 2 * (len(key) - 1)
        new_lock = [[-2] * (2 * (len(key) - 1) + len(lock)) for __ in range(2 * (len(key) -1)+ len(lock))]
        target = 0
        
        for i in range(len(lock)):
            for j in range(len(lock)):
                if lock[i][j] == 0:
                    target += 1
                    new_lock[i+len(key)-1][j+len(key)-1] = 0
                if lock[i][j] == 1:
                    new_lock[i+len(key)-1][j+len(key)-1] = 1
        for i in range(len(new_lock) - len(key)+1):
            for j in range(len(new_lock) - len(key)+1):
                cnt = 0
                bp = True
                for k in range(len(key)):
                    for p in range(len(key)):
                        if key[k][p] == 1 and new_lock[i+k][j+p] == 1:
                            bp = False
                            break
                        if key[k][p] == 1 and new_lock[i+k][j+p] == 0:
                            cnt += 1
                if cnt == target and bp:
                    return True
                
            
    return False
