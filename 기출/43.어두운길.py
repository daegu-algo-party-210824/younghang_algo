# 43.어두운길.py


# 크루스칼 써서 최소 스패닝 트리를 구한다.
# 이후 현재의 크기와 mst의 간선의 합을 빼준다.


N,M = map(int,input().split())

def find (parent, a) :
    if parent[a] != a :
        parent[a] = find(parent,parent[a])
    return parent[a]

def union(parent,a,b) :
    a = find(parent,a)
    b = find (parent,b)
    if (a<b) :
        parent[b] = a 
    else :
        parent[a] = b
    return

edge = []
parent = [ i for i in range(N)]
total = 0
for i in range(M) :
    x,y,z = map(int,input().split())
    edge .append ((z,x,y))
    total += z

edge = sorted(edge, key = lambda x : x[0])

dist = 0
for i in range(len(edge)) :
    z,x,y = edge[i]
    if find(parent,x) != find(parent,y) :
        union(parent,x,y)
        dist += z 

print(total-dist)

# 1. 크루스칼을 쓸려면 정렬해야한다.