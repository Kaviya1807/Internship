numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sorted:", sorted(numbers, reverse=True))

for index, value in enumerate(numbers):
    print(index, value)