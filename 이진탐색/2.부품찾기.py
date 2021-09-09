#부품찾기 p197

def binary_search(arr,start,end,value) :
    if start>end :
        return -1
    mid = (start+end)//2

    if (arr[mid] == value):
        return mid
    elif (arr[mid] < value ):
        return binary_search(arr,mid+1,end,value) 
    else :
        return binary_search(arr,start,mid-1,value)
import sys
n = sys.stdin.readline().rstrip()
arr = list(map(int,input().split()))
arr.sort()


m = int(sys.stdin.readline().rstrip())


arr2 = list(map(int,input().split()))

for i in range(m) :
    print(binary_search (arr,0,len(arr)-1,arr2[i]))
#인덴스를 반환.



