# learning numpy library and learned creating arrays
import numpy as np
def creating_array_using_numpy():
    # 1-D array
    a = np.array([1,2,3,])
    print(type(a))

    #2-D array
    b = np.array([[1,2,3],[4,5,6]])
    print(b)

    #3-D array
    c = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
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

def array_indexing_using_numpy():
    #array indexing
    arr = np.array([1,2,3,4,5])
    print(arr[0])  # Access the first element
    print(arr[-1])  # Access the last element
    print(arr[1:4])  # Access elements from index 1 to 3
    print(arr[3] + arr[4])# Access elements at index 3 and 4 and add them

    #accessing 2-D array
    arr2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
    print(arr2d[0, 1])  # Access the element at row 0, column 1
    print(arr2d[1, 3])  # Access the element at row 1, column 3

    #accessing 3-D array
    arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
    print(arr3d)
    print(arr3d[0, 1, 2])# Access the element at depth 0, row 1, column 2

    #negative indexing
    print(arr2d[1, -1])# Access the last element of the second row

#array attribute
def array_attribute():
    a1 = np.arange(10,dtype=int)
    a2 = np.arange(12,dtype=float).reshape(3,4)
    a3 = np.arange(8).reshape(2,2,2)
    print(a1)
    print(a2)
    print(a3)

    # ndim
    print(a1.ndim)  # Number of dimensions
    print(a2.ndim)
    print(a3.ndim)

    # shape
    print(a1.shape)# Number of elements in each dimension
    print(a2.shape)
    print(a3.shape)

    # size
    print(a1.size)# Total number of elements in the array
    print(a2.size)
    print(a3.size)

    # itemsize
    print(a1.itemsize)  # Size of each element in bytes
    print(a2.itemsize)
    print(a3.itemsize)

    # dtype
    print(a1.dtype)  # Data type of the elements
    print(a2.dtype)
    print(a3.dtype)

def changing_datatype_of_numpy_array():
    a1  = np.arange(10,dtype=int)
    print(a1.astype(float))  # Change the data type to float or any datatype you want to change to

changing_datatype_of_numpy_array()

