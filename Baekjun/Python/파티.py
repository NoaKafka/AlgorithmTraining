import heapq
from collections import defaultdict

INF = int(1e9)

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    q = []
    heapq.heappush(q, [distance[start], start])

    while q:
        cur_dist, cur_node = heapq.heappop(q)
        if cur_dist > distance[cur_node]:
            continue

        for new_node, new_dist in graph[cur_node].items():
            dist = cur_dist + new_dist
            if dist < distance[new_node]:
                distance[new_node] = dist
                heapq.heappush(q, [dist, new_node])
    return distance
    

N, M, dest = map(int, input().split())

graph = defaultdict(dict)
arr = []
for _ in range(M):
    x, y, value = map(int, input().split())
    graph[x][y] = value


for i in range(1,N+1):
    # 출발점 지정
    arr.append(dijkstra(graph, i))

t = arr[dest-1].items()
answer = [0] * (N + 1)
for tt in t:
    answer[tt[0]] = tt[1]

for i in range(len(arr)):
    answer[i+1] += arr[i][dest]
    

print(max(answer))

'''
answer == sum(arr[2])
for i in range(len(arr)):
    answer += arr[i][2]
'''

        
            

