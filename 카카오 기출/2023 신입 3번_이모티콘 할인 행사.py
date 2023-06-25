from itertools import product  # 모든 경우의 수를 포함할 순열 연산

def solution(users, emoticons):
    discount = [10, 20, 30, 40]
    answer = [0, 0]
    
    # 순열 연산을 통해 모든 할인율의 경우의 수 고려(최대 4^7)
    for sales in product(discount, repeat = len(emoticons)):
        res = [0, 0]
        for user in users:
            tmp = 0  # 해당 유저의 이모티콘 구매 비용 총합
            for i in range(len(emoticons)):
                if user[0] <= sales[i]:  # 할인율 비교
                    tmp += emoticons[i] * (100 - sales[i]) / 100
            if tmp >= user[1]:  # 구매 비용이 기준 이상이면 전환
                res[0] += 1
            else:
                res[1] += tmp
                
        answer = max(answer, res)  # 임티플 가입 인원을 우선, 동일하면 결제비 비교
    
    return answer