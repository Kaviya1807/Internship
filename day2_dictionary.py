student = {
    "name": "Kaviya",
    "age": 19,
    "mark": 90
}

print(student["name"])
print(student.get("mark"))

student.update({"age": 20})

print(student)
print(student.items())