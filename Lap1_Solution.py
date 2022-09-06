import math

# Problem 1

print("============================")
print("Enter the circle radius: ")
radius = float(input())
result = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is: {result}")

# Problem 2

print("============================")
number1 = 1234567.456
number2 = 1234567.456
print('{:,}'.format(number1))
print('{:,.0f}'.format(number2))

# Problem 3

print("============================")
print("Enter the amount of purchase: ")
amount = float(input())
tax = amount * 0.05
print(f"Total purchase = {amount} SR \nSales Tax = {tax} SR \nTotal = {amount + tax} SR")

# Problem

print("============================")


def lbs_to_kgs(lbs):
    kgs = lbs / 2.205
    return '{:.2f}'.format(kgs)


print("Enter the weight in pound: ")
pounds = int(input())
weight = lbs_to_kgs(pounds)
print(f"The weight in kilograms = {weight} kgs ")

# Problem 5

print("============================")
print("Enter the value of x:")
x = int(input())
print("Enter the value of y:")
y = int(input())

compute = y*x*y + x*y + x*y*x
print(f"The compute value is: {compute}")

print("============================")
