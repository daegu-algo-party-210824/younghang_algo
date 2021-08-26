from collections import deque 

def bfs (graph, start, visited) :
    visited[start] = True
    q = deque([start])

    while q :
        temp = q.popleft()
        print(temp)
        for i in graph[temp]:
            if visited[i] == False :
                q.append(i)
                visited[i] = True
#adj 리스트
graph = [
    [],
    [2,3,8],      #1은 2,3,8과 연결됨.
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9 

bfs(graph,1,visited)
