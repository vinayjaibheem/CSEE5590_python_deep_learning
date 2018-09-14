def removeWords():
    words = []
    with open("file1.txt") as f:
        for line in f:
            words.append(line.split(" "))  #file1.txt converted into list
        print("*********The words in file1 are: ",words[0])

    words1 = []
    with open("file2.txt") as f2:
        for line1 in f2:
            words1.append(line1.split(" "))   #file2 converted into list
        print("***********The words in file2 are: ",words1[0])

    notmatch = []
    for i in words[0]:
        if i not in words1[0]:    #for words in file1 but not in file2
            #print(i)
            notmatch.append(i)  #append into notmatch list

    print("**************The file1 without file2 words in file1 are",notmatch)

removeWords()