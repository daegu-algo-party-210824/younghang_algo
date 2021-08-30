n = int(input())
arr = list(map(int,input().split()))


ret = 0
arr.sort()

temp = 0 

for i in range(len(arr)):
    temp += 1
    if temp >= arr[i] :
        ret +=1
        temp = 0

print(ret)

   


