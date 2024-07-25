# Task 1
a: float = float(input("Please enter a number: "))
b: float = float(input("Please enter a number: "))
if a > b:
    for _ in range(3):
        print(b, end=" ")
elif a < b:
    for _ in range(3):
        print(a, end=" ")
else:
    print("The numbers are even!")
print("")

# Task 2
a: int = int(input("Please enter a number: "))
b: int = int(input("Please enter a number: "))
print(f"The average is : {(a+b)/2}")

# Task 3
a: int = int(input("Please enter the first number: "))
b: int = int(input("Please enter the second number: "))
c: int = int(input("Please enter the third number: "))
if a == b and a == c:
    print(f"All the numbers are equal [ {a} ]")
elif a > b and a > c:
    print(f"The bigger number is: {a}")
elif b > a and b > c:
    print(f"The bigger number is: {b}")
elif c > a and c > a:
    print(f"The bigger number is: {c}")
# Task 4
movie_len: int = int(input("Please enter the movie len (in minutes): "))
hours: int = int(movie_len / 60)
minutes: int = int(movie_len % 60)
print(f"The movie len is: {hours} hour(s) and {minutes} minute(s)")
# Task 5
number: int = int(input("Please enter a 4 digit number: "))
print(f"The unity digit in the number is: {number % 10}")
# Task 6
number: int = int(input("Please enter a 4 digit number: "))
print(f"The 2nd unity digit in the number is: {int(number // 10 % 10)}")
# Task 7
number: int = int(input("Please enter a 2 digit number: "))
print(f"The sum of the digits of the number is: {int(number % 10 + number / 10)}")
# Task 8
number: int = int(input("Please enter a 2 digit number: "))
print(f"The new number is: {int(number % 10)}{int(number / 10)}")
# Task 9
number: int = int(input("Please enter a number: "))
while number == 0:
    print("Error! the number need to be different than 0.\nTry again!")
    number: int = int(input("Please enter a number: "))
print(f"The number {number} is even" if number % 2 == 0 else f"The number {number} is odd")
# Task 10
while True:
    salary: int = int(input("Please enter your salary: "))
    if salary <= 0:
        print(f"Pleas enter a valid number. ( cannot be zero or negetive )")
        continue
    else:
        break
if salary > 50_000:
    print(f"The tax you need to pay is {(salary - 50_000) * 0.51 + 14_650}")
elif salary > 35_000:
    print(f"The tax you need to pay is {(salary - 35_000) * 0.45 + 7900}")
elif salary > 25_000:
    print(f"The tax you need to pay is {(salary - 25_000) * 0.4 + 3900}")
elif salary > 18_000:
    print(f"The tax you need to pay is {(salary - 18_000) * 0.3 + 1800}")
elif salary > 12_000:
    print(f"The tax you need to pay is {(salary - 12_000) * 0.2 + 600}")
elif salary > 6000:
    print(f"The tax you need to pay is {(salary - 6000) * 0.1}")
else:
    print(f"You dont need to pay tax.")
# Task 11
age: int = int(input("Please enter your age: "))
if age >= 8:
    height: int = int(input("Please enter your height (in cm) : "))
    if age >= 8 and age <= 18:
        if height >= 115:
            print(f"You can get in the rollercoaster!")
        else:
            print(f"unfortunately you cant get in the rollercoaster because your height is lower than 115 cm.")
    elif age >= 18:
        if height >= 100:
            print(f"You can get in the rollercoaster!")
        else:
            print(f"unfortunately you cant get in the rollercoaster because your height is lower than 101 cm")
else:
    print(f"unfortunately you cant get in the rollercoaster because of your age.\n"
          f"you need to be at least 8 years old (you are {age} years old).")