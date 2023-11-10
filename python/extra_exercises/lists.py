# Exercise 4: List Manipulation

# Given a list of words `word_list`, perform the following operations:
# 1. Print the length of the list.
# 2. Print the third word in the list.
# 3. Append the word "Python" to the end of the list.
# 4. Insert the word "Programming" at index 2.
# 5. Remove the second word from the list.
# 6. Print the final state of the list.

word_list = ["Hello", "World", "of", "Lists"]

#1
print(len(word_list))
#2
print(word_list[2])
#3
word_list.append("Python")
print(word_list)
#4
word_list.insert(2,"Programming")
print(word_list)
# 5
word_list.pop(1)
print(word_list)


# Exercise 5: List Manipulation and Filtering

# Given a list of numbers `number_list`, perform the following operations:
# 1. Create a new list `even_numbers` containing only the even numbers from the original list.
# 2. Create a new list `squared_odd_numbers` containing the squares of only the odd numbers from the original list.
# 3. Remove any duplicates from the original list and store the result in a new list `unique_numbers`.

number_list = [1, 2, 3, 4, 5, 2, 6, 3, 7, 8, 9, 10, 4, 6, 8, 10]
# 1
even_numbers = []
for num in number_list:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# 2
squared_odd_numbers = []
for num in number_list:
    if not num % 2 == 0:
        num *= num
        squared_odd_numbers.append(num)
print(squared_odd_numbers)

# 3
unique_numbers = []
for num in number_list:
    if not num in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)

# Other solution for exercise 3
# The set returns any an unorder list of unique elements, so it will remove the duplicates
# it returns a set so you have to encapsulate the list into a list() to return a [ ] instead of { }
unique_numbers_aux = list(set(number_list))
print(unique_numbers_aux)