
# 금광 문제 
# 1. 너무 i,j 가 헷갈려서 x,y로 바꿔서 진행했다
# 2. 함수형으로 사용하려고 발전했다.

def function (N,M) :
    arr = [[0] * M for i in range(N)]
    dp = [[0] * M for i in range(N)]
    
    temp = list(map(int,input().split()))

    cnt = 0 
    for i in range(N) :
        for j in range(M) :
            arr[i][j] = temp[cnt]
            cnt+=1
    for i in range(N) :
        dp[i][0] = arr[i][0]

    for x in range(1,M) :
        for y in range(N) :
            if (y-1>=0) :
                dp[y][x] = max(dp[y-1][x-1]+ arr[y][x],dp[y][x] )
            dp[y][x] = max(dp[y][x-1]+ arr[y][x],dp[y][x] )
            if (y+1< N) :
                dp[y][x] = max(dp[y+1][x-1]+ arr[y][x],dp[y][x] )                  
    print(dp)
function(4,4)


    
        

    
    
     
        

