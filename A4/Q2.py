

student_grades = {'Ram': 85, 'Sham': 92}

def find_highest_grade(grades):
    highest_student = max(grades, key=grades.get)
    return highest_student

student_grades['Eve'] = 95

print("\nStudent Grades:")
for student in sorted(student_grades):
    print(f"{student}: {student_grades[student]}")

highest_student = find_highest_grade(student_grades)
print(f"\nStudent with the highest grade: {highest_student} with grade {student_grades[highest_student]}")
