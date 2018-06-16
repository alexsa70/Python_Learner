x = int(input('x ='))

if 0 < x < 7:
    print("Value is in range, let's continue")
    y = 2 * x - 5
    print(y)
    if y < 0:
        print("Y is negative")
    elif y > 0:
            print("Y is positive")        
    else:
        print("y=0")
