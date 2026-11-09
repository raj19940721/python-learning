technologies = ["React", "Next.js", "Python", "FastAPI"]

print(technologies)

employee = ["Raja", 31, 8.5, True]

print(employee)

# Create a Python list containing your five technical skills and perform these operations:
# 1. Print the complete list.
# 2. Print the first element.
# 3. Print the third element.
# 4. Print the last element using negative indexing.
# 5. Print the second-last element using negative indexing.

skills = ["JavaScript", "React", "Next.js", "TypeScript", "Python"]

print(skills)
print(skills[0])
print(skills[2])
print(skills[-1])
print(skills[-2])

# exercise 2 – List Operations

# adding elements to a list, removing elements from a list, updating elements, and printing the final list.

skills1 = ["JavaScript", "React", "Python"]

# Add "FastAPI" at the end using append().
# Insert "Next.js" at index 1 using insert().
# Add "Django" and "Flask" using extend().
# Print the final list.

skills1.append("FastAPI")
skills1.insert(1, "Next.js")
skills1.extend(["Django", "Flask"])
print(skills1)

skills2 = ["JavaScript", "React", "Next.js", "Python", "FastAPI", "Django"]

# Remove "React" using remove().
# Remove the last element using pop().
# Remove "Next.js" using del.
# Print the final list.

skills2.remove("React")
skills2.pop()
del skills2[1]
print(skills2) 

skills3 = ["JavaScript", "React", "Python", "Django", "Flask"]

# 1. Replace "React" with "Next.js".
# 2. Replace "Django" with "FastAPI".
# 3. Replace "Flask" with "LangChain".
# 4. Print the updated list.

skills3[1] = "Next.js"
skills3[3] = "FastAPI"
skills3[4] = "LangChain"
print(skills3)

skills4 = ["HTML", "CSS", "JavaScript", "React", "Next.js", "Python", "FastAPI"]

# Print the first three elements.
# Print elements from index 2 to index 5 (excluding 5).
# Print the last three elements.
# Print the complete list in reverse order using slicing.

print(skills4[:3])
print(skills4[2:5])
print(skills4[-3:])
print(skills4[::-1])

# Sorting and reversing a list

numbers = [45, 12, 89, 23, 67, 10]

# Sort numbers in ascending order.
# Sort numbers in descending order.
# Reverse the original list using reverse().
# Create a new sorted list using sorted() without modifying the original.

numbers.sort()
print("Sorted in ascending order:", numbers)
numbers.sort(reverse=True)
print("Sorted in descending order:", numbers)
numbers.reverse()
print("Reversed list:", numbers)
new_sorted = sorted(numbers)
print("New sorted list:", new_sorted)

# Final challenge

# Scenario: Employee Skills Management
# Create a list:

employee_skills = ["JavaScript", "React", "Python", "Django", "HTML", "CSS" ]

# Add "FastAPI" using append().
# Insert "Next.js" at index 2.
# Remove "Django" using remove().
# Replace "HTML" with "TypeScript".
# Print the first four skills using slicing.
# Create a new alphabetically sorted list using sorted().

employee_skills.append("FastAPI")
employee_skills.insert(2, "Next.js")
employee_skills.remove("Django")
employee_skills[4] = "TypeScript"
print(employee_skills[:4])
print(employee_skills)
new_sorted_skills = sorted(employee_skills)
print(new_sorted_skills)
