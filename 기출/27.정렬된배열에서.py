from bisect import bisect_right, bisect_left
n,x = map(int,input().split())

arr = list(map(int,input().split()))

print (bisect_right(arr,x))

print (bisect_left(arr,x))

if bisect_right(arr,x) != bisect_left(arr,x)  :
    print(bisect_right(arr,x)-bisect_left(arr,x))
else :
    print(-1)


