
def firstnonrepeatedchar():
    input1 = input("Enter the string")
    stack = list(input1.replace(" ","")) #remove spaces between words entered by user and convert to list
    print(stack)

    repeated = [] #repeated chars in the string
    first = [] #every character parsed in the string
    onlyone = []  #characters which have count 1

    for i in stack:
        if i not in first:
            first.append(i)   #append each element entering into the stack
        else:
            repeated.append(i)   #Append the duplicate elements in this
    for j in stack:
        if j in first and j not in repeated:
            onlyone.append(j)   #append the not repeating character

    print("The first non-repeated character in the string is",onlyone[0])   #print the first non-repeating character

firstnonrepeatedchar()
