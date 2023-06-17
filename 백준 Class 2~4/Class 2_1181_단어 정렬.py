n = int(input())
words = [input() for _ in range(n)]
words = list(set(words))

# lambda 함수를 이용해 길이 - 사전 순 정렬
words.sort(key=lambda x: (len(x), x))

for i in words:
    print(i)