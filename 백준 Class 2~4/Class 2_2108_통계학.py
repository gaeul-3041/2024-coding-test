from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]

print(round(sum(nums)/n))  # 평균값(반올림)

nums.sort()
print(nums[n//2])  # 중앙값

cnt = Counter(nums).most_common()
# 최빈값이 2개 이상의 경우
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
# 최빈값이 1개인 경우
else:
    print(cnt[0][0])
    
print(nums[-1] - nums[0])  # 최댓값 - 최솟값