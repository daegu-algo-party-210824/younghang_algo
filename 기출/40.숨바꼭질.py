from collections import deque 
n,m = map(int,input().split())

graph = [[]for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split(" "))
    graph[a].append((1,b))



