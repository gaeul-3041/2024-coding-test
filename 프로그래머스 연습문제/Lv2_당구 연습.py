def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        tmp = 10000000
        
        # 위, 오른쪽, 아래, 왼쪽 벽을 각각 맞추고 가는 최소의 거리
        d1 = (startX - x) ** 2 + (startY - 2 * n + y) ** 2
        d2 = (startX - 2 * m + x) ** 2 + (startY - y) ** 2
        d3 = (startX - x) ** 2 + (startY + y) ** 2
        d4 = (startX + x) ** 2 + (startY - y) ** 2
        
        # 공의 위치에 따라 원쿠션이 불가능한 경우를 제외하고 최솟값 찾기
        if startY == y and startX > x:
            tmp = min(tmp, d1, d2, d3)
        elif startY == y and startX < x:
            tmp = min(tmp, d1, d3, d4)
        elif startX == x and startY > y:
            tmp = min(tmp, d1, d2, d4)
        elif startX == x and startY < y:
            tmp = min(tmp, d2, d3, d4)
        else:
            tmp = min(tmp, d1, d2, d3, d4)
            
        answer.append(tmp)
    
    return answer