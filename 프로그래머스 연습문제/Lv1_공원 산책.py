def solution(park, routes):
    answer = []
    px, py = 0, 0  # 이전 위치
    r, c = len(park), len(park[0])
    
    # 시작 위치 찾기
    for i in range(r):
        for j in range(c):
            if park[i][j] == 'S':
                px, py = i, j
                break
                
    cx, cy = px, py  # 현재 위치
                
    for route in routes:
        di, step = route.split()  # 방향, 거리
        move = True  # 이동 가능 여부
        
        # 이동 경로 안에 장애물 없는지 확인
        for i in range(1, int(step) + 1):
            if di == 'S' and 0 <= px + i < r and park[px + i][py] != 'X':
                cx += 1
            elif di == 'N' and 0 <= px - i < r and park[px - i][py] != 'X':
                cx -= 1
            elif di == 'E' and 0 <= py + i < c and park[px][py + i] != 'X':
                cy += 1
            elif di == 'W' and 0 <= py - i < c and park[px][py - i] != 'X':
                cy -= 1
                # 장애물 발견 시 즉시 중단
            else:
                move = False
                break
        
        if move:
            px, py = cx, cy
        else:
            cx, cy = px, py

    return [cx, cy]