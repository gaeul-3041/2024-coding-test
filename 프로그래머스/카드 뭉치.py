from collections import deque

def solution(cards1, cards2, goal):
    c1 = deque(cards1)
    c2 = deque(cards2)
    
    for word in goal:
        if c1 and word == c1[0]:
            c1.popleft()
        elif c2 and word == c2[0]:
            c2.popleft()
        else:
            return 'No'
    
    return 'Yes'