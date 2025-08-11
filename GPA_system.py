students_data = {}
option = True

print("Welcome to the students data software.")
while option:
    gpa_data = [] #list
    student = input("What is the student name?\n")
    for i in range(4):
        gpaText = input("What is the gpa for the course " + str(i+1)+"\n")
        gpa = float(gpaText)
        gpa_data.append(gpa)

    sum = 0
    for gpa in gpa_data:
        sum += gpa

    avg_gpa = sum/4

    students_data[student] = avg_gpa
    user_input = input("Would you like to add more students data?y/n\n")
    option = (user_input == 'y')

print(students_data)


