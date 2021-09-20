# 41.여행계획
# 3 4 / 2 3 / 1 2 / 0 1 
# 케이스로 값을 넣었을 때에는 parent가 갱신되지 않는다.
# 대신에 0,4 로 find를 할때에 갱신이 된다.

N,M = map(int,input().split(" "))

parent = [i for i in range(N)]
# 최상단에 parent를 가져온다.

def find(a) :
    global parent
    if a != parent[a] :
        parent[a] = find(parent[a])
    return parent[a]
    
def union(a,b):
    global parent

    a = find(a)
    b = find(b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

arr = []
for i in range(1,N+1) :
    arr.append(list(map(int,input().split(" "))))

path = list(map(int,input().split(" ")))


# 연결하는 부분.
for i in range(N) :
    for j in range(N):
        if arr[i][j] == 1:
            union(i,j)
            


#부모만 체크하면 된다.
onlyparent = find(path[0])
flag = 1
for i in range(1,len(path)) :
    if onlyparent != find(path[i]-1):
        flag = 0


print(parent)
if (flag == 1) :
    print("YES")

else :
    print("NO")
    
