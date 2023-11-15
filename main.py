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