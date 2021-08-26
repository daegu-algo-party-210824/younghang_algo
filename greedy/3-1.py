# 거스름돈 문제
coins = [500,100,50,10]
n = int(input())
answer = 0

for i in coins :
    answer += n//i
    n = n%i

print("answer :" + str(answer))

# 그리디가 적용되는지 확인해야한다.
# 500/ 100 단위로 떨어지기 때문에 그리디가 사용가능한데
# 500/400/100 이런식으로 떨어질 경우에는 800을 넣으면 그리디를 사용할 수가 없다.
# 중요점 : 현재 가장 좋은 것만으로 선택을 할 경우 최적해가 나오는지 안나오는지 확인하면 가능하다.
