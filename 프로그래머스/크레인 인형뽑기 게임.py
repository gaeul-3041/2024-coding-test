def solution(board, moves):
    answer = 0
    n = len(board[0])
    line = [[] for i in range(n)]  # 기존 보드를 스택의 모음으로 변환
    outline = []
    
    # 가로 세로 길이가 동일하므로 둘 모두 편의상 n을 활용
    for i in range(n-1, -1, -1):
        for j in range(n):
            if board[i][j] > 0:
                line[j].append(board[i][j])
            
    for m in moves:
        if line[m-1]:
            p = line[m-1].pop()
            if outline and outline[-1] == p:
                answer += 2
                outline.pop()
            else:
                outline.append(p)
    
    return answer