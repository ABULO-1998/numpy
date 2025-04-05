import numpy as np


arr=np.array([[1,2],[3,4]])
print(arr)
print(arr.shape)
print(arr[1])
print(arr[0][0])
print(arr[1][-1])
print(arr[0,0])
print(arr[:,0])
print(arr[0,:])
print(arr.T)
print (np.linalg.inv(arr))
print(np.linalg.det(arr))
print(np.diag(arr))

c=np.diag(arr)
print(np.diag(c))