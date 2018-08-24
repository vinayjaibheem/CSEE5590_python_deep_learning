def third_task():
    string = input("Input a string\n")
    digit = 0
    letter = 0

    for char in string:
        if char.isdigit():
            digit = digit + 1
        elif char.isalpha():
            letter = letter + 1
        else:
            pass

    print("Letters", letter)
    print("Digits", digit)


third_task()