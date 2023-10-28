# 17. 하노이의 탑
# start, via, end를 이용한 위치 관리

answer = []

def hanoi(s, v, e, n):
    if n == 1:
        answer.append([s, e])
        return
    # 직전 단계 원판은 목표가 아닌 중간 기둥으로 먼저 이동
    hanoi(s, e, v, n - 1)
    answer.append([s, e])
    hanoi(v, s, e, n - 1)

def solution(n):
    hanoi(1, 2, 3, n)
    return answer
