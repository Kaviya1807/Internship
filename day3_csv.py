import csv

# Writing data into CSV file

students = [
    ["Name", "Age", "Mark"],
    ["Kaviya", 19, 90],
    ["Priya", 20, 85],
    ["Divya", 19, 95]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Student data saved successfully!")

# Reading CSV file

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    print("\nStudent Details:")

    for row in reader:
        print(row)