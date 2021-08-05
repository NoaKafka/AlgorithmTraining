n = int(input())
upper = []
lower = []

for _ in range(n):
    cnt = int(input())
    
    upper = list(map(int, input().split()))
    lower = list(map(int, input().split()))

    cnt = int(input())
    if cnt > 2 :

        upper[1] += lower[0]
        lower[1] += upper[0]

        for i in range(2, cnt):
            
            #위
            upper[i] += max(lower[i-1], max( upper[i-2], lower[n-2]))
            #아래
            lower[i] = max(upper[i-1], max( upper[i-2], lower[n-2]))
    if cnt == 2:
        upper[1] += lower[0]
        lower[1] += upper[0]

    print(max(upper[-1], lower[-1]))

