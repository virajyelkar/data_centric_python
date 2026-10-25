"""
    # Learning NumPy Library: Master Workspace Engine

    This is an interactive, menu-driven Python application tracking my progress with the NumPy library.
    It serves as the foundational data-centric computing pipeline for my Master's research under Dr. Bhavin Patel.

    FEATURES COVERED:
    1. Array Creation & Manipulation (1D to 4D matrices, linspace, identity vectors)
    2. Matrix Indexing & Slicing (Positive, negative, and multi-dimensional coordinate access)
    3. Memory Attributes Inspection (ndim, shape, size, itemsize, dtype)
    4. Dynamic Memory Type Casting (.astype transformations)
    5. Vector & Array Operations (Scalar math, element-wise arithmetic, relational matrices)
    6. Multi-dimensional Traversal (Nested loop array iteration logs)
    7. Matrix Reshaping Blocks (Joining via concatenate, array splitting, index searching via where)
    8. Linear Algebra Engines (Vector scaling, 4-way dot products, cross products, matrix-vector multiplication)

    HOW TO RUN:
    Execute the script directly in your terminal command prompt. 
    An interactive console menu wrapper will automatically launch to let you choose exactly which block to run.
"""

import numpy as np
def creating_array_using_numpy():
    def array_1D_creation():
        # 1-D array
        print("\n============1-D array =============")
        a = np.array([1,2,3,])
        print(a)

    def array_2D_creation():
        #2-D array
        print("\n===============2-D array ============")
        b = np.array([[1,2,3],[4,5,6]])
        print(b)

    def array_3D_creation():
        #3-D array
        print("\n================3-D array=============")
        c = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
        print(c)

    def array_4D_creation():
        #4-D array
        print("\n===================4-D array===============")
        A1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        print(A1)

    def to_specify_datatype():
        #dtype
        print("\n============check datatype of array=============")
        D = np.array([1,2,3],dtype=float)#to specify the datatype of the array, you can use the dtype parameter while creating the array
        print(D)

    def creating_array_using_arange():
        #np.arange
        print("\n====================arange function==================")
        rang = np.arange(1,11)#to create an array with a range of numbers, you can use the np.arange() function. It takes three parameters: start, stop, and step. The start parameter is the first number in the range, the stop parameter is the last number in the range (exclusive), and the step parameter is the difference between each number in the range.
        print(rang)

    def arange_with_reshape():
        #np.arange with reshape
        print("\n=========arange with reshape=============")
        rang1 = np.arange(1,11).reshape(5,2) #we can also use the reshape() function to change the shape of the array.
        print(rang1)

    def ones_and_zeros_func():
        #np.ones and np.zeros
        print("\n=======np.once and np.zeros========")
        one = np.ones((3,4))#np.ones() function creates an array filled with ones.
        print(one)
        zero = np.zeros((3,3))#np.zeros() function creates an array filled with zeros.
        print(zero)

    def random():
        #np.random
        print("\n=========np.random============")
        x = np.random.random((3,3)) #np.random.random() function creates an array filled with random numbers between 0 and 1. The parameter is the shape of the array.
        print(x)

    def creating_array_with_linspace():
        #np.linspace
        print("\n===========linespace==============")
        y = np.linspace(-5,5,3)#np.linspace() function creates an array with a specified number of evenly spaced values between two endpoints.
        print(y)

    def creating_array_with_identity():
        #np.identity
        print("\n===========np.identity=============")
        z = np.identity(4) #np.identity() function creates a square identity matrix of a specified size.
        print(z)

    def main_menu_of_creating_array():
        while True:
            print("\n============main menu of creating array==============")
            print("1. create 1-D array  ")
            print("2. create 2-D array ")
            print("3. create 3-D array  ")
            print("4. create 4-D array  ")
            print("5. run dtype function ")
            print("6. run creating array using arange ")
            print("7. run crearing array using arange wiht reshape ")
            print("8. run ones and zeros func")
            print("9. run random function ")
            print("10. run creating array with linspace")
            print("11. run creating array using identity function")
            print("12. exit the main menu of creating array ")

            choice = int(input("enter your choice between(1-12)=> "))

            if choice == 1:
                array_1D_creation()
            elif choice == 2:
                array_2D_creation()
            elif choice == 3:
                array_3D_creation()
            elif choice == 4:
                array_4D_creation()
            elif choice == 5:
                to_specify_datatype()
            elif choice == 6:
                creating_array_using_arange()
            elif choice == 7:
                arange_with_reshape()
            elif choice == 8:
                ones_and_zeros_func()
            elif choice == 9:
                random()
            elif choice == 10:
                creating_array_with_linspace()
            elif choice == 11:
                creating_array_with_identity()
            elif choice == 12:
                print("\nexiting the menu ")
                break
            else:
                print("\n[invalid choice] please enter number between 1-12")
    main_menu_of_creating_array()

