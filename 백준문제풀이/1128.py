import heapq
import sys

n = int(sys.stdin.readline().rstrip())


q1 = []
q2 = []

heapq.heapify(q1)
heapq.heapify(q2)

for i in range(n) :
    a = int(sys.stdin.readline().rstrip())
    if a == 0 :
        if len(q1) == 0 and len(q2) == 0 :
            print(0)
            continue
        if len(q1) == 0 and len(q2) != 0 :
            print(-heapq.heappop(q2))
            continue
        if len(q1) != 0 and len(q2) == 0 :
            print(heapq.heappop(q1))
            continue
    
        if q1[0] < q2[0] :
            print(heapq.heappop(q1))
        else :
            print(-heapq.heappop(q2))
    else :
        if a > 0 :
            heapq.heappush(q1,a)
        else :
            heapq.heappush(q2,-a)    

