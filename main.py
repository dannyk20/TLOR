def count_elements(my_list):
    return len(my_list)

# 예제 사용법
example_list = [1, 2, 3, 4, 5]
result = count_elements(example_list)
print(f"The number of elements in the list is: {result}")

def is_even(number):
    return number % 2 == 0

# 예제 사용법
num = 8
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is not even.")

def add_numbers(a, b):
    return a + b

# 예제 사용법
num1 = 5
num2 = 10
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")

def to_uppercase(input_string):
    return input_string.upper()

original_string = "Hello, World!"
uppercase_string = to_uppercase(original_string)
print(uppercase_string)
