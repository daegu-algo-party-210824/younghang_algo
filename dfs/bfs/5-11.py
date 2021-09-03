# 미로탈출 문제

# 탈출하는 최소의 거리를 구한다.
# 1. 큐에 넣을 때 거리까지 같이 넣을것인가 ?
# 2. ??????????????????????????????

from collections import deque 
n,m = map(int,input().split())
visited = [[False]*m for _ in range(n)]

arr = []
for i in range(n):
    arr.append(input())

#arr가 1이면 움직일 수 있다.
dir = [[1,0],[-1,0],[0,1],[0,-1]]
def bfs(starty,startx) :
    visited[starty][startx] = True
    q = deque()
    q.append((starty,startx,1))
    while q : 
        temp = q.popleft()
        y    = temp[0]
        x    = temp[1]
        cnt  = temp[2]
        print("(y,x,cnt)",y,x,cnt)
        #여기에 값이 들어가는게 맞나 확인바람.
        if (y == n-1 and x == m-1) :
            return cnt
        for i in range(4) :
            ny = y + dir[i][0]
            nx = x + dir[i][1]
            if (nx >=0 and nx < m and ny >=0 and ny < n and arr[ny][nx] == '1' and visited[ny][nx] == False ):
                q.append((ny,nx,cnt+1))

                visited[ny][nx] = True

print(bfs(0,0))

# 예는 들어 tuple를 정렬한다면 
# 정렬 기준이 들어가게 만들어보자. 1. sorted (array, key - >>>>>> 이거 확인하기)
