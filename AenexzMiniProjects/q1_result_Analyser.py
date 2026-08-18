def Grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Fail"


def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)
    grade = Grade(average)

    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average:.2f}")
    print(f"Grade: {grade}")

    # Check for subjects below 40 using a loop
    below_40 = []
    for i in range(len(marks)):
        if marks[i] < 40:
            below_40.append(f"Subject {i + 1} ({marks[i]})")

    if below_40:
        print("Subjects below 40:", ", ".join(below_40))
    else:
        print("Subjects below 40: None")


# Example Usage / Sample Input
student_name = "Rahul Sharma"
roll_number = 101
subject_marks = [85.5, 92.0, 38.0, 74.5, 35.0]

analyze_result(student_name, roll_number, subject_marks)
