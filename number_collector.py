print("=" * 40)
print(" Number Collector")
print("=" * 40)

numbers = []

try:
    entered_number1 = float(input("Enter a number: "))
    numbers.append(entered_number1)
except ValueError:
    print("Invalid input. Please enter a valid number.")

try:
    entered_number2 = float(input("Enter a number: "))
    numbers.append(entered_number2)
except ValueError:
    print("Invalid input. Please enter a valid number.")

try:
    entered_number3 = float(input("Enter a number: "))
    numbers.append(entered_number3)
except ValueError:
    print("Invalid input. Please enter a valid number.")

print(f"\nYou entered the numbers: {numbers}")
print(f"Sum: {sum(numbers):.2f}")
print(f"Average: {sum(numbers)/len(numbers):.2f}")



