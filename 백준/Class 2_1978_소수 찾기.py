n = int(input())
nums = list(map(int, input().split()))
answer = 0

for num in nums:
    flag = True
    if num == 1:
        flag = False
    elif num == 2:
        flag = True
    else:
        for j in range(2, num):
            if num % j == 0:
                flag = False
                break
    if flag:
        answer += 1
        
print(answer)