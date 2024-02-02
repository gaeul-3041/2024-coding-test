from collections import deque

n = int(input())
ocean = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
shark_x, shark_y = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((shark_x, shark_y))

for i in range(n):
    for j in range(n):
        if ocean[i][j] == 9:
            shark_x, shark_y = i, j
            ocean[i][j] = 0
            break
        
size = 2  # 현재 사이즈
eat = 0  # 현재 먹은 물고기 수, 성장할 때마다 0으로 초기화
time = 0  # 총 소요 시간(정답)

## To do