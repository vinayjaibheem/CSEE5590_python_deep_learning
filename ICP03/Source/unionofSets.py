def unionSet():


    input1 = input("Enter Set A")
    input2 = input("Enter Set B")

    SetA = set(input1.split())
    SetB = set(input2.split())

    #SetA = {"fatema","vinay"}

    #SetB = {"fatema"}

    Symt_Diff = SetA^SetB

    print(Symt_Diff)

unionSet()