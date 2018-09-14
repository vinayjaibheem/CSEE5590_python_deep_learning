import csv
def DnaTest():
    input1 = input("Enter the codon sequence")
    print("The input sequence is" ,input1)

    value = [input1[i:i+3] for i in range(0,len(input1),3)]
    print("String seperated by a size value of 3" , value)

    count1 = value.count('AAA')
    count2 = value.count('GGG')
    count3 = value.count('TTT')


    dict1 = {}

    with open("codon.tsv") as tsvfile:
        for row in tsvfile:
            (key , val) = row.split()
            dict1[key] = val
    print(dict1)
    for i in dict1:
        if i == "TTT":
            result1 = (dict1.get(i))
        elif i == "AAA":
            result2 = dict1.get(i)
        elif i == "GGG":
            result3 = dict1.get(i)
    print(result1, count3)
    print(result2, count1)
    print(result3 , count2)

DnaTest()
