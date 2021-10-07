import sys

n = int(input())
set1 = set([])
for i in range(n) :
    temp = sys.stdin.readline().rstrip().split()
    if len(temp) == 1:
        moduler = temp[0] 
        if moduler == "all" :
            set1 = set([i for i in range(1,21)])

        if moduler == "empty" :
            set1 = set([])
    else :

        moduler = temp[0] 
        num = int(temp[1])
        if moduler == "add" :
            set1.add(num)
        if moduler == "remove" :
            if num in set1 :
                set1.remove(num)

        if moduler == "check" :
            if num in set1 :
                print(1)
            else :
                print(0)
        if moduler == "toggle" :
            if num in set1 :
                set1.remove(num)
            else :
                set1.add(num)



