# sort 사용법 : sort(key = lambda x : (x ))

def solution(weights, head2head):
    answer = []
    
    #1. 승률
    win_pro = []
    
    for i in range(len(head2head)):
        n = 0
        cnt = 0
        for j in range(len(head2head[i])):
            if (i!= j and head2head[i][j] == "W"):
                cnt+=1
            if (i!= j and head2head[i][j] != "N"):
                n +=1
        if (n==0):
            win_pro.append(0)
        else :
            win_pro.append(cnt/n)
    
    #2. 몸무게가 높은 이긴횟수
    num_win2 = []
    for i in range(len(head2head)):
        cnt = 0
        for j in range(len(head2head[i])):
            if (i!= j and head2head[i][j] == "W" and weights[i] < weights[j] ):
                cnt+=1
        num_win2.append(cnt)
    
    #3. 몸무게
    
    #4. 번호
    win_pro3 = [i for i in range(1,len(weights)+1)]
    
    #print(arr)
    
    
    arr3 = []
    
    for i in range(len(weights)):
        arr3.append (  (win_pro[i],num_win2[i],weights[i],win_pro3[i]))
    
    print(arr3.sort(key = lambda x:(-x[0],-x[1],-x[2],x[3])))
    print(arr3)
    
    for i in range(len(weights)):
        answer.append(arr3[i][3])
    return answer