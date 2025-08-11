from util import *

students ={
    123: [123, "Sam", 3.4,3],
    234: [234, "Sara", 3.5,3],
    435: [435, "John", 3.2,1],
    563: [563, "Tom", 3.1,2],
}
continue_option = True
while continue_option:
    user_option = show_menu()
    match user_option:
        case 1:
            run_search(students)
        case 2:
            run_edit(students)
        case 3:
            run_add(students)
        case 4: 
            run_remove(students)
        case 5:
            run_print(students)
    user_input = input("Would you like to do something else?y/n\n")
    if user_input.lower() =='n':
        continue_option = False
print("Thank you for using the students app")