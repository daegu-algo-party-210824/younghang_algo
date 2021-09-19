#1. 정확한 순위를 알려면 x / 나 / y 
# 각 갯수가 

# 자기가 갈 수 있는 값이랑 
# 자기로 들어오는 값이랑 합이 n-1이 되면 정확한 순위를 알 수 있다.

N,M = map(int,input().split(" "))

arr = [[int(1e9)]*(N+1) for i in range(N+1)]

for i in range(M) :
    a,b = map(int,input().split(" "))
    arr[a][b] = 1
# v플로이드 워셜은 0으로 초기화 해줘야 한다.
for a in range(1,N+1) :
    arr[a][a] = 0 

for k in range(1,N+1):
    for a in range(1,N+1) :
        for b in range(1,N+1) :
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

ret = 0
cnt = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] != int(1e9) :
            cnt +=1
    for j in range(1,N+1):
        if arr[j][i] != int(1e9) :
            cnt +=1
    if cnt == N-1 :
        ret +=1
    cnt = 0
    
    
print(ret)


