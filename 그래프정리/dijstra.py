# 그냥 다익스트라 외워라

import heapq

#
n,m= map(int,input().split())
start = int(input())
visited = [False] * (n+1)
distance = [1e9] * (n+1)
adj = [[] for i in range(n+1)]
for i in range(m):
    temp = list(map(int,input().split()))
    adj[temp[0]].append((temp[1],temp[2]))
# 시작점이 필요


q= []
# (거리, 노드)
distance[start] = 0
heapq.heappush(q,(0,start))

while q :
    #최소길이를 찾는다.
    dis,current = heapq.heappop(q)
    #여기에서 조심. 
    if (dis > distance[current]):
        continue
    #최소길이에서 갈 수 있는 경우를 모두 넣는다.
    for i in adj[current]:
        cost = dis + i[1]
        #여기에 조심. 
        if (cost < distance[i[0]]):
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

print(distance)    

######################################
q=[]
heapq  (q,(0,start))
while q :
    dis , now = heapq.heappop(q)
    if (dis > distance[now]):
        continue
    for i in adj[now] :
        cost = i[1] + dis
        if (cost < distance[i[0]]):
            distance[i[0]] = cost 
            heapq.heappush(q,(cost,i[0]))

