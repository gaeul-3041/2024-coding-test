# 12. 이진 변환 반복하기
# 1의 개수 셀 방법, 다음 s 설정 방법 생각

def solution(s):
    # 동작 횟수 & 제거한 0의 개수
    cnt = 0
    removed = 0
    
    while s != '1':
        cnt += 1
        s1 = len(s)
        s2 = s.count('1') # 1의 개수를 저장할 변수
        removed += s1 - s2 # 제거한 0의 개수 업데이트
        s = bin(s2)[2:] # '0b...' 형태이므로 첫 2개 문자는 제외
    
    return [cnt, removed]
