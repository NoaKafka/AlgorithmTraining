import copy

def dfs(user_list, ban_list, ban_idx):
    arr = []
    
    if ban_idx == len(ban_list):
        #print('leaf ', user_list)
        user_list.sort()
        return [user_list]
        
    for user in user_list:
        if len(user) != len(ban_list[ban_idx]):
            #print('con')
            continue
        for idx in range(len(user)):
            if user[idx] != ban_list[ban_idx][idx] and ban_list[ban_idx][idx] != '*':
                break
            if idx == len(user)-1:
                #print('bfs!')
                t_ul = copy.deepcopy(user_list)
                t_ul.remove(user)
                #print(t_ul)
                
                leaf = dfs(t_ul, ban_list, ban_idx+1)
                #print(leaf)
                for l in leaf:
                    arr.append(l)
                #print(arr)
    return arr

def solution(user_id, banned_id):
    
    arr = dfs(user_id, banned_id, 0)

    answer = []
    for a in arr:
        if not a in answer:
            answer.append(a)
    
    
    return len(answer)

u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["fr*d*", "abc1**"]
print(solution(u,b))
