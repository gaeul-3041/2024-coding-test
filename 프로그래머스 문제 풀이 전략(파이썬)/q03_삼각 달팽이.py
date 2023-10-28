# 3. 삼각 달팽이
# n, n-1, n-2 ... 1회 동작, 3가지 방향 순환

def solution(n):
    answer = []
    board = [[0] * n for i in range(n)]
    x, y = -1, 0 # 시작점은 (-1, 0)으로, 좌표계가 아닌 배열 인덱스 기준
    cnt = 0 # 방향을 결정할 변수
    num = 1
    
    for i in range(n, 0, -1): # 매번 동작 횟수는 n부터 1까지 1씩 감소
        # 현재 방향 결정: cnt를 3으로 나눈 나머지
        if cnt % 3 == 0:
            for j in range(i):
                x += 1
                board[x][y] = num
                num += 1
                
        elif cnt % 3 == 1:
            for j in range(i):
                y += 1
                board[x][y] = num
                num += 1
        
        else:
            for j in range(i):
                x -= 1
                y -= 1
                board[x][y] = num
                num += 1
                
        cnt += 1
        
    for i in range(n):
        for j in range(i + 1):
            answer.append(board[i][j])
                
    return answer