# def func1():
#  # Start of the try block where code that may cause an exception is placed
#     try:
#  # A list of integers
#         l = [1, 5, 6, 7]

#  # Take input from the user, converting it to an integer
#         i = int(input("Enter the index: "))

#  # Try to print the element at the index provided by the user
#         print(l[i])

#  # If everything goes well, return 1 to indicate success
#         return 1

#  # Catch any exception that occurs in the try block
#     except:
#  # If an exception occurs, print an error message
#         print("Some error occurred")

#  # Return 0 to indicate failure
#         return 0

#  # The finally block will always be executed, regardless of what happens in the try-except block
#     finally:
#  # Print a message indicating that this block is always executed
#         print("I am always executed")

#  # The code here would never be reached due to the return statements above
#  # print("I am always executed")
# # Call func1() and store its return value in variable x
# x = func1()
# # Print the return value of func1
# print(x)

def check_positive_number(num):
 i = int(input('Enter Your Number: '))
 if num < 0:
    raise ValueError("The number must be positive!")
 return num


# check_positive_number(10)
check_positive_number(-1)  # This will raise an error



