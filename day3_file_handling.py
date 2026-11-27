# Writing data into a file

with open("student.txt", "w") as file:
    file.write("Name: Kaviya\n")
    file.write("Age: 19\n")
    file.write("Course: AI and ML\n")

print("Data saved successfully!")


# Reading data from a file

with open("student.txt", "r") as file:
    data = file.read()

print("\nStudent Details:")
print(data)