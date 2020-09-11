import copy
import itertools
def check(n, candi, w, idx):
    # 시계
    weak = copy.deepcopy(w)
    for i in range(len(weak)):
        arr = []
        for j in range(i,len(weak)):
            arr.append(weak[j])
        for j in range(0,i):
            arr.append(n + weak[j])
        #print(arr)
        start_idx = 0
        start = arr[start_idx]
        for c in candi:
            start += c
            #find next start
            #print('c는 : ',c, ' start는 : ',start)
            if start >= arr[-1]:
                return True
            
            while True:
                start_idx += 1
                if arr[start_idx] > start:
                    start = arr[start_idx]
                    break
            
    return False
def solution(n, weak, dist):
    answer = 0
    dist.sort(reverse =True)
    r_weak = copy.deepcopy(weak)
    for i in range(len(r_weak)):
        r_weak[i] = n - r_weak[i]
    r_weak.sort()
    #print(r_weak)
    for i in range(1,len(dist)+1):
        #시작점
        if i == len(weak):
            return i
        #print('forward')
        cans = list(itertools.permutations(dist, i))
        for k in range(len(cans)):
            if check(n, list(cans[k]), weak, i) : return i
            #print('backward')
            if check(n, list(cans[k]), r_weak, i) : return i
        
    
    return -1
