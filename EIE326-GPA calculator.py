print("GPA Calculator for 6 Courses")

grades = []
units = []
total_points = 0
total_units = 0

# Loop to collect grades and unit loads
for i in range(6):
    print(f"\nCourse {i + 1}")
    grade = float(input("Enter grade point (A=5, B=4, etc.): "))
    unit = int(input("Enter unit load: "))

    grades.append(grade)
    units.append(unit)

    total_points += grade * unit
    total_units += unit

# Calculate GPA
if total_units == 0:
    print("Total unit load cannot be zero.")
else:
    gpa = total_points / total_units
    print(f"\nYour GPA is: {gpa:.2f}")
