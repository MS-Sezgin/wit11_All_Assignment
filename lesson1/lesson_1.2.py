"""
✅ Project 2: Age Check
Practice input, type conversion, and conditions.

Ask the user for their age.
If under 18 → print “You are not an adult”.
Else → print “You are an adult”.
Ask for birth year and calculate age (use 2025).
"""

age = int(input("give me your age"))

print("You are an adult" if age >= 18 else "You are not an adult")

otoAge = 2025 - int(input("give me your birthday"))

print(f"your age is : {otoAge}")