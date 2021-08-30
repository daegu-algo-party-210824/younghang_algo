# 그냥 크루스칼 외워라.
def find_parent (parent,a) :
    if a != parent[a] :
        parent[a] = find_parent(a)
    return parent[a]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)

    if a<b :
        parent[b] = a 
    else :
        parent[a] = b


for i in arr :
    if find_parent(i[0]) == find_parent(i[i]) :
        #사이클이 있다.
    else :
        #
        union_parent(parent,a,b)
        sum += 길이




