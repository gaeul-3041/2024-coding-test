n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
dfs(1)

answer = visited.count(1) - 1
print(answer)