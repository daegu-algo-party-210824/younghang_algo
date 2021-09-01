#인접리스트로 구현 

adj = [[]for i in range(10)]

adj[0].append((1,7))

adj[0].append((2,5))
adj[1].append((0,7))
adj[2].append((0,5))

print(adj)