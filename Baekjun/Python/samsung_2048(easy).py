import copy

def left(q):
    graph = copy.deepcopy(q)
    for i in range(n):
        # 좌로 밀착
        arr = []
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                arr.append(graph[i][j])
        new_arr = []
        # 합치기
        for j in range(1,len(arr)):
            if arr[j] == arr[j-1]:
                new_arr.append(arr[j-1] * 2)
                arr[j] = 0
            else :
                if arr[j-1] != 0:
                    new_arr.append(arr[j-1])
        if len(arr) != 0 :
            if arr[len(arr)-1] != 0:
                new_arr.append(arr[len(arr)-1])
        # 0 채우기
        for j in range(len(graph[i]) - len(new_arr)):
            new_arr.append(0)

        graph[i] = new_arr
    return graph             


def right(q):
    graph = q = copy.deepcopy(q)
    for i in range(n):
        graph[i].reverse() 
    graph = left(graph)
    for i in range(n):
        graph[i].reverse()        
    return graph  

def up(q):
    graph = copy.deepcopy(q)
    #위로 밀착
    for i in range(n):
        t = []
        for j in range(n):
            t.append(graph[j][i])
        #print(t)
        arr = []
        for it in t:
            if it != 0:
                arr.append(it)
        new_arr = []
        # 합치기
        #print(len(arr))
        for j in range(1,len(arr)):
            if arr[j] == arr[j-1] and arr[j] != 0:
                new_arr.append(arr[j-1] * 2)
                arr[j] = 0
            else :
                if arr[j-1] != 0:
                    new_arr.append(arr[j-1])
        if len(arr) != 0 :
            if arr[len(arr)-1] != 0:
                new_arr.append(arr[len(arr)-1])
        
        #print(new_arr)
        for j in range(n - len(new_arr)):
            new_arr.append(0)
        
        for j in range(n):
            graph[j][i] = new_arr[j]
    return graph

def down(q):
    graph = copy.deepcopy(q)
    for i in range(n):
        for j in range(n//2):
            temp = graph[j][i]
            graph[j][i] = graph[n-j-1][i]
            graph[n-j-1][i] = temp
    graph = up(graph)
    for i in range(n):
        for j in range(n//2):
            temp = graph[j][i]
            graph[j][i] = graph[n-j-1][i]
            graph[n-j-1][i] = temp
    
    return graph


def dfs(graph, cnt):
    
    if cnt > 5:
        #return max value of graph
        return max(map(max, graph))
    q = copy.deepcopy(graph)
    t = copy.deepcopy(q)
    u = up(t)
    t = copy.deepcopy(q)
    
    d = down(t)
    t = copy.deepcopy(q)
    
    l = left(t)
    t = copy.deepcopy(q)
    
    r = right(t)
    t = copy.deepcopy(q)
    
    a = dfs(u, cnt+1)
    b = dfs(d, cnt+1)
    c = dfs(l, cnt+1)
    d = dfs(r, cnt+1)

    noa = [a,b,c,d]
    return max(noa)


n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

answer = dfs(graph, 1)
print(answer)
