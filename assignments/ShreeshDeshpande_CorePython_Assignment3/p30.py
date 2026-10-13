

def get_result_details(percentage):
    if percentage >= 90: return 'A', 'Pass'
    if percentage >= 80: return 'B', 'Pass'
    if percentage >= 70: return 'C', 'Pass'
    if percentage >= 60: return 'D', 'Pass'
    return 'F', 'Fail'

subjects = ["Python", "Maths", "Database", "Networks", "AI"]
marks = [(input(f"Enter marks for {sub}: ")) for sub in subjects]

total = sum(marks)
percentage = total / len(subjects)
grade, result = get_result_details(percentage)

print(f"\nTotal Marks: {total}")
print(F"\nPercentage: {percentage:.1f}%")
print(f"\nGrade: {grade}")
print(f"\nResult: {result}")