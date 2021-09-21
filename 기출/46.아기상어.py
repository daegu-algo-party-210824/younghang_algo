# 46.아기상어


# 구해야 되는거 : 엄마상어에게 요청하기 전까지의 시간 
# 초기 상어의 크기는 2 
# 크기의 갯수만큼 먹어야지 성장한다.
# BFS 돌려서 가장 가까운거를 먹는데 이때 거리롤 위치를 반환한다
# BFS 돌릴때에는 (위쪽, 왼쪽) 순서로 먹는다
# 
# 

from collections import deque
n = int(input())
arr = []
for i in range(n) :
    arr.append(list(map(int,input().split())))

def find(visited,min_value,arr,size):
    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[i][j] == min_value and arr[i][j] >0 and size > arr[i][j]:
                return (i,j)
    return (-1,-1)
#시작점 가지고 끝점을 반환한다.
def bfs (arr,size,sy,sx):
    global n
    visited = [[0]*(n) for i in range(n)]
    visited[sy][sx] = 1
    min_value = int(1e9)
    dir = [[-1,0],[0,-1],[0,1],[1,0]]

    q = deque([])
    q.append((sy,sx))
    short = []
    # 갈수 있는 거리를 모두 판단한 뒤에 
    while q :
        y,x = q.popleft()

        if (arr[y][x] < size and (arr[y][x] != 0 and arr[y][x] != 9)) :
            min_value = min (visited[y][x],min_value)
        
        for i in range(4) :
            ny = y + dir[i][0]
            nx = x + dir[i][1]
            if ny >=0 and ny < n and nx >=0 and nx < n and visited[ny][nx] == 0 :
                if (arr[ny][nx] <= size) :
                    visited[ny][nx] = visited[y][x] +1
                    q.append((ny,nx))
    return visited,min_value

def find_yx (arr):    
    for i in range(n) :
        for j in range(n) :
            if (arr[i][j] == 9 ):
                return [i,j] 


sy,sx= find_yx(arr)
time = 0
size = 2
size_cnt = 0
min_value = int(1e9)

while (True) :
    beforey, beforex = sy,sx
    visited,min_value = bfs(arr,size,sy,sx)
    sy,sx = find(visited,min_value,arr,size)
    #탈출 조건 (갈 수 있는 지 없는지)
    
    if (min_value == int(1e9) or (sy ==-1 and sx ==-1)):
        break
    time += (min_value-1)
    
    size_cnt +=1
    if (size == size_cnt) :
        size +=1
        size_cnt = 0

    arr[beforey][beforex] = 0
    arr[sy][sx] = 9


#print(arr)
print(time)





    