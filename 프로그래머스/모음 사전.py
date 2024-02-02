# 18. 모음사전
# 5글자니까 사전을 직접 만드는 게 제일 빠를듯?

alpha = ['A', 'E', 'I', 'O', 'U']

def makeDic(dic, s, length):
    # 6글자 이상은 미포함
    if length > 5:
        return
    # ''을 제외한 모든 만들어진 문자열을 추가
    if s != '':
        dic.append(s)
    for nxt in alpha:
        makeDic(dic, s + nxt, length + 1)

def solution(word):
    dic = []
    makeDic(dic, '', 0)
    for i in range(len(dic)):
        if dic[i] == word:
            return i + 1
