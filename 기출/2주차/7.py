#ㄹㅓㄱ키 스스트트레레이이트
#럭키 스트레이트
num = input()

sum1 = 0
sum2 = 0

for i in range(len(num)//2) :
    sum1+= int(num[i])

for i in range(len(num)//2,len(num)) :
    sum2 += int(num[i])


print(sum1,sum2)
if (sum1 == sum2) :
    print("LUCKY")
else:
    print("READY")