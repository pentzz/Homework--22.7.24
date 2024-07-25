# Task 1
sum: int = None
a: int = 0
while True:
    a: int = int(input("Please enter a number: "))
    if a == -99:
        break
    if sum == None:
        sum = 0
    sum = sum + a

print(f"The sum of the numbers you entered is: {sum}")

# Task 2
a: int = int(input("Please enter a number: "))
if a == -99:
    max = None
    min = None
else:
    max: int = a
    min: int = a
    while True:
        if a == -99:
            break
        if a <= 0:
            break
        if a > max:
            max = a
        if a < min:
            min = a
        a: int = int(input("Please enter a number: "))
print(f"The max number is: {max}.\nThe min number is :{min}.")

# Task 3
num_list: list = []
max: int = None
ans: int = 0
for i in range(5):
    num: int = int(input("Please enter a number: "))
    num_list.append(num)
    if i == 0:
        max = num
    if num > max:
        max = num
        ans = i
print(f"The serial number of the highest number is {ans+1}. (the number {num_list[ans]})")

# Task 4
a: int = int(input("Please enter a number: "))
b: int = int(input("Please enter a number: "))
ans: int = 0
for _ in range(a):
    ans = ans + b
print(f"The answer is {ans}")

# Task 5
a: int = int(input("Please enter a number: "))
b: int = int(input(f"Please enter the power for the number {a}: "))
ans: int = a
for _ in range(b-1):
    ans = ans * a
print(f"The answer is {ans}. ({a} in the power of {b})")

# Task 6 (Bonus) solution 1
num: int = int(input("Please enter a number: "))
is_it_there: bool = False
while True:
    dig: int = int(input("Please enter a single digit: "))
    if int(dig / 10) != 0:
        print(f"Error you need to enter a single digit\nTry again..")
        continue
    else:
        while num >= 1:
            z: int = num % 10
            if dig == z:
                is_it_there = True
                break
            else:
                num: int = int(num / 10)
                continue
        break
print(f"{is_it_there}- the digit {dig} is in the number you entered" if is_it_there else
      f"{is_it_there} - the digit {dig} is NOT in the number you entered")
# Task 6 (Bonus) solution 2
num: int = int(input("Please enter a number: "))
digit: int = int(input("Please enter a single digit: "))

is_it_there: bool = str(digit) in str(num)

print(is_it_there)


# Task 7 (Bonus)
num1: int = int(input("Please enter a number: "))
num2: int = int(input("Please enter a number: "))
min: int = num1 if num1 < num2 else num2
maxdiv: int = 1
for _ in range(2, min+1):
    if num1 % _ == 0 and num2 % _ == 0:
        maxdiv = _
print(f"The max divisor of {max} and {min} is: {maxdiv}.")

# Task 8
is_it_prime: bool = True
num: int = int(input("Please enter a number: "))
for _ in range(2, num):
    if num % _ == 0:
        is_it_prime = False
print(f"The number {num} in NOT prime" if not is_it_prime else f"The number {num} is prime.")
