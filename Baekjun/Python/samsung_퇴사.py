N = int(input())
answer = 0
time= []
payment = []

for i in range(N):
    a, b = map(int, input().split())
    time.append(a)
    payment.append(b)

def solution(idx, pay):
    global answer
    global N
    global time
    global payment

    if idx >= N:
        if pay > answer :
            answer = pay
        return 0
    
    # advice == True
    if idx + time[idx] <= N:
        solution(idx + time[idx], pay + payment[idx])
    
    # advice == False
    if idx + 1 <= N: 
        solution(idx + 1, pay)
    return 0

solution(0, 0)
print(answer)
