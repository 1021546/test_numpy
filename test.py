import numpy as np

my_list = [1, 2, 3, 4, 5]

my_numpy_list = np.array(my_list)
# print(my_numpy_list)  #This line show the result of the array generated

second_list = [[1,2,3], [5,4,1], [3,6,7]]
new_2d_arr = np.array(second_list)
# print(new_2d_arr)  #This line show the result of the array generated

my_list = np.arange(10) #O
# print(my_list)
Rmy_list = np.arange(0,10)
# print(Rmy_list)

my_list = np.arange(0,11,2)
# print(my_list)

my_zeros = np.zeros(7)
# print(my_zeros)

my_ones = np.ones(5)
# print(my_ones)

two_d = np.zeros((3,5))
# print(two_d)

lin_arr = np.linspace(1, 3, 15)
# print(lin_arr)

my_matrx = np.eye(6)    #6 is the number of columns/rows you want
# print(my_matrx)

my_rand = np.random.rand(4)
# print(my_rand)

my_rand = np.random.rand(5, 4)
# print(my_rand)

my_randn = np.random.randn(7)
# print(my_randn)

# print(np.random.randn(3,5))

# print(np.random.randint(20)) #generates a random integer exclusive of 20
# print(np.random.randint(2, 20)) #generates a random integer including 2 but excluding 20
# print(np.random.randint(2, 20, 7)) #generates 7 random integers including 2 but excluding 20

arr = np.random.rand(25)
# print(arr)
# print(arr.reshape(5,5))

arr_2 = np.random.randint(0, 20, 10)
# print(arr_2)
# print(arr_2.max()) #This gives the highest value in the array 
# print(arr_2.min()) #This gives the lowest value in the array

# print(arr_2.argmax()) #This shows the index of the highest value in the array 
# print(arr_2.argmin()) #This shows the index of the lowest value in the array

# print(arr.shape)

my_array = np.arange(0,11)
# print(my_array[8])  #This gives us the value of element at index 8

# print(my_array[2:6]) #This returns everything from index 2 to 6(exclusive)
# print(my_array[:6]) #This returns everything from index 0 to 6(exclusive)
# print(my_array[5:]) #This returns everything from index 5 to the end of the array.

two_d_arr = np.array([[10,20,30], [40,50,60], [70,80,90]])
# print(two_d_arr[1][2]) #The value 60 appears is in row index 1, and column index 2
# print(two_d_arr[0,1])

# print(two_d_arr[:1, :2])           # This returns [[10, 20]]
# print(two_d_arr[:2, 1:])         # This returns ([[20, 30], [50, 60]])
# print(two_d_arr[:2, :2])       #This returns ([[10, 20], [40, 50]])

# print(two_d_arr[0])    #This grabs row 0 of the array ([10, 20, 30])
# print(two_d_arr[:2]) #This grabs everything before row 2 ([[10, 20, 30], [40, 50, 60]])


new_arr = np.arange(5,15)
# print(new_arr > 10) #This returns TRUE where the elements are greater than 10 [False, False, False, False, False, False,  True,  True,  True, True]

bool_arr = new_arr > 10
# print(new_arr[bool_arr])  #This returns elements greater than 10 [11, 12, 13, 14]
# print(new_arr[new_arr>10]) #A shorter way to do what we have just done

# print(new_arr[(new_arr>6) & (new_arr<10)])

my_array[0:3] = 50  #Result is: [50, 50, 50, 3, 4,  5,  6,  7,  8,  9, 10]
# print(my_array)

arr = np.arange(1,11)
# print(arr * arr)             #Multiplies each element by itself 
# print(arr - arr)             #Subtracts each element from itself
# print(arr + arr)             #Adds each element to itself
# print(arr / arr)              #Divides each element by itself
# print(arr + 50)            #This adds 50 to every element in that array

# print(np.sqrt(arr))    #Returns the square root of each element 
# print(np.exp(arr))    #Returns the exponentials of each element
# print(np.sin(arr))    #Returns the sin of each element
# print(np.cos(arr))   #Returns the cosine of each element
# print(np.log(arr))     #Returns the logarithm of each element
# print(np.sum(arr))     #Returns the sum total of elements in the array
# print(np.std(arr))     #Returns the standard deviation of in the array

mat = np.arange(1,26).reshape(5,5)
# print(mat.sum())      #Returns the sum of all the values in mat
# print(mat.sum(axis=0))  #Returns the sum of all the columns in mat
# print(mat.sum(axis=1))  #Returns the sum of all the rows in mat