def solution(s):
    answer = 0
    k = len(s)
    
    for i in range(k):
        stack = []
        chk = 1  # 불가능한 경우를 판별하는 변수
        for j in range(k):
            c = s[(i+j) % k]  # 시작점을 i로 두고 문자열 회전
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    chk = 0
                    break
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    chk = 0
                    break
        
        # break 없이 모든 과정이 끝나고 스택이 비어있으면 1을 더함
        if not stack:
            answer += chk
    
    return answer