
def notcommonStudents():
    input1 = input("Enter students of Python Class")
    python_list = list(input1.split())
    python_list1 = set(python_list)   #converting list A into set A
    print("The students in python class ", python_list1)

    input2 = input("Enter students of Web Application Class")
    webapp_list = list(input2.split())
    webapp_list1 = set(webapp_list)         #converting list B into set B
    print("The students in web application class ", webapp_list1)

    result_list = python_list1.difference(webapp_list1)        #Using set difference to find A-B(students in A but not in B)
    print("The result list of those students in python class but not in web application class ", result_list)

notcommonStudents()