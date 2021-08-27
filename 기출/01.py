n = int(input())
arr = list(map(int,input().split()))


ret = 0
arr.sort()

temp = arr[0]

for i in range(len(arr)):
    temp -= 1
    if temp == 0 and (i+1) < len(arr):
        temp = arr[i+1]
        ret +=1
   


