n = int(input())

distance = list(map(int,input().split(" ")))

values = list(map(int,input().split(" ")))

values = values[:len(values)-1]


price = values[0]
sum1  = values[0] * distance[0]
for i in range(1,len(values)):
    if (price > values[i]) :
        price = values[i]
    sum1+= price * distance[i]

print(sum1)