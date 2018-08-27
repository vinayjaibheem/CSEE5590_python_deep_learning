fileName= input("Enter filename")
infile= open(fileName,'r')

count = 0
for line in infile:
    words = line.split()
    count = sum(len(word) for word in words)
    print(line,len(words), count , "\n")

