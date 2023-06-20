T = 10

for test_case in range(1, T + 1):
    n = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()
    
    for i in range(n):
        boxes[0] += 1
        boxes[-1] -= 1
        boxes.sort()
        
    print('#{} {}'.format(test_case, boxes[-1] - boxes[0]))