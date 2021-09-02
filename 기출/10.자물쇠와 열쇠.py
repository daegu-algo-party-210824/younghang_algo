# 1.직접 다 만들기
# 2.함수화를 해서 간단하게 만들기.
def rotate(arr,n) :
    ret = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            ret [i][j] = arr[n-1-j][i]
    print(ret)
    return ret
def check(a,b,n,m) :
    #
    for i in range(m,n+m) :
        for j in range(m,n+m) :
            if (a[i][j] == 0 and b[i][j] == 0 ):
                return False
            if (a[i][j] == 1 and b[i][j] == 1):
                return False
    return True
            
    
def solution(key, lock):
    N = len(lock)
    M = len(key)

    arr1 = [[0]*(2*M+N) for i in range(2*M+N)]
    for i in range(M,N+M) :
        for j in range(M,N+M) :
            arr1[i][j] = lock[i-M][j-M]
    print(arr1)
    arr2 = [[0]*(2*M+N) for i in range(2*M+N)]
    isret = True
    
    for m in range(4):
        for i in range(M+N+1):
            for j in range(M+N+1):
                for k in range(M):
                    for l in range(M) :
                        arr2[k+i][l+j] = key[k][l]
                #print(arr2)
                if check(arr1,arr2,N,M)== True :
                    return True
                arr2 = [[0]*(2*M+N) for i in range(2*M+N)]
        key= rotate(key,M)
    #for i in range(M) :
    
    #    for i in range(M) :
    #        key
    return False 
        


print(solution ([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))

#1. rotation을 하기 어렵다.
