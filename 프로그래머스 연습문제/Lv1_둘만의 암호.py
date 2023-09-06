def solution(s, skip, index):
    answer = []
    # ord, chr을 써도 되지만 이것도 충분히 편한 방법
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # skip할 문자는 미리 제거
    for c in skip:
        alphabet = alphabet.replace(c, '')
        
    for c in s:
        if c in skip:
            continue
        else:
            idx = alphabet.index(c)
            answer.append(alphabet[(idx + index) % len(alphabet)])

    # 문자가 담긴 리스트를 문자열로 변환하는 방식 채택
    return ''.join(answer)
