# 백준 알고리즘 1922 네트워크 연결
# 크루스칼 : 주의점 parent를 최상단으로 모두 초기화해야한다.
N = int(input())
M = int(input())
parent = [i for i in range(N+1)]


#최상단 부모를 찾는 알고리즘.
def unionfind(parent,a) :
    if parent[a] == a:
        return a
    return unionfind(parent,parent[a])

def union(parent,a,b) :
    #이부분이 잘 이해가 안가는데?
    a = unionfind(parent,a)
    b = unionfind(parent,b)
        
    if (a<b) :
        parent[b] = a
    else :
        parent[a]=b
edge = []
for i in range(M):
    temp = list(map(int,input().split()))
    edge.append ((temp[2],temp[0],temp[1]))

edge = sorted(edge,key=lambda x : x[0])

result = 0

for i in range(M):
    a = unionfind(parent,edge[i][1])
    b = unionfind(parent,edge[i][2])

    if (a != b) :
        union(parent,edge[i][1],edge[i][2])
        result += edge[i][0]


print(result)




