# 인덱스 값과 실제 값이 같은 값이 있는 경우 고정점이라고 하고 고정점을 구하자

def function (arr,start,end):
    if start > end :
        return -1
    mid = (start+end)//2
    if (mid == arr[mid]) :
        return mid
    elif (mid < arr[mid]) :
        return function(arr,start,mid-1)
    else :
        return function(arr,mid+1,end)

n = int(input())
arr = list(map(int,input().split()))

print(function(arr,0,len(arr)-1))


