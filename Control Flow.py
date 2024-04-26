# Example 3: Control Flow
# If-else statement
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1



# There are multiple ways to write loops and if-else statements in Python. Below are some examples demonstrating different syntaxes and styles:


# Example 1: Using a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Example 2: Using a while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1



# Example 3: Using list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)



# Example 1: Simple if-else statement
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")



# Example 2: Using if-elif-else statement
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'D'
print("Grade:", grade)



# Example 3: Using list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)
