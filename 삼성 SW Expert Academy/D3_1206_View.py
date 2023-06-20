T = 10

for test_case in range(1, T + 1):
    n = int(input())
    buildings = list(map(int, input().split()))
    answer = 0
    
    for i in range(2, n - 2):
        building = buildings[i]
        around = max(buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2])
        if building > around:
            answer += building - around
    
    print('#{} {}'.format(test_case, answer))  # 이 형태를 기억해두자...
