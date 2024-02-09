def solution(n, k, cmd):
    answer = ['O' for i in range(n)]
    trash = []
    
    k += 1  # up[-1] 등의 형태로 연산 실수가 발생하지 않도록 첫 인덱스를 1로 설정
    up = [i-1 for i in range(n+2)]  # i번째 행의 위 / -1, 0을 추가
    down = [i+1 for i in range(n+1)]  # i번째 행의 아래 / n+1을 추가
    
    for c in cmd:
        a = c[0]
        if a == 'U':
            b = int(c[2:])
            for i in range(b):
                k = up[k]
        elif a == 'D':
            b = int(c[2:])
            for i in range(b):
                k = down[k]
        elif a == 'C':
            trash.append(k)
            up[down[k]] = up[k]  # down의 up은 삭제된 행의 up으로 변경
            down[up[k]] = down[k]  # up의 down은 삭제된 행의 down으로 변경
            if n < down[k]:
                k = up[k]
            else:
                k = down[k]
        elif a == 'Z':
            t = trash.pop()
            down[up[t]] = t  # up의 down은 복구된 행의 down으로 변경
            up[down[t]] = t  # down의 up은 복구된 행의 up으로 변경
            
    for i in trash:
        answer[i-1] = 'X'
    
    return ''.join(answer)