healths	       items	                               return
[200,120,150]	[[30,100],[500,30],[100,400]]	        [1,2]
[300,200,500]	[[1000, 600], [400, 500], [300, 100]]	[3]

import heapq

def solution(healths, items):
    answer = []
    for i in range(len(items)):
        items[i].append(i)
    items = sorted(items, key = lambda x : -x[0])
    
    visited = [ False ] * len(healths)
    healths = sorted(healths, reverse = True)
    cnt = 0
    #가능한 healths중 제일 작은걸 뺀다.
    for item in items:
        maxi = -1
        if cnt == len(healths):
            break
        for idx in range(len(healths)):
            if not visited[idx] :
                if healths[idx] - item[1] >= 100:
                    maxi = idx
                else:
                    if maxi >= 0:
                        visited[maxi] = True
                        cnt+=1
                        answer.append(item[2]+1)
                    break
        else:
            if not visited[idx] :
                if healths[idx] - item[1] >= 100:
                    maxi = idx

            if maxi >= 0:
                visited[maxi] = True
                cnt+=1
                answer.append(item[2]+1)



    return sorted(answer)
