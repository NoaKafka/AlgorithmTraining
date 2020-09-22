N = int(input())
room = []
answer = N

room = list(input().split())
for i in range(len(room)):
    room[i] = int(room[i])
[j,b] = map(int,input().split())

for i in range(len(room)):
    room[i] -= j

for i in range(len(room)):
    if room[i] > 0:
        
        if room[i] % b == 0:
            answer += room[i] // b
        else :
            answer += (room[i] // b)+1
print(answer)
