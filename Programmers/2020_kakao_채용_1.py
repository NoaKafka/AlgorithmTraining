def solution(s):
    answer = len(s)
    window_size = len(s) // 2
    for win in range(window_size, 0, -1):
        ans = 0
        cnt = 1
        s_copy = s[:]
        target = ""
        while 1:
            if len(s_copy) <= win:
                if(cnt != 1):
                    ans += len(str(cnt))
                ans += len(s_copy)
                break
            
            target = s_copy[0: win]
            s_copy = s_copy[win: len(s_copy)]
            if target == s_copy[0 :win]:
                cnt += 1
            else:
                if cnt != 1:
                    ans += len(str(cnt))
                    ans += len(target)
                    cnt = 1
                else :
                    ans += len(target)
    
        if answer > ans:
            answer = ans
    return answer

s = "aaaaaaaaaabbbbbbbbbb"
print(solution(s))
