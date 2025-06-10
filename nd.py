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

ar=np.array([[5,6]])
con=np.concatenate((arr,ar.T),axis=1)
print(con)

att=np.array([[2,3],[4,5]])
at=np.array([[6,7]])
cont=np.concatenate((att,at.T),axis=1)
cont=np.concatenate((att,at),axis=None)
cont=np.concatenate((att,at),axis=0)
print(cont)

a=np.array([[8,9,10,11]])
b=np.array([[12,13,14,15]])
c=np.hstack((a,b))
print(c)

a = np.random.random((3,2))
print (a)

a = np.random.randn(1000)
print(a.mean(), a.var())

a = np.random.randint(3, 10, size=(3,3))
print (a)
