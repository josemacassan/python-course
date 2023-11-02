
name = "Dave"
count = 1


def another():
    color = "Blue"
    # You cannot modify global variables
    #count += 1
    # That´s the way to modify global values
    global count
    count += 1
    print(count)

    def greeting(firstname):
        nonlocal color
        color = "red"
        print(color)
        print(name)
        print(firstname)

    greeting("Dave")

print(count)
another()
