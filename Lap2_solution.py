import random

# Problem 1
def printnums(num):
    if num % 2 == 0:
        print(f" {num} is even and all the following are the even numbers from 0 to {num}: ")
        for even in range(0, num+1, 2):
            print(even, end=" ")
    else:
        print(f" {num} is odd and all the following are the even numbers from 1 to {num}: ")
        for odd in range(1, num+1, 2):
            print(odd, end=" ")

print("============================")
try:
    number = int(input("Please enter a positive number: "))
except ValueError:
    print("Error! you need to enter a number")
else:
    if number<0:
        print(f"{number} is not a positive number")
    else:
        printnums(number)

print("\n============================")





# Problem 2
x = random.randint(1, 50)
y = random.randint(1, 50)

def checkanswer(answer):
    if x*y == answer:
        print("Congratulation the answer is correct!")
    else:
        print(f"Wrong answer!, the correct answer = {x*y}")

try:
    result = int(input(f"\n{x} * {y} =? : "))
except ValueError:
    print("Error! you need to enter a number")
else:
    checkanswer(result)
print("============================")

# Problem 3
def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

try:
    year = int(input("Please enter a year to check if it is leap or not: "))
except ValueError:
    print("Error you need to enter a number")
else:
    isLeapYear(year)
print("============================")

# Problem 4
for i in range(5):
    for j in range((5 - i) - 1):
        print(end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()


# Problem 5
number = 5
guess = None
attempts = 1

print("Guess the number!")
try:
    while guess != number:
        if attempts <= 5:
            guess = int(input("Is it... "))
        else:
            print("Sorry you ran out of attempts :( .")
            break

        if guess == number:
            print("Wow! You guessed it right!")
            break
        elif guess < number:
            print("Opps, It's bigger...")
            attempts = attempts + 1
        elif guess > number:
            print("Opps, It's not so big.")
            attempts = attempts + 1
except ValueError:
    print("Error! you need to enter a number")
print("============================")


