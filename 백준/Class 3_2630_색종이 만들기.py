n = int(input())
white, blue = 0, 0
paper = [list(map(int, input().split())) for _ in range(n)]

# 종이 4분할로 자르는 재귀 함수
def cutter(x, y, k):
    global white, blue
    head = paper[x][y]
    for i in range(x, x + k):
        for j in range(y, y + k):
            if head != paper[i][j]:  # 같은 색 통일이 아니면 4등분
                cutter(x, y, k//2)
                cutter(x, y + k//2, k//2)
                cutter(x + k//2, y, k//2)
                cutter(x + k//2, y + k//2, k//2)
                return
    if head == 0:
        white += 1
    else:
        blue += 1
        
cutter(0, 0, n)
print(white)
print(blue)