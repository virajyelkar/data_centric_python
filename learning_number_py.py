"""
    # Learning NumPy Library: Arrays, Indexing, Attributes, Datatypes & Operations

    This is an interactive, menu-driven Python script tracking my progress with the NumPy library.
    It covers array creation, indexing mechanics, memory attributes, and element operations.

    HOW TO RUN:
    Simply run the script in your terminal. You do not need to uncomment anything!
    An interactive menu will ask you to enter a choice from 1 to 6 to test different blocks.
    
    i will keep adding more examples to this file as I learn more about the NumPy library.
"""

import numpy as np
def creating_array_using_numpy():
    # 1-D array
    print("\n============1-D array =============")
    a = np.array([1,2,3,])
    print(type(a))

    #2-D array
    print("\n===============2-D array ============")
    b = np.array([[1,2,3],[4,5,6]])
    print(b)

    #3-D array
    print("\n================3-D array=============")
    c = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
    print(c)

    #4-D array
    print("\n===================4-D array===============")
    A1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    print(A1)

    #dtype
    print("\n============check datatype of array=============")
    D = np.array([1,2,3],dtype=float)
    print(D)

    #np.arange
    print("\n====================arange function==================")
    rang = np.arange(1,11)
    print(rang)

    #np.arange with reshape
    print("\n=========arange with reshape=============")
    rang1 = np.arange(1,11).reshape(5,2)
    print(rang1)

    #np.ones and np.zeros
    print("\n=======np.once and np.zeros========")
    one = np.ones((3,4))
    print(one)
    zero = np.zeros((3,3))
    print(zero)

    #np.random
    print("\n=========np.random============")
    x = np.random.random((3,3))
    print(x)

    #np.linspace
    print("\n===========linespace==============")
    y = np.linspace(-5,5,3)
    print(y)

    #np.identity
    print("\n===========np.identity=============")
    z = np.identity(4)
    print(z)

def array_indexing_using_numpy():
    #array indexing
    print("\n=======array indexing=======")
    arr = np.array([1,2,3,4,5])
    print(arr[0])  # Access the first element
    print(arr[-1])  # Access the last element
    print(arr[1:4])  # Access elements from index 1 to 3
    print(arr[3] + arr[4])# Access elements at index 3 and 4 and add them

    #accessing 2-D array
    print("\n=======accessing 2-D array==========")
    arr2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
    print(arr2d[0, 1])  # Access the element at row 0, column 1
    print(arr2d[1, 3])  # Access the element at row 1, column 3

    #accessing 3-D array
    print("\n========accessing 3-D array==========")
    arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
    print(arr3d)
    print(arr3d[0, 1, 2])# Access the element at depth 0, row 1, column 2

    #negative indexing
    print("\n========negative indexing===========")
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
    print("\n========number of dimensions using 'ndim'===========")
    print(a1.ndim)  # Number of dimensions
    print(a2.ndim)
    print(a3.ndim)

    # shape
    print("\n=====number of elements in each dimension using 'shape'=======")
    print(a1.shape)# Number of elements in each dimension
    print(a2.shape)
    print(a3.shape)

    # size
    print("\n ==========total number of elements in the array using 'size'=============")
    print(a1.size)# Total number of elements in the array
    print(a2.size)
    print(a3.size)

    # itemsize
    print("\n========size of each element in bytes using 'itemsize'=============")
    print(a1.itemsize)  # Size of each element in bytes
    print(a2.itemsize)
    print(a3.itemsize)

    # dtype
    print("\n========data type of the elements using 'dtype'==================")
    print(a1.dtype)  # Data type of the elements
    print(a2.dtype)
    print(a3.dtype)

def changing_datatype_of_numpy_array():
    print("\n=====change the datatype==========")
    a1  = np.arange(10,dtype=int)
    print(a1.astype(float))  # Change the data type to float or any datatype you want to change to

#array operations
def array_operations():
    a1 = np.arange(12).reshape(3,4)
    a2 = np.arange(12,24).reshape(3,4)

    #scalar operation
    print("\n=========scholar operation========")
    print(a1 * 2)# Multiply each element of a1 by 2

    #arithmetic operations
    print("\n=======arithmetic operation with array and number===========")
    print(a1 + 2)
    print(a1 - 2)
    print(a1 * 2)
    print(a1 / 2)
    print(a1 % 2)
    print(a1 ** 2)
    print(a1 // 2)

    #arithmetic operations between two arrays
    print("\n========arithmetic operation between two arrays=========")
    print(a1 + a2)
    print(a1 - a2)
    print(a1 * a2)
    print(a1 / a2)
    
    #relational operations
    print("\n===========relation operation with array and numbers=============")
    print(a2 > 15)
    print(a2 < 15)
    print(a2 >= 15)
    print(a2 <= 15)
    print(a2 == 15)
    print(a2 != 15)

    #relational operations between two arrays
    print("\n========relational operations between two arrays==========")
    print(a1 > a2)
    print(a1 < a2)
    print(a1 >= a2)
    print(a1 <= a2)
    print(a1 == a2)
    print(a1 != a2)

def main_menu():
    while True:
        print("\n==========numpy============")
        print("1. run array creation example ")
        print("2. run array indexing example")
        print("3. run array attributes check ")
        print("4. run changing datatype of array example")
        print("5. run array operations ")
        print("6. exit menu")

        #taking input from user
        choice = int(input("\nEnter your choice between(1-6) =>  "))

        if choice == 1:
            creating_array_using_numpy()
        elif choice == 2:
            array_indexing_using_numpy()
        elif choice == 3:
            array_attribute()
        elif choice == 4:
            changing_datatype_of_numpy_array()
        elif choice == 5:
            array_operations()
        elif choice == 6:
            print("\nexiting library session workspace. keep building, bro! ")
            break #stops the loop and closes my numpy menu
        else:
            print("\n[invalid choice] please type a number between 1 to 6.")

#this line starts the menu when you run my code
main_menu()
