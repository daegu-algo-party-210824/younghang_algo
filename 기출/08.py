
n = input()

arr = []
sum1 = 0
for i in range(len(n)):
    if ((n[i].isdigit())) :
        sum1 += int(n[i])
    else :
        arr.append(n[i])

arr.sort()

ret = ''

for i in range (len(arr)) :
    ret+=arr[i]
ret += str(sum1)

print(ret)

