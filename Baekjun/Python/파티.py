N, M, dest = map(int, input().split())


graph = [[0] * (N+1) for __ in range(N+1)]
visited_f = [0] * (N+1)
visited_b = [0] * (N+1)

for _ in range(M):
    x, y, value = map(int, input().split())
    graph[x][y] = value


