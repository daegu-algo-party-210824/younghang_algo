n,m = map(int,input().split())

arr = [[(1e9) for i in range(n+1) ] for i in range(n+1)]

for i in range(n+1) :
    arr[i][i] = 0

for i in range(m) :
    a,b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for k in range(n+1):
    for a in range(n+1) :
        for b in range(n+1) :
            arr[a][b] = min (arr[a][b], arr[a][k] + arr[k][b])

min1 = 987654321
index1 = -1

for i in range(1,n+1) :
    sum1 = 0
    for j in range(1,n+1) :
        sum1 += arr[i][j]
    if (min1 > sum1) :
        min1 = sum1
        index1 = i

print(index1)



    