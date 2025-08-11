def show_menu():
    print("What would you like to do today?")
    print("-Find a student? 1")
    print("-Edit a student info? 2")
    print("-Add a student? 3")
    print("-Remove a student? 4")
    print("-print the students list? 5")
    return int(input(""))

def run_search(students):
    print("Searching")

def run_edit(students):
    print("Editing")

def run_add(students):
    print("Adding")

def run_remove(students):
    id = int(input("Please Enter user id:\n"))
    del students[id]
    return 

def run_print(students):
    print(students)