# 10. 문자열 압축
# 2020 카카오 기출
# 제일 앞에서부터 정해진 만큼만 절단 가능

def solution(s):
    answer = len(s)
    half = len(s) // 2
    
    # 한 번에 자를 단위: 1개부터 half개까지
    for i in range(1, half + 1):
        head = '' # 첫 문자열 조각
        cnt = 1
        res = '' # 각 동작별 완성된 문자열을 저장할 변수
        for j in range(0, len(s) + 1, i):
            nxt = s[j:j+i] # 다음 문자열 조각
            # 중복이 확인되면 카운트 증가
            if nxt == head:
                cnt += 1
            else:
                res += nxt
                # 같은 문자열 반복이 앞에 있었다면 그 숫자를 문자열로 바꿔 추가 (e.g. 2 -> '2')
                # 이렇게 되면 res에는 abab -> ab2 같은 형태로 저장되지만 문제 풀이엔 상관없음
                if cnt >= 2:
                    res += str(cnt)
                cnt = 1 # 카운트 초기화
                head = nxt
        answer = min(len(res), answer) # 완성된 문자열 길이와 원래 최솟값 비교
    
    return answer