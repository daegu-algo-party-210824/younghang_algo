#벨만 포드.
def solution (arr,n) :

    for k in range(1,n+1) :
        for i in range(1,n+1):
            for j in range(1,n+1) :
                arr[i][j] = min (arr[i][j] + arr[j][k] , arr[i][j])
