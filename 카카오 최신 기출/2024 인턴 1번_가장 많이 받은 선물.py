def solution(friends, gifts):
    k = len(friends)
    answer = [0 for i in range(k)]
    giftidx = [0 for i in range(k)]  # 선물 지수
    numbers = {}  # 각 friend에게 번호를 붙여줌
    giftlog = [[0] * k for i in range(k)]  # 선물을 주고 받은 기록을 담는 테이블
    
    for i in range(k):
        numbers[friends[i]] = i
        
    for gift in gifts:
        src, dst = gift.split(' ')
        giftlog[numbers[src]][numbers[dst]] += 1  # 선물 테이블 업데이트
        giftidx[numbers[src]] += 1  # 선물 지수 업데이트 - 준 사람에게 +1
        giftidx[numbers[dst]] -= 1  # 선물 지수 업데이트 - 받은 사람에게 -1
        
    for i in range(k):
        for j in range(i+1, k):
            if giftlog[i][j] > giftlog[j][i]:
                answer[i] += 1
            elif giftlog[i][j] < giftlog[j][i]:
                answer[j] += 1
            else:
                if giftidx[i] > giftidx[j]:
                    answer[i] += 1
                elif giftidx[i] < giftidx[j]:
                    answer[j] += 1
        
    return max(answer)
