n = int(input())
answer = 0

# 5가 2보다 적게 나오므로 5의 개수만 체크
for i in range(1, n+1):
    if i % 5 == 0:
        answer += 1
    if i % 25 == 0:
        answer += 1
    if i % 125 == 0:
        answer += 1
        
print(answer)