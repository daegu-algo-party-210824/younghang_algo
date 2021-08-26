n = int(input())
arr = list(input().split())

x,y = 1,1

#y.x
dir = [[-1,0],[1,0],[0,1],[0,-1]]
dir_index = dict([])

dir_index["U"] = 0
dir_index["D"] = 1
dir_index["R"] = 2
dir_index["L"] = 3

for i in range(len(arr)) :
    ny = y + dir[dir_index[arr[i]]][0] 
    nx = x + dir[dir_index[arr[i]]][1]
    if (ny <1 or ny > n or nx <1 or nx > n) :
        continue
    y,x = ny,nx

print(y,x)


