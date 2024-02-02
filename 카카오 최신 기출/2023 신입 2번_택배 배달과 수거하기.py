def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 가장 먼 집부터 계산하기 위해 뒤집기
    deliveries.reverse()
    pickups.reverse()
    
    a = 0  # 배달할 물건 수
    b = 0  # 픽업할 상자 수
    
    for i in range(n):
        a += deliveries[i]
        b += pickups[i]
        
        # 배달할 물건이나 픽업할 상자가 없을 때까지 왕복, 왕복 거리만큼 기록
        while a > 0 or b > 0:
            a -= cap
            b -= cap
            answer += (n - i) * 2
    
    return answer