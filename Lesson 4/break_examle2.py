name = None

while True:
    print("Menu:")
    print("1. Enter name")
    print("2. Say Hello")
    print("3. Exit")

    print()

    response = input("Please choose an action: ")
    
    
    if response == "1":
        name = input("Enter your name: ")
    elif response == "2":
        if name:
            print("Hello ", name, "!!!")
            print()
        else:
            print("I don't know your name")
            print()
    elif response == "3":
        break
    else:
        print("incorrect input")

print()


