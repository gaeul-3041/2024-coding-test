# 5. 행렬의 곱셈
# 행렬 곱셈 어떻게 하는지만 알면 쉬운 문제...

def solution(arr1, arr2):
    # arr1은 a * b, arr2는 b * c 크기의 행렬
    a = len(arr1)
    b = len(arr1[0])
    c = len(arr2[0])
    
    # 정답 행렬은 a * c 크기
    answer = [[0] * c for i in range(a)]
    
    for i in range(a):
        for j in range(c):
            for k in range(b):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    
    return answer