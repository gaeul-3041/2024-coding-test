# 9. 짝지어 제거하기
# 한 번의 순회로 모두 매칭하는 방법?

def solution(s):
    stack = []
    
    for c in s:
        # 바로 앞에 중복 문자가 있으면 stack에서 곧바로 제거
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if stack:
        return 0
    else:
        return 1