n = int(input())
cnt = 0
num = 666  # 666부터 시작

while True:
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
    num += 1