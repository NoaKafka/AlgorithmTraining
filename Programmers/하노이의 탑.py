def solution(n):
    answer = []
    def hanoi(num, f, t, middle):
        if num== 1:
            answer.append([f,t])
            return

        hanoi(num-1, f, middle, t)
        answer.append([f,t])
        hanoi(num-1, middle, t, f)

    
    hanoi(n,1,3,2)
    
    return answer
