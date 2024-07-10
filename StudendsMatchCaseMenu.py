students = {}


def add_student(name):
    match name in students:
        case False:
            students[name] = []
            print(f"Student {name} added.")
        case True:
            print(f"Student {name} already exists.")


def add_grade(name, grade):
    match name in students:
        case True:
            students[name].append(grade)
            print(f"Grade {grade} added for {name}.")
        case False:
            print(f"Student {name} does not exist.")


def calculate_average(name):
    match name in students:
        case True:
            grades = students[name]
            match bool(grades):
                case True:
                    average = sum(grades) / len(grades)
                    print(f"Average grade for {name} is {average:.2f}.")
                    return average
                case False:
                    print(f"No grades available for {name}.")
                    return None
        case False:
            print(f"Student {name} does not exist.")
            return None


def display_students():
    match bool(students):
        case True:
            for name, grades in students.items():
                print(f"Student: {name}, Grades: {grades}")
        case False:
            print("No students available.")


def remove_student(name):
    match name in students:
        case True:
            del students[name]
            print(f"Student {name} removed.")
        case False:
            print(f"Student {name} does not exist.")


def update_grade(name, old_grade, new_grade):
    match name in students:
        case True:
            try:
                index = students[name].index(old_grade)
                students[name][index] = new_grade
                print(f"Grade {old_grade} updated to {new_grade} for {name}.")
            except ValueError:
                print(f"Grade {old_grade} not found for {name}.")
        case False:
            print(f"Student {name} does not exist.")


def get_highest_grade(name):
    match name in students:
        case True:
            grades = students[name]
            match bool(grades):
                case True:
                    highest_grade = max(grades)
                    print(f"Highest grade for {name} is {highest_grade}.")
                    return highest_grade
                case False:
                    print(f"No grades available for {name}.")
                    return None
        case False:
            print(f"Student {name} does not exist.")
            return None


def save_data(filename='data/students_data.txt'):
    try:
        with open(filename, 'w') as file:
            for name, grades in students.items():
                grades_str = ','.join(map(str, grades))
                file.write(f"{name}:{grades_str}\n")
        print(f"Data saved to {filename}.")
    except FileNotFoundError:
        print(f"Directory 'data' does not exist. Creating the directory.")
        import os
        os.makedirs(os.path.dirname(filename))
        save_data(filename)


def load_data(filename='data/students_data.txt'):
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, grades_str = line.strip().split(':')
                grades = list(map(int, grades_str.split(',')))
                students[name] = grades
        print(f"Data loaded from {filename}.")
    except FileNotFoundError:
        print(f"File {filename} does not exist. No data loaded.")


def main():
    while True:
        print("\nStudent Grades Management System")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Calculate the average grade for a student")
        print("4. Display all students and their grades")
        print("5. Remove a student")
        print("6. Update a student's grade")
        print("7. Get a student's highest grade")
        print("8. Save student data to a file")
        print("9. Load student data from a file")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the student's name: ")
            add_student(name)
        elif choice == '2':
            name = input("Enter the student's name: ")
            grade = float(input("Enter the grade: "))
            add_grade(name, grade)
        elif choice == '3':
            name = input("Enter the student's name: ")
            calculate_average(name)
        elif choice == '4':
            display_students()
        elif choice == '5':
            name = input("Enter the student's name: ")
            remove_student(name)
        elif choice == '6':
            name = input("Enter the student's name: ")
            old_grade = float(input("Enter the old grade: "))
            new_grade = float(input("Enter the new grade: "))
            update_grade(name, old_grade, new_grade)
        elif choice == '7':
            name = input("Enter the student's name: ")
            get_highest_grade(name)
        elif choice == '8':
            filename = input("Enter the filename to save to: ")
            save_data(filename)
        elif choice == '9':
            filename = input("Enter the filename to load from: ")
            load_data(filename)
        elif choice == '10':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
