# p349 재귀함수로 모든 경우를 탐색함 .
# 오랜만에 백준으로 풀어서 출력오류....
all_value = []
#+-*/
def function (cnt,n,arr,ddd,value) :
    if cnt == n :
        all_value.append(value)
        return 
    if (ddd[0] >0) :
        ddd[0] -=1 
        function(cnt+1,n,arr,ddd,value+arr[cnt])
        ddd[0] +=1 
    if (ddd[1] >0) :
        ddd[1] -=1 
        function(cnt+1,n,arr,ddd,value-arr[cnt])
        ddd[1] +=1
    if (ddd[2] >0) :
        ddd[2] -=1 
        function(cnt+1,n,arr,ddd,value*arr[cnt])
        ddd[2] +=1
    if (ddd[3] >0) :
        ddd[3] -=1 
        if value <0 :
            value *= -1
            value = value // arr[cnt]
            value *= -1
            function(cnt+1,n,arr,ddd,value)
        else :
            function(cnt+1,n,arr,ddd,value//arr[cnt])
        
        ddd[3] +=1
    return

n = int(input())

arr = list(map(int,input().split()))

ddd = list(map(int,input().split()))

print(all_value)
function(1,len(arr),arr,ddd,arr[0])

print(int(max(all_value)))
print(int(min(all_value)))

