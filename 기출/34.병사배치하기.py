n = int(input())

arr = list (map(int,input().split()))

dp = [0] * n
dp[0] =1

for i in range(n) :
    for j in range(i) :
        if (dp[j]+1 >= dp[i] and arr[i] < arr[j]):
            dp[i]= dp[j]+1

print(n - dp[n-1])


