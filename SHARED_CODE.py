import math

# A basic function to return the sum of the two numbers.
def add(num_1, num_2):
    return num_1 + num_2

# A basic function to return the difference of the two numbers.
def subtract(num_1, num_2):
    return num_1 - num_2

# A basic function to return the product of the two numbers.
def multiply(num_1, num_2):
    return num_1 * num_2

# A basic function to the the quotiont of the two numbers.
def divide(num_1, num_2):
    # A case to make sure that they cant divide by zero.
    if num_2 == 0:
        return "You cannot divide by 0"
    else:
        return num_1/num_2


