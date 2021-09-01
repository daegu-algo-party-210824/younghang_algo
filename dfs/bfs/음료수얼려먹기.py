#음료수 얼려먹기 
#dfs로 구현해서 
#방문할 수 있으면 cnt하고 같은 것들은 1로 갱신해준다.

n , m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input())))

#
def dfs (y,x) :
    #1이면 들어가지 않는다.
    if (arr[y][x] == 1):
        return
    dir = [[-1,0],[1,0],[0,1],[0,-1]]
    if (arr[y][x] == 0) :
        arr[y][x] = 1
        for i in range(4):
            ny = y + dir[i][0]
            nx = x + dir[i][1]
            if (ny >= 0 and ny < n and nx >=0 and nx < m and arr[ny][nx] ==0 ):
                dfs(ny,nx)
                #다시 초기화 시킬 필요는 없다./
cnt = 0
for i in range(n):
    for j in range(m):
        if (arr[i][j] == 0) :
            cnt +=1
            dfs(i,j)

print(cnt)
        
'''
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
'''

