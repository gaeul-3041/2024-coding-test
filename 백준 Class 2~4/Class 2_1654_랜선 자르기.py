k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

start, end = 1, max(lines)

# 이분 탐색 - 구현 방법 기억해두기
while start <= end:
    mid = (start + end) // 2
    cnt = 0  # 만들어진 랜선의 개수
    for line in lines:
        cnt += line // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)