tmp = []
arr = []
dir = [[0,-1],[-1,-1],[0,-1],[1,-1],[0,1],[1,1],[0,1],[-1,1]]

def make_list(arr) :
    list1 = []
    for i in range(4) :
        for j in range(4) :
            if (arr[i][j] != 17) :
                list1.append(list((arr[i][j][0], arr[i][j][1]-1 , i, j)))
    list1 = sorted(list1)

    for i in range(len(list1)):
        x = list1[i][3]
        y = list1[i][2]
        direction = list1[i][1]

        ny = y + dir[direction][0]
        nx = x + dir[direction][1]

        while(True) :
            if ny >= 0 and ny < 4 and nx >= 0 and nx < 4 and arr[ny][nx][0] != 17:
                break
            direction +=1
            direction = direction%8  
            ny = y + dir[direction][0]
            nx = x + dir[direction][1]

        if (ny >= 0 and ny < 4 and nx >= 0 and nx < 4):
            # 스왑이 가능하면 스왑하자.
            arr[y][x] = (arr[y][x][0],direction+1)
            
            arr[y][x] , arr[ny][nx] = arr[ny][nx] , arr[y][x]
            print(arr)
  
    return list1,arr

def dfs (arr,sy,sx) :
    arr[sy][sx] = (17,arr[sy][sx][1])
    list1,arr = make_list(arr)
    
    x = sx
    y = sy
    direction = arr[y][x][1]

    
    ny = y + dir[direction][0]
    nx = x + dir[direction][1]

    while(True) :
        if ny >= 0 and ny < 4 and nx >= 0 and nx < 4 :
            break
        direction +=1
        direction = direction%8  
        ny = y + dir[direction][0]
        nx = x + dir[direction][1]
    
    while (ny >= 0 and ny < 4 and nx >= 0 and nx < 4) :
        #arr[ny][nx] , arr[y][x] = arr[y][x] , arr[ny][nx]
        prior = arr[y][x]
        next = arr[ny][nx]
        arr[y][x][0] = (0,arr[y][x][1])
        arr[ny][nx][0] = (17,arr[y][x][1])
        dfs(arr,ny,nx)
        arr[y][x] = prior
        arr[ny][nx] = next    

    
for i in range(4) :
    tmp.append (list(map(int,input().split(" "))))

for i in range(4) :
    tmp2=[]
    for j in range(0,8,2):
        tmp2.append((tmp[i][j],tmp[i][j+1]))
    arr.append(tmp2)    

print(arr)

dfs (arr,0,0)



