import math
""" 1   Create an empty list called my_list.
    Add integers from 1 to 5 to the list.
    Print the list.
    Add the numbers 6, 7, and 8 to the list.
    Print the updated list.
    Access and print the element at index 3.
    Check if the number 5 is in the list."""

my_list = [1,2,3,4,5]
print(my_list)
my_list.append(6)
my_list.append(7)
my_list.append(8)
print(my_list)
print(my_list[2])
print(5 in my_list)

""" 2    Create a list of your favorite fruits.
    Add "banana" to the end of the list.
    Insert "orange" at index 1.
    Remove the fruit at index 3.
    Print the updated list."""

fruits = ["blueberry", "apple", "watermelon", "kiwi"]
fruits.append("banana")
print(fruits)
fruits.insert(1, "orange")
print(fruits)
# Removes the element at index 3, if you don´t pass any argument it removes the last element of the list
fruits.pop(3)
print(fruits)

"""Exercise 3: List Slicing

    Create a list of numbers from 1 to 10.
    Print the first three elements.
    Print the last three elements.
    Print every second element in the list."""

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[:3])
print(numbers[-3:])
# It goes from 0 to the end and prints every 2 steps
print(numbers[::2])


""" 4   Create a list of squares for the numbers 1 to 5 using list comprehension.
    Create a list of even numbers from 1 to 10 using list comprehension.
    Create a new list that contains the squares of the even numbers from the previous list."""

square_nums = [x**2 for x in range(1,6)]
print(square_nums)

even_nums = [x for x in range(1,11) if x % 2 == 0]
print(even_nums)

odd_numbers = [x for x in range(1,11) if x % 2 != 0]
print(odd_numbers)

square_evens = [x**2 for x in even_nums]
print(square_evens)