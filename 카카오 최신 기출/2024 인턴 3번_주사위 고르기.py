from itertools import combinations, product

def solution(dice):    
    n = len(dice)
    scoreBoard = {}  # 모든 경우의 수 저장용(주사위 조합 - 승리 횟수)
    
    for diceA in combinations(range(n), n//2):  # 주사위 중 조합을 이용해 절반 선택
        scoreA, scoreB = [], []
        
        diceB = [i for i in range(n) if i not in diceA]  # A가 고르지 않은 나머지 절반
        
        for p in product(range(6), repeat=n//2):  # 모든 가능한 주사위 면 조합을 구현하는 중복순열
            scoreA.append(sum(dice[i][j] for i, j in zip(diceA, p)))
            scoreB.append(sum(dice[i][j] for i, j in zip(diceB, p)))
        
        scoreB.sort()  # 이진 탐색을 위한 정렬
        
        w = 0  # 이번 diceA로 가능한 승리 횟수의 총합, 무승부는 무시
        
        for score in scoreA:
            left, right = 0, len(scoreB) - 1
            while left <= right:
                mid = (left + right) // 2
                if score <= scoreB[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            w += left
        
        scoreBoard[diceA] = w
    
    answer = max(scoreBoard, key=scoreBoard.get)  # 가장 승리 횟수가 많은 주사위 조합을 선택
    return [i+1 for i in answer]