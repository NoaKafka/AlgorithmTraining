from itertools import permutations

def solution(expression):
    answer = 0
    giho = []
    n_giho = 0
    arr = []
    temp_s = ""
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '-' or expression[i] == '*' :
            n_giho += 1
            giho.append(expression[i])
            arr.append(temp_s)
            temp_s = ''
        else:
            temp_s += expression[i]
    arr.append(temp_s)
    #6가지 순서 정하기
    num = ['+','-','*']
    #print("기호는 ",giho)
    sunseo = list(map(''.join, permutations(num)))
    for i in range(len(sunseo)):
        #print('순서는', i)
        t_arr = arr[:]
        t_giho = giho[:]
        #print(t_arr)
        for j in range(3):
            #print('기호 ', j, '번')
            t = sunseo[i][j]
            g = len(t_giho)
            #print('g  ', g)
            sik = ''
            for k in range(g):
                #print('k는 ', k, ' 기호 ', t_giho)
                #print(t_arr)
                if t_giho[k] == t:
                    sik = str(t_arr[k]) + str(t_giho[k]) + str(t_arr[k+1])
                    #print('식은 ',sik)
                    w = eval(sik)
                    t_giho[k] = '!'
                    t_arr[k] = w
                    t_arr[k+1] = w
                
            for k in range(len(t_giho)-1, -1 ,-1):
                if t_giho[k] == '!':
                    t_giho.pop(k)
                    t_arr.pop(k)
        #print('답은 ', t_arr[0])            
        if abs(t_arr[0]) > int(answer) :
            answer = abs(int(t_arr[0]))

    return answer
