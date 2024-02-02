from collections import defaultdict

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

answer = defaultdict(int)
for card in cards:
    answer[card] += 1
    
for num in nums:
    if num in answer:
        print(answer[num], end=' ')
    else:
        print(0, end=' ')