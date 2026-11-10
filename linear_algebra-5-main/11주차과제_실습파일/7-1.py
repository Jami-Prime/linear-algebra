import numpy as np

# 실습 7-1: 특성다항식과 고유값 계산
A = np.array([
    [2, 3],
    [3, -6]
], dtype=float)

print("특성다항식 계수:")
print(np.poly(A))

print("고유값:")
print(np.linalg.eigvals(A))
