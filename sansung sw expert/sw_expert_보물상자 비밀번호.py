import math

T = int(input())

for i in range(T):
    [N, K] = map(int,input().split())
    data = input()
    s = set()
    n = N//4    #한 변에 들어갈 데이터 갯수
    # 4 개의 string을 만들어서 4등분함 ->set에 넣음
    #print(n)
    for j in range(n):
        s.add(int(data[0:n],16))
        s.add(int(data[n:2*n],16))
        s.add(int(data[2*n:3*n],16))
        s.add(int(data[3*n:4*n],16))
        
        data = data[1:]+data[0]
        data =''
        
        
        #print(data)
    arr = list(s)
    arr.sort(reverse =True)
    #print(arr)
    #print(K)
    
    

    print(int(arr[K-1])
