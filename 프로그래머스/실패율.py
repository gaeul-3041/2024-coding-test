def solution(N, stages):    
    player = [0] * (N+2)  # 스테이지별 유저 분포
    fail = {}  # 실패율은 딕셔너리로 정의
    k = len(stages)  # 총 플레이어 수
    
    for stage in stages:
        player[stage] += 1
        
    for i in range(1, N+1):
        if player[i] == 0:
            fail[i] = 0
        else:
            fail[i] = player[i] / k
            k -= player[i]  # 해당 단계에서 멈춘 유저 제외

    # 값에 따라 내림차순 정렬
    answer = sorted(fail, key = lambda x: fail[x], reverse=True)
    
    return answer
