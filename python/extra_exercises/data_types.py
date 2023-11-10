# Exercise 1: Type Conversion

# Convert the following variables to different data types
# 1. Convert `num_str` to an integer and store it in a variable `num_int`
# 2. Convert `num_float` to a string and store it in a variable `num_str`
# 3. Convert `flag` to an integer and store it in a variable `flag_int`

num_str = "123"
num_float = 123.123
flag = True

num_int = int(num_str)
num_str = str(num_float)
flag_int = int(flag)

print("Str to  int: ", num_int, type(num_int))
print("Float to str: ", num_str, type(num_str))
print("Flag to int: ", flag_int, type(flag_int))


# Exercise 2: String Manipulation

# Given a string `original_string`, perform the following operations:
# 1. Extract and print the first three characters.
# 2. Print the length of the string.
# 3. Convert the string to lowercase and print the result.
# 4. Replace any occurrence of the letter 'o' with 'x' and print the modified string.

original_string = "HelloWorld"

#1
print(original_string[:3])
#2
print(len(original_string))
#3
print(original_string.lower())
#4
print(original_string.replace('o','x'))


# Exercise 3: List Operations

# Given a list of numbers `numbers`, perform the following operations:
# 1. Print the length of the list.
# 2. Print the sum of all the numbers in the list.
# 3. Check if the number 5 is present in the list. Print the result.
# 4. Create a new list `squared_numbers` containing the square of each number in the original list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1
print(len(numbers))
#2
suma = 0
for number in numbers:
    suma += number
print(suma)   
print(sum(numbers))

#3
print(5 in numbers)

#4
new_list = []
for num in numbers:
    num *= num
    new_list.append(num)

print(new_list)