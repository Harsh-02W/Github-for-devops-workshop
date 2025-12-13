print("Hello doston!");
# basic_math.py

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform basic math operations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

# Handle division safely
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "undefined (division by zero)"

# Print the results
print(f"\nResults:")
print(f"Addition: {sum_result}")
print(f"Subtraction: {diff_result}")
print(f"Multiplication: {prod_result}")
print(f"Division: {div_result}")

