from operator import itemgetter

def solution(n, build_frame):
    answer = []
    
    for i in range(len(build_frame)):
        x = build_frame[i][0]
        y = build_frame[i][1]
        a = build_frame[i][2]
        b = build_frame[i][3]
        
        # 설치
        if b == 1:
            #기둥
            if a == 0 :
                # 기둥 위
                if y == 0:
                    answer.append([x,y,0])
                else: 
                    if [x,y-1,0] in answer :
                        answer.append([x,y,0])
                    #보 한쪽 끝
                    else :
                        if [x-1,y,1] in answer or [x,y,1] in answer:
                            #or
                            #if [x,y,1] in answer and not [x,y,1] in answer:
                            answer.append([x,y,0])
                            #if not [x,y,1] in answer and [x,y,1] in answer:
                                #answer.append([x,y,0])   
            #보
            else: 
                # 양 끝이 다른 보와
                if [x-1,y,1] in answer and [x+1,y,1] in answer:
                    answer.append([x,y,1])
                else:
                    if [x,y-1,0] in answer or [x+1,y-1,0] in answer:
                        #양쪽은 x
                        #if [x,y-1,0] in answer and not [x+1,y-1,0] in answer:
                        answer.append([x,y,1])
                        #if not [x,y-1,0] in answer and [x+1,y-1,0] in answer:
                            #answer.append([x,y,1])
        # 제거
        else :
            #기둥
            if a == 0:
                if [x,y,0] in answer:
                    check_a = False
                    check_b = False
                    check_c = False
                    # 윗 기둥 버틸 수 있나
                    if [x,y+1,0] in answer:
                        if [x, y+1, 1] in answer or [x-1, y+1, 1] in answer:
                            check_a = True
                    else:
                        check_a = True
                    # 좌 보가 버틸 수 있나
                    if [x-1,y+1,1] in answer:
                        if [x-1,y,0] in answer:
                                check_b = True
                        else:
                            if [x-2,y+1,1] in answer and [x,y+1,1] in answer:
                                check_b = True
                    else:
                        check_b = True
                    # 우 보가 버틸 수 있나
                    if [x,y+1,1] in answer:
                        if [x+1,y,0] in answer:
                            check_c = True
                        else:
                            if [x-1,y+1,1] in answer and [x+1,y+1,1] in answer:
                                check_c = True  
                    else:
                        check_c = True
                    # 셋 다 버틸 수 있으면
                    if check_a and check_b and check_c:
                        answer.remove([x,y,0])
            #보
            else:
                if [x,y,1] in answer:
                    check_1 = False
                    check_2 = False
                    check_3 = False
                    check_4 = False
                    # 좌 기둥 버틸 수 있나
                    if [x,y,0] in answer :
                        if [x, y-1,0] in answer:
                            check_1 = True
                        else :
                            if [x-1,y,1] in answer:
                                check_1 =True

                    else :
                        check_1 = True
                    # 우 기둥 버틸 수 있나
                    if [x+1,y,0] in answer :
                        if [x+1, y-1,0] in answer:
                            check_2 = True
                        else :
                            if [x+1,y,1] in answer :
                                check_2 =True
                    else :
                        check_2= True
                    # 좌 보가 버틸 수 있나
                    if [x-1,y,1] in answer :
                        # 옆에 기둥이 있거나
                        if [x-1,y-1,0] in answer or [x,y-1,0] in answer:
                            check_3 = True
                        # 양 옆에 보가 있거나
                        #else:
                            #if [x-1,y,1] in answer and [x+1, y, 1] in answer:
                                #check_3 = True
                    else:
                        check_3 = True
                    # 우 보가 버틸 수 있나
                    if [x+1,y,1] in answer :
                        # 옆에 기둥이 있거나
                        if [x+1,y-1,0] in answer or [x+2,y-1,0] in answer:
                            check_4 = True
                        # 양 옆에 보가 있거나
                        #else:
                            #if [x,y,1] in answer and [x+2, y, 1] in answer:
                                #check_4 = True
                    else :
                        check_4 = True

                    if check_1 and check_2 and check_3 and check_4:
                        answer.remove([x,y,1])
    
    answer.sort(key=itemgetter(0,1,2))
    return answer
