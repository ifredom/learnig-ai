import numpy as np

a = [[1, 2, 3], [4, 5, 6]]

print(a)
b = np.stack(a, axis=0)
print(b)
c = np.stack(a, axis=1)
print(c)


# statck() 数组维度扩充，堆叠
