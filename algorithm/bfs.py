import sys
from collections import deque

cnt = 1

def bfs(graph, s, visited):
    global cnt
    q = deque([s])
    visited[s] = 1

    while q:
        u = q.popleft()
        graph[u].sort()
        for g in graph[u]:
            if not visited[g]:
                cnt += 1
                visited[g] = cnt
                q.append(g)

# 입력 받기
N, M, R = map(int, sys.stdin.readline().split())

# graph 만들기
graph = [[] for x in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

bfs(graph, R, visited)

# 순서 출력
for i in visited[1:]:
    print(i)