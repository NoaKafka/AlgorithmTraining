v	                       result
[[1, 4], [3, 4], [3, 10]]	[1, 10]
[[1, 1], [2, 2], [1, 2]]	[2, 1]

def solution(v):
    answer = []

    if v[0][0] == v[1][0]:
        answer.append(v[2][0])
        
    else:
        if v[1][0] == v[2][0]:
            answer.append(v[0][0])
            
        else:
            answer.append(v[1][0])

    if v[0][1] == v[1][1]:
        answer.append(v[2][1])
    else:
        if v[1][1] == v[2][1]:
            answer.append(v[0][1])
        else:
            answer.append(v[1][1])
        
        
    return answer
