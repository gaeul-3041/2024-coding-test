from collections import defaultdict

def solution(keymap, targets):
    answer = []
    alphas = defaultdict(int)
    
    for key in keymap:
        for i in range(len(key)):
            # dict에 처음 넣는 문자면 i + 1부터 시작
            if key[i] not in alphas:
                alphas[key[i]] = i + 1
            # 이미 봤던 문자라면 최소 횟수 업데이트
            else:
                alphas[key[i]] = min(alphas[key[i]], i + 1)
    
    for i in range(len(targets)):
        target = targets[i]
        tmp = 0
        for t in target:
            if t not in alphas:
                tmp = -1
                break
            else:
                tmp += alphas[t]
        answer.append(tmp)
        
    print(alphas)
        
    return answer