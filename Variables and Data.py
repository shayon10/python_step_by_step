# Example 1: Variables and Data Types
# Declaring variables of different data types
name = "Alice"         # String
age = 30               # Integer
height = 5.7           # Float
is_student = True      # Boolean

# Printing the variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student?", is_student)


#for use as inline

# Example: Using Input Inline for Other Operators
# You can input two numbers inline and perform operations on them
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Arithmetic Operators
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
print("Remainder:", num1 % num2)
print("Exponentiation:", num1 ** num2)

# Comparison Operators
print("Is num1 equal to num2?", num1 == num2)
print("Is num1 not equal to num2?", num1 != num2)
print("Is num1 less than num2?", num1 < num2)
print("Is num1 greater than num2?", num1 > num2)
print("Is num1 less than or equal to num2?", num1 <= num2)
print("Is num1 greater than or equal to num2?", num1 >= num2)

# Logical Operators
bool1 = bool(int(input("Enter 0 or 1 for bool1: ")))
bool2 = bool(int(input("Enter 0 or 1 for bool2: ")))

print("bool1 and bool2:", bool1 and bool2)
print("bool1 or bool2:", bool1 or bool2)
print("not bool1:", not bool1)
