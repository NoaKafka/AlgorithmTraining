visited = []

def solution(n, m, image):
    answer = 0

    global visited
    for _ in range(n):
        visited.append([False] * m)
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                stack = [[i,j]]
                visited[i][j] = True
            else:
                continue
            while len(stack) != 0:
                cur = stack.pop()
                value = image[cur[0]][cur[1]]
                print(cur)
                # 상
                if cur[0] - 1 >= 0 and value == image[cur[0]-1][cur[1]] and not visited[cur[0]-1][cur[1]]:
                    stack.append([cur[0]-1, cur[1]])
                    visited[cur[0]-1][cur[1]] = True
                # 하
                if cur[0] + 1 < n and value == image[cur[0]+1][cur[1]] and not visited[cur[0]+1][cur[1]]:
                    stack.append([cur[0]+1, cur[1]])
                    visited[cur[0]+1][cur[1]] = True
                # 좌
                if cur[1] - 1 >= 0 and value == image[cur[0]][cur[1]-1] and not visited[cur[0]][cur[1]-1]:
                    stack.append([cur[0], cur[1]-1])
                    visited[cur[0]][cur[1]-1] = True
                # 우
                if cur[1] + 1 < m and value == image[cur[0]][cur[1]+1] and not visited[cur[0]][cur[1]+1]:
                    stack.append([cur[0], cur[1]+1])
                    visited[cur[0]][cur[1]+1] = True
            answer += 1
    
    return answer
