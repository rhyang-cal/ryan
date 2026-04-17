def say_goodbye(name):
    #Prints a goodbye message with the given name
    print("Goodbye", name)

def circle_area(radius):
    #Calculates the area of a circle given its radius
    print(3.14*radius*radius)

def subtract(a, b):
    #Subtracts b from a and returns the result
    return a - b

def multiply(a, b):
    #Multiplies a and b and returns the result
    return a * b

def divide(a, b):
    #Divides a by b and returns the result
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def what_to_wear(temperature):
    #returns a tuple with the minimum and maximum temperatures in a list
    return (min(temperature), max(temperature))

def is_weekend(day):
    #Checks if the given day is a weekend (Saturday or Sunday)
    if day < 6:
        return False
    return True

def fuel_efficiency(distance, fuel):
    #Calculates the fuel efficiency in miles per gallon
    if fuel != 0:
        return distance / fuel
    else:
        return "Error: Fuel cannot be zero."
    
def secret_code(integer):
    #returns an encrypted version of the integer by moving the last digit to the front of the number
    last_digit = integer % 10
    remaining_digits = integer // 10
    return int(str(last_digit) + str(remaining_digits))

def oski_power(x, y):
    #returns the result of x raised to the power of y
    start = 1
    for i in range(y):
        start *= x
    return start

def min_for(numbers):
    #returns the minimum value from the list of numbers
    min_val = numbers[0]
    for n in numbers:
        if n < min_val:
            min_val = n
    return min_val

def max_for(numbers):
    #returns the maximum value from the list of numbers
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def min_while(numbers):
    #returns the minimum value from the list of numbers using a while loop
    min_val = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] < min_val:
            min_val = numbers[i]
        i += 1
    return min_val

def max_while(numbers):
    #returns the maximum value from the list of numbers using a while loop
    max_val = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > max_val:
            max_val = numbers[i]
        i += 1
    return max_val

def sum_py(number):
    #returns the sum of an integer's digits'
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

print(sum_py(2468))