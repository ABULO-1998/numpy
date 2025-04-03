
import numpy as np

# a = np.array([1,2,3])
# print(a.shape)
# print(a.dtype)
# print(a.ndim)
# print(a.size)
# print(a.itemsize)
# print(a[0])

# a[0]=10
# print(a)

# b=a*np.array([2,0,2])
# print(b)
# l=[1,2,3]
# a=np.array([1,2,3])

# l.append(4)
# l=l+[4]
# a=a+np.array([4,4,4])
# a=np.sqrt(a)
# a=np.log(a)
# print(l)
# print(a)

# l1=[1,2,3]
# l2=[4,5,6]
# a=np.array([1,2,3])

# dot=0
# for i in range(len(l1)):
#     dot += l1[i]*l2[i]
# print(dot)

# a1=np.array(l1)
# a2=np.array(l2)
# dot= np.dot(a1,a2)
# print(dot)

# sum1=a1*a2
# dot=np.sum(sum1)
# print(dot)

# dot=a1@a2
# print(dot)

# a=np.arange(1,7)
# print(a)
# print(a.shape)

# b=a.reshape(2,3)
# print(b)

from timeit import default_timer as timer

a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a)
B = list(b)

T =1000

def dot1():
    dot = 0
    for i in range(len(A)):
        dot +=A[i]*B[i]
    return(dot)

def dot2():
    return np.dot(a,b)

start = timer()
for t in range(T):
    dot1()
end = timer()
t1=end-start

start = timer()
for t in range(T):
    dot2()
end = timer()
t2=end-start

print('list calculation',t1)
print('np.dot',t2)
print('ratio',t1/t2)

