from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    dic = defaultdict(int)
    
    for i in range(len(want)):
        dic[want[i]] += number[i]
        
    for i in range(len(discount) - 9):
        dc = defaultdict(int)
        
        for j in range(i, i + 10):
            dc[discount[j]] += 1
        
        if dc == dic:
            answer += 1
    
    return answer