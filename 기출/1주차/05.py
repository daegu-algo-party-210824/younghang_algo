# 05 볼링공 고르기 
# 1. 서로 다른 무게를 뽑을 려고 한다.
# 그냥 포문 두개로 다르면 추가한다.
# 이 때 (1,2) == (2,1) 하나로 치기 때문에 i<j의 조건을 준다.
n,m = map(int,input().split())

arr = list(map(int,input().split()))

cnt = 0

for i in range(len(arr)) :
    for j in range(len(arr)) :
        if ( i < j and arr[i] != arr[j]):
            cnt+=1
print(cnt)