def array_indexing_using_numpy():
    def array_indexing():
        #array indexing
        print("\n=======array indexing=======")
        arr = np.array([1,2,3,4,5])
        print(arr)
        print(arr[0])  # Access the first element
        print(arr[-1])  # Access the last element
        print(arr[1:4])  # Access elements from index 1 to 3
        print(arr[3] + arr[4])# Access elements at index 3 and 4 and add them

    def accessing_2D_array():
        #accessing 2-D array
        print("\n=======accessing 2-D array==========")
        arr2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
        print(arr2d[0, 1])  # Access the element at row 0, column 1
        print(arr2d[1, 3])  # Access the element at row 1, column 3

    def accessing_3D_array():
        #accessing 3-D array
        print("\n========accessing 3-D array==========")
        arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
        print(arr3d)
        print(arr3d[0, 1, 2])# Access the element at depth 0, row 1, column 2

    def negative_indexing():
        #negative indexing
        arr2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
        print("\n========negative indexing===========")
        print(arr2d)
        print(arr2d[1, -1])# Access the last element of the second row

    def main_menu_of_array_indexing():
        while True:
            print("\n=======menu of array indexing using numpy=======")
            print("1. run array indexing ")
            print("2. run accessing 2-D array ")
            print("3. run accessing 3-D array ")
            print("4. run negative indexing ")
            print("5. exit the main menu of array indexing ")

            choice = int(input("Enter your choice between(1-5)=> "))

            if choice == 1:
                array_indexing()
            elif choice == 2:
                accessing_2D_array()
            elif choice == 3:
                accessing_3D_array()
            elif choice == 4:
                negative_indexing()
            elif choice == 5:
                print("exited the main menu of array indexing ")
                break
            else:
                print("\n[invalid choice] please enter your choice between 1-5 ")
    main_menu_of_array_indexing()
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
    a1 = np.arange(12).reshape(3,4) #this will create a 3x4 array with values from 0 to 11
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

# numpy array iteration example
def array_iteration_example():
    print("============array_iteration===========")
    arr = np.array([1,2,3,4,5])
    for i in arr:
        print(i)

    #iterating 2-D array
    arr2 = np.arange(12).reshape(2,6) #this will create a 2-D array with shape (2,6)
    print("\n========2-D Array Iteration==========")
    for i in arr2:# iterate over each row of the 2-D array
        print(i)

    #iterating on each element of 2-D array
    print("\n========Iterating on each element of 2-D array==========")
    for i in arr2:# iterate over each row of the 2-D array
        for j in i: # iterate over each element of the row
            print(j)

    #iterating 3-D array
    print("\n========3-D Array Iteration==========")
    arr3 = np.arange(24).reshape(2,3,4) #this will create a 3-D array with shape (2,3,4)
    for i in arr3:
        print(i)
    #iterate down the scalar elements of the 3-D array
    print("\n========Iterating on each element of 3-D array==========")
    for i in arr3:# iterate over each 2-D array of the 3-D array
        for j in i: # iterate over each row of the 2-D array
            for k in j: # iterate over each element of the row
                print(k)

#numpy array joining example
def numpy_array_joining_example():
    print("\n========numpy array joining example==========")
    a1 = np.array([[1,2,3],[4,5,6]])
    a2 = np.array([[7,8,9],[10,11,12]])

    #joining two arrays along axis 0
    print("\n========joining two arrays along axis 0==========")
    print(np.concatenate((a1,a2),axis=0)) #this will join the two arrays along the first axis (rows)

    #joining two arrays along axis 1
    print("\n========joining two arrays along axis 1==========")
    print(np.concatenate((a1,a2),axis=1)) #this will join the two arrays along the second axis (columns)

