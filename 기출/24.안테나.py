n = int(input())
arr = list(map(int,input().split()))
arr.sort()

# 짝수일때
if n%2 == 0 :
    temp1 = arr[n//2]
    temp2 = arr[n//2-1]
    sum1 = 0
    for i in range(n) :
        sum1 += arr[i] - temp1
    sum2 = 0
    for i in range(n) :
        sum2 += arr[i] - temp2

    if sum1 < sum2 :
        print(temp2)
    else :
        print(temp2)
if n%2 ==1 :
    temp1 = arr[n//2]
    print(temp1)