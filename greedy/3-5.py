n,k = list(map(int,input().split()))

cnt = 0
########################################
'''while (n!= 1):
    #여기에서는 10만까지 밖에 되지 않을 수도 있다.
    if (n % k == 0):
        n = n//k
    else :
        n = n-1
    cnt +=1

print(cnt)
'''
#######################################

# 1. 한번에 나눌수 있는거를 한꺼번에 나누고
# 2. 뺀다.

cnt = 0

while(n!= 1):
    #나눌때는 한꺼번에 나눠서 n을 줄이자
    while (n % k != 0):
        n = n-1
        cnt +=1
    n = n//k
    cnt +=1
    
    
print(cnt)






