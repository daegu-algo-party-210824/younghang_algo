# 너무 더러운데 .....
def solution (s) :
    min1 = len(s)
    if len(s)== 1:
        return 1

    for n in range(1,len(s)//2+1):
        arr = []
        i = 0
        #1. arr에 담는다.
        while (i < len(s)):
            arr.append(s[i:i+n])
            i += n
        #print(arr)
        sum = 1
        temp = []
        for i  in range(0,len(arr)-1):
            if (arr[i] == arr[i+1]):
                sum += 1
            else :
                temp.append(sum)
                sum =1
        temp.append(sum)
        #print(temp)
        temp2 = 0

        for k in  temp :
            if (k == 1):
                temp2 +=  n
            else :
                temp2 += len(str(k))+n

        if (len(s) % n != 0) :
            temp2 -= n- len(s)%n
        
        #print(temp2)
        min1 = min(temp2,min1)


        temp.clear()
        arr.clear()
    return min1

#print  ("min : " +str(solution('aabbaccc')))