# =========================================================
# Problem 1
employess = []

def add_employees():
    print("==== Enter 5 employees salaries =====")
    for i in range(5):
        try:
            salary = float(input(f" Please enter the salary for employee number {i+1}: "))
        except ValueError:
            print("Error Wrong input !")
            exit()

        employess.append(salary)


# 1. To diplay the salary list
def displaySalary():
    print(f"★	Display all employess salaries: {employess}")
    # for person in employess:
    #     print(f"The salary for employee 1 is {person}")

# 2. The lowest salary in the list
def lowestSalary():
    lowest = min(employess)
    print(f"2. The lowest salary in the list is: {lowest}")

def heightestSalary():
    heigest = max(employess)
    print(f"3. The heigest salary in the list is: {heigest}")

def totalSalary():
    total = 0
    for em in employess:
        total += em
    print(f"4. The total of all salaries is: {total}")

def changeValue2():
    print("5. Change the  value of index 2: ")
    employess[2] = 8000
    displaySalary()


def removeThird():
    print("6. Remove the third salary in the list: ")
    displaySalary()
    del employess[2]
    displaySalary()


def removeFirst():
    print("7. removing first occurrence in list: ")
    # exception 3000 not in the list
    try:
        x = employess.index(3000)
        employess.pop(x)
        displaySalary()
    except ValueError:
        print("Error! their is no 3000 in the list")
        exit()

def main():
    add_employees()
    displaySalary()
    lowestSalary()
    heightestSalary()
    totalSalary()
    changeValue2()
    removeThird()
    removeFirst()

main()

# =========================================================
# Problem 2
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
list3 = [1, 2, 3, 4, 5]
list4 = [6, 7, 8, 9]

def common_data(list1, list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
    return False

c1 = common_data(list1,list2)
c2 = common_data(list3,list4)
print(c1)
print(c2)

# =========================================================
# Problem 3
items = "Milk = 9 Eggs = 6 Bread = 4 Cheese = 7"
total = 0
for num in items:
    if num.isdigit():
        total += int(num)
print(f"The sum of item is: {total}")

# =========================================================
# Problem 4
origninallist = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
print(f"The maximum sum of sub lists: { max(origninallist, key=sum)}")
print(f"The minimum sum of sub lists:  { min(origninallist, key=sum) }")

# =========================================================
# Problem 5
t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)
new_t = []
for i in range(4):
    new_t.append(t1[i]+t2[i]+t3[i])
new_t = tuple(new_t)
print(new_t)