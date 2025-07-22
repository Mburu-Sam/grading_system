def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def weighted_score(exam, assignment, participation):
    return (exam * 0.5) + (assignment * 0.3) + (participation * 0.2)

def main():
    num_students = int(input("How many students do you want to enter? "))
    student_records = []

    for _ in range(num_students):
        print("\nEnter student data:")
        name = input("Name: ")
        exam = float(input("Exam score (0-100): "))
        assignment = float(input("Assignment score (0-100): "))
        participation = float(input("Participation score (0-100): "))

        final_score = weighted_score(exam, assignment, participation)
        grade = calculate_grade(final_score)

        student_records.append({
            "name": name,
            "score": round(final_score, 2),
            "grade": grade
        })

    print("\n📋 Final Report Card")
    print("-----------------------")
    for student in student_records:
        print(f"{student['name']}: {student['score']}% - Grade: {student['grade']}")

if __name__ == "__main__":
    main()
