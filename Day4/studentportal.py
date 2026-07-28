def InputMarks(n):
    marks = []
    for i in range(n):
        mark = float(input(f"Enter mark for subject {i + 1}: "))
        marks.append(mark)
    return marks

def Percentage(marks):
    total = sum(marks)
    length = len(marks)
    percentage = (total / (length * 100)) * 100
    return percentage
def grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

while True:
    n = int(input("Enter the number of subjects: "))
    marks = InputMarks(n)
    percentage = Percentage(marks)
    student_grade = grade(percentage)
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {student_grade}")

    cont = input("Do you want to enter marks for another student? (yes/no): ")
    if cont.lower() != 'yes':
        break