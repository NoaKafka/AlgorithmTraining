def recurse(s):
    ans = ""
    left = 0
    right = 0
    idx = 0
    check = 0
    while 1:
        if idx == len(s):
            break
        
        if s[idx] == '(':
            left += 1
        else :
            right += 1
        
        if left < right :
            check = 1

        print('L ', left, ' R ', right, ' index ', idx)
        if left == right:
            if check == 0:
                #올바른 답
                ans += s[0:idx+1]
                print('right ', ans)
                if idx  != len(s) :
                    ans += recurse(s[idx+1 : len(s)])
                break
            else :
                #틀린 답
                ans += '('
                ans += recurse(s[idx +1 : len(s)])
                ans += ')'
                temp_str = ""
                for i in range(1, idx):
                    if s[i] == '(':
                        temp_str += ')'
                    else :
                        temp_str += '('
                ans += temp_str
                print('wrong1 ', ans)
                print(len(s))
                print(s[idx + 1 : len(s) - 1])
                
                print('wrong2 ', ans)
                break
                
        else:
            idx += 1
            
    return ans        
            
def solution(p):
    answer = ''
    
    answer = recurse(p)
                
    return answer
