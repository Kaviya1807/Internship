import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    marks = []

    for row in reader:
        marks.append(int(row["Mark"]))
        print(row["Name"], row["Age"], row["Mark"])

if marks:
    print("Total Students:", len(marks))
    print("Average Mark:", sum(marks) / len(marks))
    print("Highest Mark:", max(marks))
    print("Lowest Mark:", min(marks))