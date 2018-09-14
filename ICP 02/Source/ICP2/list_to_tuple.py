def list_to_tuple():
    input1 = input("Enter a list of numbers to be converted \n")
    l = list(input1)
    print(l)
    t = tuple(l)
    print("The Tuple values for 1st and last element of the list are",tuple(t[0] + t[-1]))


list_to_tuple()
