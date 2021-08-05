max_weight  specs	                        names	                        return
300	    [["toy","70"], ["snack", "200"]]	["toy", "snack", "snack"]	2
200	    [["toy","70"], ["snack", "200"]]	["toy", "snack", "toy"]	        3


def solution(max_weight, specs, names):
    answer = 0

    dic = dict(specs)
    summ = 0
    
    for i in range(len(names)):
        if summ + int(dic[names[i]]) > max_weight:
            answer += 1
            summ = int(dic[names[i]])
        else:
            summ += int(dic[names[i]])
    if summ != 0:
        answer += 1
    
    return answer
