s	result
"xyb"	"yb"
"yxyc"	"yyc"

def solution(s):
    answer = ''
    idx = 0
    while idx < len(s):
        s = s[idx:]
        maxi = max(s)
        arr = list(filter(lambda x: s[x] == maxi, range(len(s))))
        answer += maxi * len(arr)        
        idx = arr[-1] + 1
    return answer
