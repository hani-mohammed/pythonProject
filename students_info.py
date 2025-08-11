from util import *

students ={
    #1234: [1234, "Sam", 3.4, 3],
    #3321: [3321, "Sara", 4.0, 1]
}
continue_option = True
while continue_option:
    show_menu()
    user_input = input("Would you like to do something else?y/n\n")
    if user_input.lower() =='n':
        continue_option = False
print("Thank you for using the students app")