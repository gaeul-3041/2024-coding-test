# 2. 행렬 테두리 회전하기
# 각 코너별 직접 돌리는 작업 필요

def solution(rows, columns, queries):
    answer = []
    board = [[0] * (columns + 1) for i in range(rows + 1)]
    
    # 문제에서 제시한 방법 그대로 번호 부여
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            board[i][j] = (i - 1) * columns + j
            
    for x1, y1, x2, y2 in queries:
        head = board[x1][y1] # 가장 앞의 데이터는 마지막 덮어쓰기를 위해 따로 저장
        a = head # 테두리 내 최솟값을 저장할 변수
        
        # 왼쪽 모서리 - 위쪽이 아래쪽을 끌어들여 덮어씀
        for i in range(x1, x2):
            t = board[i + 1][y1]
            board[i][y1] = t
            a = min(a, t) # 현재 최솟값 a와 t를 비교
        
        # 아래쪽 모서리 - 왼쪽이 오른쪽을 끌어들여 덮어씀
        for i in range(y1, y2):
            t = board[x2][i + 1]
            board[x2][i] = t
            a = min(a, t)
            
        # 오른쪽 모서리 - 아래쪽이 위쪽을 끌어들여 덮어씀
        for i in range(x2, x1, -1):
            t = board[i - 1][y2]
            board[i][y2] = t
            a = min(a, t)
        
        # 위쪽 모서리 - 오른쪽이 왼쪽을 끌어들여 덮어씀
        for i in range(y2, y1, -1):
            t = board[x1][i - 1]
            board[x1][i] = t
            a = min(a, t)
        
        board[x1][y1 + 1] = head # 왼쪽 위 모서리 바로 오른쪽 칸은 head를 덮어씀
        answer.append(a)
    
    return answer
