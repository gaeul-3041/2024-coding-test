def solution(plans):
    answer = []
    process = []
    
    # 시작 시간을 정수로 변환 및 소요 시간을 정수형으로 변환
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
    
    # 시작 시간 순으로 정렬
    plans.sort(key = lambda x : x[1])
    
    for i in range(len(plans) - 1):
        name, start, playtime = plans[i]  # 현재 과제
        next_name, next_start, next_playtime = plans[i+1]  # 다음 과제
        
        # 현재 과제를 하고 시간이 남을 경우
        if start + playtime <= next_start:
            answer.append(name)
            left_time = next_start - (start + playtime)
            
            # 남은 시간만큼 최근 과제부터 다시 수행
            while left_time > 0 and process:
                n, s, p = process.pop()
                if left_time >= p:
                    answer.append(n)
                    left_time -= p
                else:
                    process.append([n, s, p - left_time])
                    left_time = 0
        
        # 제 시간에 과제가 불가능할 경우
        else:
            playtime -= (next_start - start)  # 남은 시간을 업데이트
            process.append([name, start, playtime])
            
    answer.append(plans[-1][0])
    
    while process:
        n = process.pop()[0]
        answer.append(n)
    
    return answer