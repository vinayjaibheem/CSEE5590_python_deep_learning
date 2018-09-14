import csv


line = input("Enter the string: ") #'TTTTTCTTA'
size = 3
chars = [line[i:i+size] for i in range(0, len(line), size)]
elements_dict = {}
result_dict = {}
result_dict_copy = {}
result_list = []


with open('codon.tsv') as tsvfile:
    reader = csv.reader(tsvfile,delimiter='\t')
    for row in tsvfile:
        (key, value) = row.split()
        elements_dict[key] = value


for list_element in chars:
    result_dict[list_element] = elements_dict[list_element]


result_dict_copy = result_dict
count = 0

for list_element in result_dict:
     if result_dict[list_element] != result_dict[list_element]:


print(count)

