# 경쟁적 전염 문제 
# 1. 탈출조건.
# 2. 큐에 넣는거 주의 (arr, y, x, cnt) 
# 3. 큐에 넣는거는 arr는 뺄 수 있다.

from collections import deque
n,k = map(int,input().split())
dir = [[-1,0],[1,0],[0,1],[0,-1]]
arr = []
for i in range(n) :
    arr.append(list(map(int,input().split())))
S,X,Y = list(map(int,input().split()))

q = []
for i in range(n) :
    for j in range(n):
        if (arr[i][j] != 0 ):   
            q.append((arr[i][j],i,j,0))

q.sort()
q = deque(q)
while q:
    value , y, x , cnt = q.popleft()
    
    if cnt >= S :
        break
    for i in range(4):
        ny = y + dir[i][0]
        nx = x + dir[i][1]
        if (ny< n and ny >= 0 and nx < n and nx >=0 and arr[ny][nx] == 0) :
            arr[ny][nx] = value
            q.append((value,ny,nx,cnt+1))
#print(arr)
print(arr[X-1][Y-1])



