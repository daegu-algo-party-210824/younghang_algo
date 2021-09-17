n = int(input())
arr = input()

def dfs (cnt,n,value):
    global arr 
    if cnt >= n :
        #최대값 갱신
        return
    # 1.괄호를 추가하는 경우

    if cnt +1 == "*":
        temp = int(arr[cnt]) * int(arr[cnt+2])
        dfs(cnt+3,n,temp)
    
    if cnt +1 == "+":
        temp = int(arr[cnt]) + int(arr[cnt+2])
        dfs(cnt+3,n,temp)
    
    if cnt +1 == "-":
        temp = int(arr[cnt]) - int(arr[cnt+2])
        dfs(cnt+3,n,temp)
    
    
    
    # 2.바로 계산하는경우
