import math
mines = {'diamond': 2, 'iron': 1, 'stone': 0}
answer = 1250  # 이론상 가능한 정답의 최댓값

# 다이아, 철, 돌 곡괭이로 완전탐색 DFS를 수행할 함수
def dfs(dia, iron, stone, minerals, nxt, res):
    global answer
    
    if nxt >= len(minerals) or dia + iron + stone == 0:  # 곡괭이를 다 썼거나 채광이 끝난 경우
        answer = min(answer, res)
        return
    
    cnt = min(5, len(minerals) - nxt)  # 다음 채광할 분량
    cnt_score = [[0] * cnt for _ in range(3)]  # 채광 결과를 담을 배열(줄마다 다이아 / 철 / 돌 곡괭이를 사용한 결과)
    
    for i in range(3):
        k = 2 - i  # 이번에 사용할 도구의 강도(다이아 2, 철 1, 돌 0)
        for j in range(nxt, nxt + cnt):  # 채광할 범위 지정
            # 둘의 강도 차이를 5의 제곱 지수로 활용, 1 미만일 경우 1로 올림
            cnt_score[i][j - nxt] = math.ceil(5 ** (mines[minerals[j]] - k))
    
    # 남아있는 곡괭이로 다음 DFS 함수 수행
    if dia > 0:
        dfs(dia - 1, iron, stone, minerals, nxt + 5, res + sum(cnt_score[0]))
    if iron > 0:
        dfs(dia, iron - 1, stone, minerals, nxt + 5, res + sum(cnt_score[1]))
    if stone > 0:
        dfs(dia, iron, stone - 1, minerals, nxt + 5, res + sum(cnt_score[2]))

def solution(picks, minerals):
    dfs(picks[0], picks[1], picks[2], minerals, 0, 0)
    
    return answer