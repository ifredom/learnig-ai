import numpy as np
from sklearn.utils import check_random_state

n = 50
XX = np.arange(n)
print(XX)

rs = check_random_state(0)
print(rs)

YY = rs.randint(-10, 10, size=50)
print(YY)

# axis设置为0维
data = np.stack([XX, YY], axis=0)
print(data)


newList = data[:,1]
print(newList)

newList0 = data[:,0]
print(newList0)