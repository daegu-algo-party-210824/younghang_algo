# 방법이 두개있는데 나는 재귀함수로 이진탐색 구현해보기

import sys


def binary_search(arr,start, end, value) :
    if start > end :
        return False
    mid = (start+end) //2

    if (arr[mid] == value) :

        return mid
    elif (arr[mid] < value) :
        return binary_search(arr, mid+1, end,value)
    else :
        return binary_search(arr,start,mid-1,value)

n, v = map(int,input().split())

arr = list(map(int,sys.stdin.readline().rstrip().split()))

arr.sort()



print(binary_search(arr,0,len(arr)-1,v))

# 주의 사항 빠르게 입력 받기




