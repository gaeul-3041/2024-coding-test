def solution(nums):
    # 폰켓몬의 종류만 추출
    phone = len(set(nums))

    # 만약 폰켓몬이 n/2가지 이상이면 그것들만 하나씩 뽑는 게 최선
    if phone < len(nums) // 2:
        return phone
    # 가짓수가 부족하면 가짓수보다 더 나올 수 없음
    else:
        return len(nums) // 2
