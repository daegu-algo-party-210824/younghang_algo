
#1.국어점수가 감소하는 순으로
#2.영어점수가 감소하는 순으로
#3.수학점수가 감소하는 순으로
#4.사전순으로 증가하는 순으로

n = int(input())

arr = []
for i in range(n) :
    temp = input().split()
    arr.append ((temp[0],int(temp[1]),int(temp[2]),int(temp[3])))

a = sorted(arr,key = lambda x : (-x[1],x[2],-x[3],x[0]))

for i in range(len(a)) :
    print(a[i][0])