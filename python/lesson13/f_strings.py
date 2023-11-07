person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person,coins)
print(message)

message = "\n{} has {} coins left.".format(person,coins)
print(message)

# {1} and {0} are the indexes of the format
message = "\n{1} has {0} coins left.".format(coins,person)
print(message)

message = "\n{person_aux} has {coins_aux} coins left.".format(coins_aux=coins,person_aux=person)
print(message)

# Adding a dictionary
player = { 'person': 'Dave', 'coins': 3}
# passing the dictionary to the format
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

###############
# f-Strings! This is the way.

# Letter f is similar to the .format()
message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 *5} coins left."
print(message)

message = f"\n{person.lower()} has {2 *5} coins left."
print(message)

message = f"\n{player['person']} has {player['coins']} coins left."
print(message)

########################
# You can pass formatting options

num = 10
# The .2f says the number of decimals and f means fixed
print(f"\n2.25 times {num} is {2.25* num:.2f}\n")

for num in range(1,11):
    print(f"2.25 times {num} is {2.25* num:.2f}\n")

for num in range(1,11):
    # The .2% means is going to return the % so is going to 
    # multiply the result of the division by 100
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")


