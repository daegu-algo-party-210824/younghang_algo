import sys
input = sys.stdin.readline


n = int(input().rstrip())
m = int(input().rstrip())
arr = [[int(1e9)]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            arr[i][j] = 0
    #print(arr)
for i in range(m) :
    temp = list(map(int,input().rstrip().split(" ")))
    # min을 이용할수 있다.
    if (arr[temp[0]][temp[1]] > temp[2] ):
        arr[temp[0]][temp[1]] = temp[2]

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            # 시작점 초기화 해주는건 중요하다.
                #min으로 대체할 수 있다.
            if arr[i][j] > arr[i][k] + arr[k][j] :
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if (arr[i][j] == int(1e9)):
            print("0",end=' ')
        else :
            print(arr[i][j], end = ' ')
    print()


"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""                
