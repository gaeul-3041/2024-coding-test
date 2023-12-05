# 정확성만 해결, 효율성은 시간 초과 발생
from collections import deque
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r, c, land, visited):
    global answer
    n = len(land)
    m = len(land[0])
    
    q = deque()
    q.append((r, c))
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

def solution(land):
    global answer
    n = len(land)
    m = len(land[0])
    
    for i in range(m):
        visited = [[0] * m for i in range(n)]
        oil = 0
        for j in range(n):
            if land[j][i] == 1 and visited[j][i] == 0:
                visited[j][i] = 1
                oil += bfs(j, i, land, visited) + 1
        answer = max(answer, oil)
        print(oil, answer)
    
    return answer
