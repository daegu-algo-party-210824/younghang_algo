# 연구소 문제 
# bfs (큐에 여러 개를 넣고 갱신한다.)
# 주의사항 : deepcopy 
# itertools import combinations -> 모든경우를 만든다. 

from itertools import combinations 
from collections import deque
import copy

def bfs(arr):
    dir = [[-1,0],[1,0],[0,1],[0,-1]]
    q = deque([])
    for i in range(N) :
        for j in range(M):
            if arr[i][j] == 2 :
                q.append((i,j))

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dir[i][0]
            nx = x + dir[i][1]
            if (ny >= 0 and ny <N and nx >=0 and nx < M and arr[ny][nx] == 0):
                arr[ny][nx] = 2
                q.append((ny,nx))
    ret = 0
    for i in range(N) :
        for j in range(M):
            if arr[i][j] == 0 :
                ret +=1
    return ret

N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split(" "))))

dd= []
for i in range(N) :
    for j in range(M) :
        if (arr[i][j] == 0) :
            dd.append((i,j))

arr1 = list(combinations(dd,3))
#print(arr)
max1 = 0
for i in arr1 :
    #여기에서 arr 변경해주자.
    temp = copy.deepcopy(arr)

    temp[i[0][0]][i[0][1]] = 1
    temp[i[1][0]][i[1][1]] = 1
    temp[i[2][0]][i[2][1]] = 1
    
    max1 = max(max1,bfs(temp))

    temp[i[0][0]][i[0][1]] = 0
    temp[i[1][0]][i[1][1]] = 0
    temp[i[2][0]][i[2][1]] = 0

print(max1)
    
