#1. 한점에서 다른 점으로 가는 거라서 다익스트라를 쓸수도 있다.
#2. 하지만 길이가 1로 동일하기 때문에 BFS를 사용하는게 더 용이하다.

import heapq
def dijkstra (start,graph,n):
    distance = [1e9] * (n+1)
    #(거리,노드)
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    #이거 다일까?
    while q:
        dis, now = heapq.heappop(q)
        if (dis > distance[now]):
            continue
        for i in graph[now] :
            if (dis+1 < distance[i] ):
                heapq.heappush(q,( dis +1,i))
                distance[i] = dis+1
    return distance


n,m,k,x = list(map(int,input().split(" ")))
#print(n,m,k,x)
graph = [[]for i in range(n+1)]
for i in range(m) :
    s,e = map(int,input().split())
    graph[s].append(e)

a = (dijkstra(x,graph,n))

ret = []
for i in range(1,n+1):
    if (k == a[i]):
        ret.append(i)
if len(ret) > 0 :
    for i in ret :
        print(i)
else :
    print("-1")


