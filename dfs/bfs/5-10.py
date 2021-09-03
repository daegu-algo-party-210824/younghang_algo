# 음료수 얼려먹기
def dfs (y,x):
    global dir
    global n
    global m
    global visited
    global arr
    visited[y][x] = True
    print("(y,x) : ",y,x)
    for i in range(4) :
        ny = y + dir[i][0]
        nx = x + dir[i][1]
        if (ny >=0 and ny < n and nx >=0 and nx < m and visited[ny][nx] == False and arr[ny][nx] == '0') :
            dfs(ny,nx)
            

from collections import deque

n,m = list(map(int,input().split()))
arr = []
dir = [[1,0],[-1,0],[0,1],[0,-1]]
# 2차원 배열 
visited = [[False]*m for _ in range(n)] 
for i in range(n):
    arr.append(input())

cnt = 0

for i in range(n) :
    for j in range(m) :
        if visited[i][j] == False and arr[i][j] == '0':
            dfs(i,j)
            cnt +=1
            print(cnt)
print(cnt)

# TC
'''
case
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

8

case 2 
4 5    
00110
00011
11111
00000

3
'''





