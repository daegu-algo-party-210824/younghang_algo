from collections import deque
# deque는 bfs를 위해서 필요하다.
q = deque([])

q.append(1)
print(q)
q.append(2)
print(q)
q.append(3)
print(q)
q.append(4)
print(q)

q.popleft()
print(q)
q.popleft()
print(q)
q.popleft()
print(q)
q.popleft()
print(q)

