import numpy as np

u = np.array([1, 2, 4])
v = np.array([2, -3, 5])
w = np.array([4, 2, -3]) # 1*3 벡터 

print("u · v =", np.dot(u, v)) # 내적값을 출력 
print("u · w =", np.dot(u, w))
print("v · w =", np.dot(v, w))
