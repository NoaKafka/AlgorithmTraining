import copy
answer = []

def DFS(graph, start_idx, visited):
    global answer
    visited.append(start_idx)
    
    if len(visited) == len(graph):
        answer.append(visited)
    
    for idx in range(0, len(graph)):
        if idx not in visited and graph[start_idx][1] == graph[idx][0]:
            v = copy.deepcopy(visited)     
            DFS(graph, idx, v)
    

def IdxToStr(graph, indexArr):
    ans = [graph[indexArr[0]][0]]
    for i in indexArr:
        ans.append(graph[i][1])
    return ans

def arr_compare(arr1, arr2):
    for i in range(0, len(arr2)):
        if arr1[i] == arr2[i]:
            continue
        elif arr1[i] > arr2[i]:
            return arr2
        else:
            return arr1
    return arr1

def solution(tickets):
    global answer
    
    for idx in range(0, len(tickets)):
        if tickets[idx][0] == "ICN":
            DFS(tickets, idx, [])
    
    new_answer = []
    for i in answer:
        new_answer.append(IdxToStr(tickets, i))
        
    real_answer = new_answer[0]
    
    for a in new_answer:
        real_answer = arr_compare(real_answer, a)
    return real_answer
