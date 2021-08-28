#문자열 뒤집기
#


# 아이디어 연결된 숫자들을 하나의 1 혹은 0으로 취급한다.
# 그 중에서 적은 숫자를 많은 숫자로 변경하는 작업을 수행한다. 
arr = input()
cnt_zero = 0
cnt_one  = 0

temp = arr[0]
if temp == '1':
    cnt_one +=1
else :
    cnt_zero +=1

for i in range(1,len(arr)):
    if temp != arr[i] :
        if arr[i] == '0' :
            cnt_zero +=1
        else :
            cnt_one +=1
        temp = arr[i]

#print(cnt_zero)
#print(cnt_one)


print(min (cnt_zero,cnt_one))
