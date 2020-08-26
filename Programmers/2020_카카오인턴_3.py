def solution(gems):
    
    start = 0
    end = 0
    gem_set = set(gems)
    lis = list(gem_set)
    num = len(gem_set)
    summ = len(gems) + 1
    
    real_start = 0
    real_end = 0

    dic = {}
    while 1:
        #print(dic)
        if len(dic) == num :
            #구간 줄여보기
            #arr.pop(0)
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1
            
        elif end == len(gems):
            break
        else :
            #arr.append(gems[end])
            if gems[end] in dic:
                dic[gems[end]] += 1
            else :
                dic[gems[end]] = 1
            end += 1
        
        #arr_set = set(arr)

        
        if summ > end - start:
            if len(dic) == num:
                summ = end - start
                real_start = start
                real_end = end
                
    
    return [real_start+1, real_end]
