def solution(N, number):
    answer = 1
    num_len = len(str(number))
    N = int(N)

    DP = []
    DP.append([0])
    #set을 만들기
    for i in range(1,9):
        s = set()
        idx = i // 2
        for j in range(1,idx+1):
            a = DP[j]
            b = DP[i-j]
            for a_i in range(len(a)):
                for b_i in range(len(b)):
                    if a[a_i] + b[b_i] > 0:
                        s.add(a[a_i] + b[b_i])
                    if a[a_i] - b[b_i] > 0:
                        s.add(a[a_i] - b[b_i])
                    if a[a_i] * b[b_i] > 0:
                        s.add(a[a_i] * b[b_i])
                    if a[a_i] // b[b_i] > 0:
                        s.add(a[a_i] // b[b_i])
                    if b[b_i] // a[a_i] > 0:
                        s.add(b[b_i] // a[a_i])
        temp = str(N)
        for h in range(i-1):
            temp += str(N)
        s.add(int(temp))
        ans_list = list(s)
        if int(number) in ans_list:
            #DP.append(ans_list)
            #print(DP)
            return i
        else :
            DP.append(ans_list)
            #print(DP)
    return -1


N = 2
number = 8
print(solution(N,number))
