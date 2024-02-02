n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
answer = 64

for x in range(n-7):
    for y in range(m-7):
        cnt1 = 0
        cnt2 = 0
        # 8*8 체스판이 되는 시작점만 뽑아서 비교
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W':
                        cnt1 += 1
                    if board[i][j] != 'B':
                        cnt2 += 1
                else:
                    if board[i][j] != 'B':
                        cnt1 += 1
                    if board[i][j] != 'W':
                        cnt2 += 1
        answer = min(answer, cnt1, cnt2)

print(answer)