#numpy array splitting example
def array_splitting_example():
    arr = np.array([1,2,3,4,5,6,7,8,9,10])
    #splitting an array into 2 equal parts
    print("\n========splitting an array into 2 equal parts==========")
    print(np.array_split(arr, 2)) #this will split the array into 2 equal parts

    #accessing the first part of the split array
    print("\n========accessing the first part of the split array==========")
    print(np.array_split(arr, 2)[0]) #this will access the first part of the split array
    print(np.array_split(arr, 2)[1])

    #splitting 2-D array into 2 equal parts
    arr2d = np.array([[1,2],[3,4],[5,6],[7,8]])
    print("\n========splitting 2-D array into 2 equal parts==========")
    newarr = np.array_split(arr2d, 2) #this will split the 2-D array into 2 equal parts
    print(newarr)

    #splitting 2-D array into 2-d array along columns
    print("\n========splitting 2-D array into 3 equal parts==========")
    print(np.array_split(arr2d, 3, axis=1)) #this will split the 2-D array into 3 equal parts along columns

#array searching example
def array_searching_example():
    print("\n========array searching example==========")
    a1 = np.array([1,2,3,4,5,6,7,8,9,10])
    x = np.where(a1 == 5) #where function is you to search
    print(x)

    #search sorted array
    print("\n========search sorted array==========")
    y = np.searchsorted(a1, 5) #searchsorted function is used to find the index where the value should be inserted to maintain the order of the array
    print(y)

    #search multiple values in an array
    print("\n========search multiple values in an array==========")
    z = np.searchsorted(a1, [3, 7]) #this find multiple values in array
    print(z)

    """
        vector maths and matrix operations
    """
def vector_matrix_operations():
    #vector scaling
    print("\n========vector scaling==========")
    v1 = np.array([1, 2, 3])
    print(v1 * 5) # Scale the vector by multiplying each element by 5

    #element-wise vector multiplication
    v2 = np.array([4, 5, 6])
    print("\n========element-wise vector multiplication==========")
    print(v1 * v2) # Element-wise multiplication of two vectors | result: [4, 10, 18]

    #dot product of two vectors
    dot_1 = np.dot(v1, v2) # Dot product of two vectors | result: 32
    print("\n========dot product of two vectors==========")
    print(dot_1)

    dot_2 = v1 @ v2 # Dot product using the @ operator | result: 32
    print("\n========dot product using @ operator==========")
    print(dot_2)

    dot_3 = np.sum(v1 * v2) # Dot product using element-wise multiplication and sum | result: 32
    print("\n========dot product using element-wise multiplication and sum==========")
    print(dot_3)

    dot_4 = v1.dot(v2) # Dot product using the dot method of the array | result: 32
    print("\n========dot product using dot method of the array==========")
    print(dot_4)

    #cross product(3D vectors only)
    v3 = np.array([1, 2, 3])
    v4 = np.array([4, 5, 6])
    cross_product = np.cross(v3, v4) # Cross product of two 3 D vectors | result: [-3, 6, -3]
    print("\n========cross product of two 3D vectors==========")
    print(cross_product)

    #matrix-vector multiplication
    print("\n========matrix-vector multiplication==========")
    matrix = np.arange(1,5).reshape(2,2) # Create a 2x2 matrix | result: [[1, 2], [3, 4]]
    vector = np.array([5, 6]) # Create a vector | result: [5, 6]
    result = matrix @ vector # Matrix-vector multiplication | result: [17, 39]
    #calculated as follows:
    # [1*5 + 2*6, 3*5 + 4*6] = [17, 39]
    print(result)

def main_menu():
    while True: #this loop will keep running until the user chooses to exit
        print("\n==========numpy============")
        print("1. run array creation example ")
        print("2. run array indexing example")
        print("3. run array attributes check ")
        print("4. run changing datatype of array example")
        print("5. run array operations ")
        print("6. run array iteration example")
        print("7. run numpy array joining example")
        print("8. run numpy array splitting example")
        print("9. run numpy array searching example ")
        print("10. run vector and matrix operations example")
        print("11. exit menu")

        #taking input from user
        choice = int(input("\nEnter your choice between(1-11) =>  "))

        #calling the functions based on user choice
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
            array_iteration_example()
        elif choice == 7:
            numpy_array_joining_example()
        elif choice == 8:
            array_splitting_example()
        elif choice == 9:
            array_searching_example()
        elif choice == 10:
            vector_matrix_operations()
        elif choice == 11:
            print("\nexiting library session workspace. keep building, bro! ")
            break #stops the loop and closes my numpy menu
        else:
            print("\n[invalid choice] please type a number between 1 to 11.")

#this line starts the menu when you run my code
main_menu()

"""
 this is the end of my numpy library learning code. I will keep adding more features to this code as I learn more about numpy and its applications in data science and machine learning.
"""