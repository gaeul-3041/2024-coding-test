from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 빠른 탐색을 위한 딕셔너리 채택
dict_a = defaultdict(int)

for i in a:
    dict_a[i] += 1

for i in b:
    if i in dict_a:
        print(1)
    else:
        print(0)