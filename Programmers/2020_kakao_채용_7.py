import copy
from collections import deque

def bfs(ab, board):
    cnt = 1
    queue = deque()
    
    visit = {str(ab):0}
    queue.append(ab)
    while True :
        out= deque()
        while len(queue) != 0:
            a = queue.popleft()
            
            if str([len(board)-2,len(board)-1, 2 ]) in visit:
                #print(visit)
                return visit[str([len(board)-2,len(board)-1, 2 ])]
            if str([len(board)-1,len(board)-2, 1 ]) in visit:
                #print(visit)
                return visit[str([len(board)-1,len(board)-2, 1 ])]
            #무조건 더 작은게 a[0], a[1]
            #좌   우   상   하   이동
            #가로
            if a[2] == 1:
                # 좌
                if a[1] != 0:
                    if board[a[0]][a[1]-1] != 1:
                        if not str([a[0], a[1]-1, a[2]]) in visit:
                            visit[str([a[0], a[1]-1, a[2]])] = cnt
                            out.append([a[0], a[1]-1, a[2]])
                        else :
                            if visit[str([a[0], a[1]-1, a[2]])] > cnt:
                                visit[str([a[0], a[1]-1, a[2]])] = cnt
                                out.append([a[0], a[1]-1, a[2]])
                            
                # 우
                if a[1]+1 != len(board)-1:
                    if board[a[0]][a[1]+2] != 1:
                        if not str([a[0], a[1]+1, a[2]]) in visit:
                            visit[str([a[0], a[1]+1, a[2]])] = cnt
                            out.append([a[0], a[1]+1, a[2]])
                        else :
                            if visit[str([a[0], a[1]+1, a[2]])] > cnt:
                                visit[str([a[0], a[1]+1, a[2]])] = cnt
                                out.append([a[0], a[1]+1, a[2]])
                # 상
                if a[0] != 0:
                    if board[a[0]-1][a[1]] != 1 and board[a[0]-1][a[1]+1] != 1:
                        if not str([a[0]-1, a[1], a[2]]) in visit:
                            visit[str([a[0]-1, a[1], a[2]])] = cnt
                            out.append([a[0]-1, a[1], a[2]])
                        else :
                            if visit[str([a[0]-1, a[1], a[2]])] > cnt:
                                visit[str([a[0]-1, a[1], a[2]])] = cnt
                                out.append([a[0]-1, a[1], a[2]])
                        
                        if not str([a[0]-1, a[1], 2]) in visit:
                            visit[str([a[0]-1, a[1], 2])] = cnt
                            out.append([a[0]-1, a[1], 2])
                        else :
                            if visit[str([a[0]-1, a[1], 2])] > cnt:
                                visit[str([a[0]-1, a[1], 2])] = cnt
                                out.append([a[0]-1, a[1], 2])
                        
                        
                        if not str([a[0]-1, a[1]+1, 2]) in visit:
                            visit[str([a[0]-1, a[1]+1, 2])] = cnt
                            out.append([a[0]-1, a[1]+1, 2])
                        else :
                            if visit[str([a[0]-1, a[1]+1, 2])] > cnt:
                                visit[str([a[0]-1, a[1]+1, 2])] = cnt
                                out.append([a[0]-1, a[1]+1, 2])

                        
                # 하
                if a[0] != len(board)-1:
                    if board[a[0]+1][a[1]] != 1 and board[a[0]+1][a[1]+1] != 1:
                        
                        if not str([a[0]+1, a[1], a[2]]) in visit:
                            visit[str([a[0]+1, a[1], a[2]])] = cnt
                            out.append([a[0]+1, a[1], a[2]])
                        else :
                            if visit[str([a[0]+1, a[1], a[2]])] > cnt:
                                visit[str([a[0]+1, a[1], a[2]])] = cnt
                                out.append([a[0]+1, a[1], a[2]])
                        
                        if not str([a[0], a[1], 2]) in visit:
                            visit[str([a[0], a[1], 2])] = cnt
                            out.append([a[0], a[1], 2])
                        else :
                            if visit[str([a[0], a[1], 2])] > cnt:
                                visit[str([a[0], a[1], 2])] = cnt
                                out.append([a[0], a[1], 2])
                        
                        if not str([a[0], a[1]+1, 2]) in visit:
                            visit[str([a[0], a[1]+1, 2])] = cnt
                            out.append([a[0], a[1]+1, 2])
                        else :
                            if visit[str([a[0], a[1]+1, 2])] > cnt:
                                visit[str([a[0], a[1]+1, 2])] = cnt
                                out.append([a[0], a[1]+1, 2])
                        
            #세로
            else :
                # 좌
                if a[1] != 0 :
                    if board[a[0]][a[1]-1] != 1 and board[a[0]+1][a[1]-1] != 1:
                        
                        if not str([a[0], a[1]-1, a[2]]) in visit:
                            visit[str([a[0], a[1]-1, a[2]])] = cnt
                            out.append([a[0], a[1]-1, a[2]])
                        else :
                            if visit[str([a[0], a[1]-1, a[2]])] > cnt:
                                visit[str([a[0], a[1]-1, a[2]])] = cnt
                                out.append([a[0], a[1]-1, a[2]])
                        
                        
                        if not str([a[0],a[1]-1, 1]) in visit:
                            visit[str([a[0],a[1]-1, 1])] = cnt
                            out.append([a[0],a[1]-1, 1])
                        else :
                            if visit[str([a[0],a[1]-1, 1])] > cnt:
                                visit[str([a[0],a[1]-1, 1])] = cnt
                                out.append([a[0],a[1]-1, 1])
                        
                        
                        if not str([a[0]+1,a[1]-1, 1]) in visit:
                            visit[str([a[0]+1,a[1]-1, 1])] = cnt
                            out.append([a[0]+1,a[1]-1, 1])
                        else :
                            if visit[str([a[0]+1,a[1]-1, 1])] > cnt:
                                visit[str([a[0]+1,a[1]-1, 1])] = cnt
                                out.append([a[0]+1,a[1]-1, 1])

                        
                # 우
                if a[1] != len(board)-1 :
                    if board[a[0]][a[1]+1] != 1 and board[a[0]+1][a[1]+1] != 1:
                        
                        if not str([a[0], a[1]+1, a[2]]) in visit:
                            visit[str([a[0], a[1]+1, a[2]])] = cnt
                            out.append([a[0], a[1]+1, a[2]])
                        else :
                            if visit[str([a[0], a[1]+1, a[2]])] > cnt:
                                visit[str([a[0], a[1]+1, a[2]])] = cnt
                                out.append([a[0], a[1]+1, a[2]])
                        
                        if not str([a[0],a[1], 1]) in visit:
                            visit[str([a[0],a[1], 1])] = cnt
                            out.append([a[0],a[1], 1])
                        else :
                            if visit[str([a[0],a[1], 1])] > cnt:
                                visit[str([a[0],a[1], 1])] = cnt
                                out.append([a[0],a[1], 1])
                        
                        if not str([a[0]+1,a[1], 1]) in visit:
                            visit[str([a[0]+1,a[1], 1])] = cnt
                            out.append([a[0]+1,a[1], 1])
                        else :
                            if visit[str([a[0]+1,a[1], 1])] > cnt:
                                visit[str([a[0]+1,a[1], 1])] = cnt
                                out.append([a[0]+1,a[1], 1])
                        
                                
                # 상
                if a[0] != 0:
                    if board[a[0]-1][a[1]] != 1 :
                        if not str([a[0]-1, a[1], a[2]]) in visit:
                            visit[str([a[0]-1, a[1], a[2]])] = cnt
                            out.append([a[0]-1, a[1], a[2]])
                        else :
                            if visit[str([a[0]-1, a[1], a[2]])] > cnt:
                                visit[str([a[0]-1, a[1], a[2]])] = cnt
                                out.append([a[0]-1, a[1], a[2]])
                            
                # 하
                if a[0]+1 != len(board)-1:
                    if board[a[0]+2][a[1]] != 1 :      
                        
                        if not str([a[0]+1, a[1], a[2]]) in visit:
                            visit[str([a[0]+1, a[1], a[2]])] = cnt
                            out.append([a[0]+1, a[1], a[2]])
                        else :
                            if visit[str([a[0]+1, a[1], a[2]])] > cnt:
                                visit[str([a[0]+1, a[1], a[2]])] = cnt
                                out.append([a[0]+1, a[1], a[2]])

        cnt+=1
        queue = deque()
        queue = out
        
        
    return cnt

def solution(board):
    answer = 0
    a = [0,0,1]
    answer = bfs(a, board)
    return answer
