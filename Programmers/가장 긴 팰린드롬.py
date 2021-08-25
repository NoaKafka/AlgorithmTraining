def solution(s):
    answer = 1

    for idx in range(len(s)//2, 1, -1):
        arr = s[:idx+1]
        print(arr)
        arr = "".join(reversed(arr))
        
        #포함
        com = s[idx:]
        print(com)
        if len(com) < len(arr):
            arr, com = com, arr
        for i in range(len(arr)):
            if arr[i] != com[i]:
                if answer < 2 * (i + 1) - 1:
                    answer = 2 * (i + 1) - 1
                break
        else:
            print(2 * len(arr))
            if answer < 2 * len(arr) - 1:
                answer = 2 * len(arr) - 1
        #미포함
        arr = s[:idx+1]

        arr = "".join(reversed(arr))
        com = s[idx+1:]
        print(arr)
        print(com)
        if len(com) < len(arr):
            arr, com = com, arr
        for i in range(len(arr)):
            if arr[i] != com[i]:
                print(2 * (i + 1) - 1)
                if answer < 2 * (i + 1) - 1 :
                    answer = 2 * (i + 1) - 1
                break
        else:
            print(2 * len(arr))
            if answer < 2 * len(arr) :
                answer = 2 * len(arr)

    return answer
