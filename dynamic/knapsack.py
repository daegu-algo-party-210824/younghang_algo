n,m =list( map (int,input().split(" ")))

v=[0] * (n+1)
w=[0] * (n+1)
#파이썬 이차월 배열 주의.
dp = [[0]* (m+1) for _ in range(n+1)] 

for i in range(1,n+1) :
    temp = list (input().split(" "))
    w[i] = (int(temp[0]))
    v[i] = (int(temp[1]))

#dp[i,j] = i번째 까지 아이템에서 최대 j까지의 만족도를 구하는 거.
for i in range(1,n+1) :
    for j in range(1,m+1) :
        #남아 있으면 초기화 해준다.
        if (j - w[i] >= 0) :
            dp[i][j] = max(dp[i-1][j], dp[i - 1][j - w[i]] + v[i])        
        #못넣는 경우는 그냥 같은 값을 넣어준다.
        else : 
            dp[i][j] = dp[i-1][j]
            
print(dp[n][m])

