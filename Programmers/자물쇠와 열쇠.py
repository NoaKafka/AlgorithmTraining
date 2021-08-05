def solution(key, lock):
    answer = True

    for _ in range(4):
        ret = [[0] * len(key) for __ in range(len(key))]
        for i in range(len(key)):
            for j in range(len(key)):
                ret[j][len(key) -1 -i] = key[i][j]

        
    
    return answer
