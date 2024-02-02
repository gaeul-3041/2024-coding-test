# 26. H-index
# 오름차순 기준 현재 논문보다 인용 수가 많은 논문이 몇 개인가?

def solution(citations):
    answer = 0
    citations.sort() # 오름차순
    
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    
    return answer