n = int(input())
dp = [0] * 1001  # 최대 크기의 배열을 미리 할당 / 1001 대신 (n + 1)을 쓰면 n = 1일 때 IndexError
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    
print(dp[n])