# 1. 교점에 별 만들기
# 굳이 교점 구하는 법도 다 알려주는 걸 보면 그냥 시키는 대로 하면 될까?

def solution(line):
    xseries = [] # x좌표만 저장
    yseries = [] # y좌표만 저장

    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            chk = a * d - b * c
            if chk == 0: # 직선의 평행 또는 일치 확인
                continue

            x = b * f - e * d
            y = e * c - a * f
            if x % chk == 0 and y % chk == 0:
                xseries.append(x // chk)
                yseries.append(y // chk)
    
    # 가로 x방향, 세로로 -y방향 배열 생성
    x_max, y_max, x_min, y_min = max(xseries), max(yseries), min(xseries), min(yseries)
    answer = [['.'] * (x_max - x_min + 1) for i in range(y_max - y_min + 1)]
    
    # 배열 인덱스는 0부터 시작하므로 각 좌표에 -min을 더해 보정
    for i in range(len(xseries)):
        nx, ny = xseries[i] - x_min, yseries[i] - y_min
        answer[ny][nx] = '*'
    
    # y축이 반대이므로 뒤집기
    answer.reverse()
    
    # 내부 배열들은 문자열로 join 시킨 후 리스트화
    return list(map(''.join, answer))