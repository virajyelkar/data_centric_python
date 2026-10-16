# learning numpy library and learned creating arrays
import numpy as np
# 1-D array
a = np.array([1,2,3,])
print(type(a))

#2-D array
b = np.array([[1,2,3],[4,5,6]])
print(b)

#3-D array
c = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c)

#4-D array
A1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(A1)


#dtype
D = np.array([1,2,3],dtype=float)
print(D)

#np.arange
rang = np.arange(1,11)
print(rang)

#np.arange with reshape
rang1 = np.arange(1,11).reshape(5,2)
print(rang1)

#np.ones and np.zeros
one = np.ones((3,4))
print(one)
zero = np.zeros((3,3))
print(zero)

#np.random
x = np.random.random((3,3))
print(x)

#np.linspace
y = np.linspace(-5,5,3)
print(y)

#np.identity
z = np.identity(4)
print(z)

