
# Exercise 1


def fibonacci(n):
    dict = {}
    prev = 0
    next = 1
    sum = 0
    count = 0
    while count < n:
        count += 1
        dict[count] = sum
        prev = next
        next = sum
        sum = prev+next
    return dict


try:
    num = int(input("Please enter a number (from 1 to N): "))
    if num >= 1:
        print(fibonacci(num))
    else:
        print("Error! The number must be betwenn 1 to N")
        exit()

except ValueError:
    print("Error! wrong input the number must be integer")


# Exercise 2

def count_str(str):
    dictStr = {}
    for x in str:
        countKey = dictStr.keys()
        if x in countKey:
            dictStr[x] += 1
        else:
            dictStr[x] = 1
    return dictStr

print(count_str("google.com"))

# Exercise 3

def checkSets(A,B):
    newDic = A - B
    return newDic


SetA = {4, 5, 6, 7, 8}
SetB = {1, 2, 3, 4, 5}
print(checkSets(SetA,SetB))
print(checkSets(SetB,SetA))

# Exercise 4
dict5 = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

def subject(sub):
    newlist = []
    for x in dict5:
        newlist.append(x[sub])
    return newlist

print(subject("Science"))
print(subject("Math"))


# Exercise 5

def addEmployee(num):
    employee_file = open("EmployeeRecords.txt", "w")

    for x in range(num):
        print(f"Please Enter information for employee {x + 1}: ")
        try:
            name = str(input())
            department = str(input())
            salary = float(input())
            if salary >= 0:
                employee_file.write(f"{name}\n")
                employee_file.write(f"{department}\n")
                employee_file.write(f"{salary}\n")

            else:
                print("Error! salary cannot be negative")
                exit()

        except ValueError:
            print("Error! wrong input")
            exit()
    employee_file.close()


def readFile():
    employee_file = open("EmployeeRecords.txt", "r")
    record = employee_file.readline()
    print("====================")
    print("Reading Employee file text")
    print("====================")
    while record != '':
        record = record.rstrip("\n")
        print(record)
        record = employee_file.readline()
    employee_file.close()


def delSecondRecord():
    print("==========================")
    print("Deleting record number 2 ...")
    print("==========================")

    try:
        check = False
        lines = []
        employee_file = open("EmployeeRecords.txt", "r")
        lines = employee_file.readlines()

        employee_file = open("EmployeeRecords.txt", "w")
        for num, line in enumerate(lines):
            if num not in [3, 4, 5]:
                employee_file.write(line)
            else:
                check = True
        if check == False:
            print("Couldn't find the second record")
        employee_file.close()
    except IndentationError:
        print("Error! Indentation Error ")
        exit()



try:
    employee = int(input("Please Enter how many employees: "))
    if (employee > 0):
        addEmployee(employee)
    else:
        print("The input must be greater than 0")

except ValueError:
    print("Error! the input is not a number")
    exit()

readFile()
delSecondRecord()
readFile()