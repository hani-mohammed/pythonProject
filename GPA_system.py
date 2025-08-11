students_data = {}
more_students_option = True
print("Welcome to the students data software.")
while more_students_option:
    sum = 0
    count = 0
    student = input("What is the student name?\n")
    more_gpa_option = True
    while more_gpa_option:
        gpaText = input("Enter the GPAs. Enter -1 to finish adding gpas.\n")
        gpa = float(gpaText)
        if gpa != -1:
            sum += gpa
            count +=1
        else :
            more_gpa_option = False


    avg_gpa = sum/count

    students_data[student] = avg_gpa
    print("Student "+ student +"  was added successfully.")
    user_input = input("Would you like to add more students data?y/n\n")
    if user_input.lower() == 'y' or user_input.lower() == 'yes':
        more_students_option = True
    elif user_input.lower() == 'n' or user_input.lower() == 'no':
        more_students_option = False
    else:
        raise NameError("Please Enter a valid option")
print(students_data)


