n  = input()

max1 = 0
#브루트 포스 모든 경우 더하기.
def function (arr,cnt,n,ret) :
    global max1
    #처음에는 첫값을 갱신한다.
    if cnt==0:
        ret = int(arr[cnt])
    #탈출조건 ret의 값을 비교한다.
    if cnt == n-1 :
        #print(ret)
        max1 = max(ret,max1)
        return 
    #그 중간이라면 계속들어가서 값을 수행한다.
    if (cnt+1 < n):
        function(arr,cnt+1,n,ret*int(arr[cnt+1]))
        function(arr,cnt+1,n,ret+int(arr[cnt+1]))

function (n,0,len(n),0)

print(max1)






