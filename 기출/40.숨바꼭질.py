# 1. bfs
# bfs를 쓰려고 하니깐 20000*20000의 배열 크기가 필요하다
# 400000000 : 4억 .... 정도로 매우 큰 편이다 
# 시작점은 일정하고 ElogE 이런걸로 할 수 있는 다익스트라가 더 좋다.
def dijkstra(graph,start,n) :
    dp = [1e9] *(n+1)

    q = []
    heapq.heapify(q)
    heapq.heappush(q,(0,start))
    dp[start] = 0
    # (코스트, 위치) // i[0],i[1]
    while q :
        dis,now = heapq.heappop(q)
        # 현재 값이 빼봣더니 크면 넘김
        if (dis > dp[now]):
            continue
        # 여기에서 다음껄로 가면서 갱신이 되는 경우에는 큐에 넣는다.
        
        for i in graph[now]:
            #여기서 코스트로 값을 설정해주면 안 헷갈린다.
            cost = dis+ i[1]
            if cost < dp[i[0]] :
                dp[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return dp
                
import heapq

from collections import deque 
n,m = map(int,input().split())

graph = [[]for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split(" "))
    graph[a].append((b,1))
    graph[b].append((a,1))

ret = (dijkstra(graph,1,n))

max1 = 0
index = -1
cnt = 0

for i in range(1,n+1):
    if max1 < ret[i] and ret[i] != 1e9:
        max1 = ret[i]
# index 찾기.
for i in range(1,n+1) :
    if max1 == ret[i] :
        index = i
        break
# cnt 찾기
for i in range(1,n+1):
    if max1 == ret[i] :
        cnt +=1

print(index, max1, cnt)








