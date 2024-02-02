n, r, c = map(int, input().split())
answer = 0

def Z(n, r, c):
    global answer
    if n == 0:
        return
    if r < 2**(n-1):
        if c < 2**(n-1):
            Z(n-1, r, c)
        else:
            answer += 2**(2*n-2)
            Z(n-1, r, c-2**(n-1))
    else:
        if c < 2**(n-1):
            answer += 2**(2*n-2)*2
            Z(n-1, r-2**(n-1), c)
        else:
            answer += 2**(2*n-2)*3
            Z(n-1, r-2**(n-1), c-2**(n-1))
            
Z(n, r, c)
print(answer)