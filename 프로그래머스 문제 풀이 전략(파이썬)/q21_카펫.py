# 21. 카펫
# 가능한 길이들을 하나씩 대보며 직접 결론 도출

def solution(brown, yellow):
    # 전체 넓이 total 정의
    total = brown + yellow
    # i는 큰 사각형의 세로 길이고, 최솟값 3부터 시작
    for i in range(3, int(total ** 0.5) + 1):
        # 불가능한 경우는 스킵
        if total % i != 0:
            continue
        # j는 큰 사각형의 가로 길이
        j = total // i
        if (i - 2) * (j - 2) == yellow:
            return [j, i]
