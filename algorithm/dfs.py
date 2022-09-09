import sys

sys.setrecursionlimit(10 ** 6)

cnt = 1

def dfs(graph, s, visited):
    global cnt
    visited[s] = cnt

    for i in graph[s]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)

# 입력 받기
n, l, s = map(int, sys.stdin.readline().split())
li = []

for _ in range(l):
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort()

# graph 만들기
graph = [[x] for x in range(n+1)]

for i in range(l):
    graph[li[i][0]].append(li[i][1])
    graph[li[i][1]].append(li[i][0])

for i in range(5):
    graph[i].pop(0)

visited = [0] * (n+1)


dfs(graph, s, visited)

# 순서 출력
for i in range(n+1):
    if i!=0:
        print(visited[i])