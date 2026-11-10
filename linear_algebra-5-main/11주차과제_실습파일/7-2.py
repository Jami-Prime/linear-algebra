import numpy as np

# 실습 7-2: 고유값과 고유벡터 계산
A = np.array([
    [3, 2],
    [3, -2]
], dtype=float)

# MATLAB의 [X, lamda] = eig(A)에 대응
eigenvalues, X = np.linalg.eig(A)

# 고유값을 4, -3 순서로 정렬하고 고유벡터 열도 같은 순서로 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

lamda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True)

print("X =")
print(X)

print("lamda =")
print(lamda)
