## 큐를 이용한 문제 풀이 
## 정확도 ok! 
## 효율성 실패!
from collections import deque
def solution (food_times,k) :
    q = deque([])
    # (시간,노드)
    for i in range(len(food_times)):
        q.append( (food_times[i],i+1) )

    print(1)

    cnt = 0 
    temp = 0
    while (q and cnt < k) :
        temp = q.popleft()
        if (temp[0] - 1 > 0 ) :
            q.append((temp[0]-1,temp[1]))
        cnt +=1
    if not q :
        return -1 
    else :
        return q[0][1]
