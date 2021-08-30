# 만들수 없는 금액 
# 생각하기 어렵다.
n = int(input())

data = list (map(int,input().split()))
data.sort()

impossibleValue = 1 

for i in data :
    # 초기값을 1로 두고 값보다 작은 값이 들어오면 
    # 더해주고 최대 값을 증가 시켜준다.

    if i <= impossibleValue :
        impossibleValue += i
    else :
        break

print(impossibleValue)