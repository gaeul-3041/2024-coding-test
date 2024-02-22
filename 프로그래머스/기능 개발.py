import math

def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    finish = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]  # 끝나는 날짜를 정수로 계산
    
    cnt = 0
    maxDate = finish[0]
    
    for i in range(n):
        # 현재 지정된 작업 및 이보다 빨리 끝나는 작업들을 묶어서 배포, 늦게 끝나는 작업이 나오면 새롭게 배포
        if finish[i] <= maxDate:
            cnt += 1
        else:
            maxDate = finish[i]
            answer.append(cnt)
            cnt = 1
    
    answer.append(cnt)
    return answer