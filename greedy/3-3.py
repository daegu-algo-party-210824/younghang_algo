n,m = list(map(int,input().split()))

arr = []
max1 = 0

for i in range(n):
    arr.append (list(map(int,input().split())))
#print(arr)
for i in arr :
    max1 = max(max1,min(i))

print(max1)

