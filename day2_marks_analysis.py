def analyze_marks(marks):
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return average, highest, lowest


marks = [80, 90, 70, 85, 95]

avg, high, low = analyze_marks(marks)

print("Average:", avg)
print("Highest:", high)
print("Lowest:", low)