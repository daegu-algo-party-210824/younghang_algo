#dfs graph는 인접리스트로 구현
graph = [
     [],
     [2,3,8],
     [1,7],
     [1,4,5],
     [3,5],
     [3,4],
     [7],
     [2,6,8],
     [1,7]]
def dfs (graph, visited,v) :
    if visited[v] == False :
        print("v 방문: ",v)
        visited[v] = True
        for i in graph[v]:
            dfs(graph,visited,i)

visited = [False]* 9


dfs(graph,visited,1)
