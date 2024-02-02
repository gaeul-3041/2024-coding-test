def solution(n, m, section):
    answer = 1
    start = section[0]
    end = section[0] + m
    
    for i in section:
        if start <= i < end:
            continue
        else:
            answer += 1
            start = i  # 구간 밖 첫 블럭이 다음 구간 시작점
            end = start + m
    
    return answer