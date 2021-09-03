#arr
def dfs (arr,visited,y,x,N,cnt,min1,max1) :
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    if (visited[y][x] == 0) :
        visited[y][x] = cnt
        for i in range(4):
            ny = y + dir[i][0]
            nx = x + dir[i][1]
            if (ny >=0 and ny < N and nx >= 0 and nx <N and visited[ny][nx] == 0) :
                #여기에서 갈 수 있는 조건을 추가한다.
                if (abs(arr[ny][nx] - arr[y][x]) >= min1 and abs (arr[ny][nx] - arr[y][x]) <= max1) :
                    dfs(arr,visited,ny,nx,N,cnt,min1,max1)
#
def make_visited(arr,visited) :
    cnt = 1
    for i in range(N) :
        for j in range(N):
            if (visited[i][j] == 0) :
                dfs(arr,visited,i,j,N,cnt,L,R)
                cnt +=1
    return visited

def arr_chagen(arr,visited) :
    max1 = 0
    for i in range(N) :
        for j in range(N) :
            max1 = max(max1,visited[i][j]) 

    for cnt in range(1,max1+1) :
        sum1= 0
        count =0
        for i in range(N) :
            for j in range(N) :
                if (visited[i][j] == cnt ):
                    sum1 += arr[i][j]
                    count +=1
        if (count >0 ):
            sum1 = sum1//count
            for i in range(N) :
                for j in range(N) :
                    if (visited[i][j] == cnt ):
                        arr[i][j] = sum1
    return arr

#
def check (visited) :
    temp = visited[0][0]
    for i in range(N):
        for j in range(N):
            if (visited[i][j] != temp) :
                return False 
    return True


arr = []
N,L,R = list(map(int,input().split()))
for i in range(N) :
    arr.append(list(map(int,input().split())))

visited = [[0]*N for i in range(N)]
#여기에서 visited 
make_visited(arr,visited)
ccc = 0
while (True) :
    # 처음에 판단해야한다. 탈출할 수 있는지 없는지 ?    
    if (check(visited) == True) :
        break
    make_visited(arr,visited)
    print(arr_chagen(arr,visited))
    visited = [[0]*N for i in range(N)]
    ccc +=1
        
print(ccc)





# 
