

product = list(input())
genuine = list(input())

dic = dict([])


for i in product:
    if (i in dic ):
        dic[i] = dic[i]+1
    else :
        dic[i] = 0

print(dic)
