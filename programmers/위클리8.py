def solution(sizes):
    answer = 0
    
    a= []

    for i in range(len(sizes)):
        a.append ((sizes[i][0],sizes[i][1]))
    
    b = sorted(a,key = lambda x : -x[0])
    c = sorted (b,key = lambda x : -x[1])

    #b는 왼쪽꺼가 가장 큰 경우
    #c는 오른쪽이 가장 큰 경우.
    
    if (b[0][0] < c[0][1]) :
        # c가 가장 큰 경우
        # b로 처리
        for i in range(len(c)):
            if (c[i][0] < c[i][1]):
                c[i] = (c[i][1],c[i][0])
        
    else :
        # b로 처리
        for i in range(len(b)):
            if (b[i][0] < b[i][1]):
                b[i] = (b[i][1],b[i][0])
    max1 = 0
    max2 = 0
    max3 = 0
    max4 = 0
    
    for i in range(len(b)) :
        max1 = max(max1,b[i][0])
        max2 = max(max2,b[i][1])
    
    for i in range(len(c)) :
        max3 = max(max3,c[i][0])
        max4 = max(max4,c[i][1])
        
    
    
    return min (max1*max2, max3*max4)



# 발전 
# (큰수, 작은수) 형식으로 넣는다. 그리고 max1, max2 곱한것을 구한다.





print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
