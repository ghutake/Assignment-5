student_marks = {"Alice":85 ,"Bob":75 ,"Rohan":76}
student_name = input("Enter the student's name:")

if student_name in student_marks:
    marks = student_marks[student_name]
    print(f"{student_name}'s marks:{marks}")
else:
    print(f"student not found.")