# 병사 배치하기
# 초기에 dp를 모두 1로 갱신하는게 생각하기 어렵다
# 시간복잡도는 n^2 이다
# 전형적인 LIS 문제
n = int(input())

arr = list (map(int,input().split()))

dp = [1] * n


for i in range(n) :
    for j in range(i) :
        if (dp[j]+1 >= dp[i] and arr[i] < arr[j]):
            dp[i]= dp[j]+1

print(n - max(dp))



