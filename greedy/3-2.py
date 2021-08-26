n,m,k = list(map(int,input().split(" ")))

print(n,m,k)

arr = list(map(int,input().split(" ")))
arr.sort()
max1 = arr[len(arr)-1]
max2 = arr[len(arr)-2]

#m번더해서 최대의 수를 만든다.
#최대 k번을 더할 수 있다.

ret = (m//(k+1)) * (k*max1 + max2) + m%(k+1)

print(ret)




