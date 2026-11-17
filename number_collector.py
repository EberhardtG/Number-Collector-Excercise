# number_collector.py

from builtins import ValueError

try:
    num1 = int(input("Enter number 1: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num1 = 0

try:
    num2 = int(input("Enter number 2: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num2 = 0

try:
    num3 = int(input("Enter number 3: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num3 = 0

total = num1 + num2 + num3
average = total / 3

print()
print(f"Your numbers: {num1}, {num2}, {num3}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")
