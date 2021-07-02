from itertools import combinations

def solution(orders, course):
    
    answer = []
    
    for i in range(len(orders)):
        sorted_characters = sorted(orders[i])
        orders[i] = "".join(sorted_characters)
    
    for idx in course :
        dic = {}
        for order in orders :
            if len(order) >= idx: 
                l = list(map(''.join, combinations(str(order), idx)))            
                for menu in l:
                    if menu in dic :
                        dic[menu] += 1
                    else :
                        dic[menu] = 1
        result = sorted(dic.items(), key = (lambda x : x[1]), reverse = True)
        if len(result) != 0:
            maxi = result[0][1]
            for j in range(len(result)) :
                if result[j][1] == 1:
                    break

                if maxi != result[j][1] :
                    break
                else :
                    answer.append(result[j][0])
            
    return sorted(answer)
