# 4. 거리두기 확인하기
# 2021 카카오 기출
# BFS 풀이를 썼지만, 크기가 작으니 그냥 각 칸 별 브루트 포스도 가능할 듯

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

def bfs(r, c, board):
    q = deque()
    q.append((r, c, 0))
    visited = [[0] * 5 for i in range(5)]
    visited[r][c] = 1
    
    while q:
        x, y, cnt = q.popleft()
        # 1명이라도 위반 사례가 있으면 False를 반환
        if board[x][y] == 'P' and cnt > 0:
            return False
        # 2칸보다 멀리 떨어진 경우
        if cnt > 2:
            continue
        # 모든 방향에 대해 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 안인가? 방문한 적 없는가? 파티션이 아닌가? 2칸 내인가?
            # 파티션이 있다면 그 뒤는 고려하지 않아도 된다
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0 and board[nx][ny] != 'X' and cnt < 2:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = 1

    # 마지막까지 위반 사례가 없다면 True를 반환      
    return True

def solution(places):
    # 각 대기실 별로 BFS 실행
    for place in places:
        board = []

        # 문자열을 리스트 형태로 변환
        for i in range(5):
            board.append(list(place[i]))
            
        ans = True # 거리두기 여부를 판단할 boolean 변수
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'P':
                    ans = ans & bfs(i, j, board) # P인 칸에 대해 BFS 실행, and 연산으로 결과 받기 
        
        if ans:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer