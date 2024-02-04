def solution(s):
    p = 0  # 스택의 역할을 할 변수
    
    for i in s:
        if i == '(':
            p += 1
        else:
            # ')'가 하나라도 먼저 나오면 올바를 수 없는 괄호 문자열
            if p == 0:
                return False
            p -= 1
            
    if p == 0:
        return True
    else:
        return False