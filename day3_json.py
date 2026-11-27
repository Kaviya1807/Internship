import json

# Student data
student = {
    "name": "Kaviya",
    "age": 19,
    "course": "AI and ML"
}

# Save data into JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Data saved successfully!")

# Read data from JSON file
with open("student.json", "r") as file:
    data = json.load(file)

print("\nStudent Details:")
print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])