import numpy as np

a = np.array([(1,2,3),(3,4,5)])

b = np.array([(1,2,3),(3,4,5)])

print(a+b)

print(a-b)

print(a*b)

print(a/b)

print(np.vstack((a,b)))

print(np.hstack((a,b)))

print(a.ravel())


