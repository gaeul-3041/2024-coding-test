# 22. 소수 찾기
# 만들 수 있는 모든 경우의 수 -> 소수 판별

from itertools import permutations

def isPrime(x):
    # 0 또는 1은 즉시 False 반환
    if x == 0 or x == 1:
        return False
    
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    n = []
    
    # 순열을 이용해 모든 경우의 수 생성
    for i in range(1, len(numbers) + 1):
        n.append(list(permutations(numbers, i)))
    
    # permutations 함수는 튜플을 반환
    # 따라서 튜플을 문자열로 먼저 변환 후 별도의 문자열에 저장해야 제대로 사용 가능
    coms = [int(''.join(x)) for i in n for x in i]
    
    for i in coms:
        if isPrime(i):
            answer.append(i)
            
    answer = set(answer)
    return len(answer)