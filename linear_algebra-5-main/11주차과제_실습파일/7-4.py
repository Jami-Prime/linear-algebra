import numpy as np

# 실습 7-4: 삼각행렬의 고유값 계산
A = np.array([
    [0, 0, 0],
    [0, 2, 5],
    [0, 0, -1]
], dtype=float)

B = np.array([
    [4, 0, 0],
    [0, 0, 0],
    [1, 0, -3]
], dtype=float)

print("(1) 행렬 A의 고유값:")
print(np.linalg.eigvals(A))

print("(2) 행렬 B의 고유값:")
print(np.linalg.eigvals(B))
