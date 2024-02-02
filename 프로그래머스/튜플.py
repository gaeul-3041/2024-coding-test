# 8. 튜플
# 숫자만 골라내서 빈도수로 순서 정하기

from collections import defaultdict

def solution(s):
    count = defaultdict(int) # 등장 횟수를 셀 딕셔너리
    tup = s[2:-2].split('},{') # },{ 기준으로 나누면 각 원소가 깔끔하게 분리됨
    
    for t in tup:
        nums = t.split(',') # 각 원소를 다시 , 단위로 분리
        for num in nums:
            n = int(num) # 숫자만 추출
            count[n] += 1
    
    # value 기준으로 내림차순 정렬
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    answer = []
    for c in count:
        answer.append(c[0])
    
    return answer