n = int(input())
score = list(map(int, input().split()))

max_score = max(score)
sum_score = sum(score)
print(sum_score / max_score * (100 / n))