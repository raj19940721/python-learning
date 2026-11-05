
# Variables and data types

print("Hello Raja!")
print("Welcome to Python Programming")
print("My goal is to become a GenAI Application Engineer")

name = "Raja"
age = 31
experience = 8
is_developer = True
float_value = 3.14

print("Name:", name)
print("Age:", age)
print("Experience:", experience, "years")
print("Is Developer:", is_developer)
print("Float Value:", float_value)


print("Data Types:")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of experience:", type(experience))
print("Type of is_developer:", type(is_developer))
print("Type of float_value:", type(float_value))

name= "Raja"
age =  31
experience = 8
current_technology = "React.js"
learning_technology = "Python"
target_role = "GenAI Application Engineer"

print("Name:", name)
print("Age:", age)
print("Experience:", experience, "years")
print("Current Technology:", current_technology)
print("Learning Technology:", learning_technology)
print("Target Role:", target_role)

print("Data Types:")
print("Type of Name:", type(name))
print("Type of Age:", type(age))
print("Type of Experience:", type(experience))
print("Type of Current Technology:", type(current_technology))
print("Type of Learning Technology:", type(learning_technology))
print("Type of Target Role:", type(target_role))

# operators

a = 20
b = 10

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Comparison Operators

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal To:", a >= b)
print("Less Than or Equal To:", a <= b)

# Logical Operators

age = 25
is_employed = True
has_experience = True

if age >= 18 and is_employed:
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")

if is_employed or has_experience:
    print("You have some work experience.")
else:
    print("You have no work experience.")

if not is_employed:
    print("You are currently unemployed.")


# Requirements:
# - Employee name = Raja
# - Age = 31
# - Experience = 8
# - Is employed = True
# Conditions:
# 1. If age is below 18, print Not Eligible.
# 2. If experience is 8 or more AND employed is True, print Senior Employee.
# 3. If experience is 5 or more, print Mid-Level Employee.
# 4. Otherwise, print Junior Employee.

employee_name = "Raja"
age1 = 31
experience1 = 8
is_employed = True

if age1 < 18:
    print("Not Eligible.")
elif experience1 >=8 and is_employed:
    print("Senior Employee.")
elif experience1 >= 5:
    print("Mid-Level Employee.")
else:
    print("Junior Employee.")

# Loops

# Exercise 1 – Print numbers

# Print numbers from 1 to 10 using a for loop.

# Exercise 2 – Even numbers

# Print even numbers from 1 to 20 using range().

# Exercise 3 – Multiplication table

# Print the multiplication table of 5.

for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

# Exercise 4 – While loop

# Print numbers from 1 to 5 using a while loop.

# Exercise 5 – Break and Continue

# Print numbers from 1 to 10, but:
# - Skip number 5 using continue.
# - Stop when the number reaches 8 using break.

i = 1
while i <= 5:
    print(i)
    i += 1

i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    if i == 8:
        break

    print(i)
    i += 1

# 4. Final Day 1 challenge
# Before we finish, solve this without looking at previous examples.

# Problem: Find the sum of numbers from 1 to 10.

# Expected output:
# Sum of numbers: 55


# Hint: Create a variable total = 0 and use a for loop.

total = 0
for i in range(1, 11):
    print(i)
    total += i

print("Sum of numbers:", total)
