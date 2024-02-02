def solution(dirs):
    road = set()  # 중복 제거를 위한 set 선언
    x, y = 0, 0
    
    for dir in dirs:
        nx, ny = x, y
        if dir == 'U':
            ny += 1
        elif dir == 'D':
            ny -= 1
        elif dir == 'L':
            nx -= 1
        else:
            nx += 1
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        
        # 왕복 길을 모두 업데이트해 중복 방지
        road.add((x, y, nx, ny))
        road.add((nx, ny, x, y))
        x, y = nx, ny
    
    return len(road) / 2
