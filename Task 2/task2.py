# Task 1
while True:
    top: int = int(input("Please enter a positive number: "))
    if top <= 0:
        print("The number needs to be positive!\nTry again..")
        continue
    else:
        break
for i in range(1, top + 1):
    print(i, end=" ")
print("")

# Task 2
a: int = int(input("Please enter a number: "))
b: int = int(input("Please enter a number: "))
if a > b:
    for i in range(b, a + 1):
        print(i, end=" ")
elif b > a:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    print(f"The numbers you entered are equal.({a})")

# Task 3
n: int = int(input("Please enter a number: "))
for i in range(0, n+1):
    if i % 2 == 0:
        print(i, end=" ")

# Task 4
max: int = int(input("Please enter a number (max): "))
den: int = int(input("Please enter a number (den): "))
while den > max:
    print(f"The den number cannot be bigger than the max number.\n"
          f"maybe youve been mistaken and you meant that {den} is the max and {max} is den.")
    ans: str = input(f"Do you want to switch them and put {den} into max and {max} into den? (yes/no): ").lower()
    if ans == "yes":
        temp: int = den # משתנה להחלפה בין den ל max
        den = max
        max = temp
    elif ans == "no":
        max: int = int(input("Please enter a number (max): "))
        den: int = int(input("Please enter a number (den): "))
    else:
        print(f"The program has finished because your answer didn't match what requested. ")
        break
if max >= den:
    for i in range(1, max+1):
        if i % den == 0:
            print(i, end=" ")
