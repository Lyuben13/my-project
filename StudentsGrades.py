students = {}


def add_student(name):
    if name not in students:
        students[name] = []
        print(f"Student {name} added.")
    else:
        print(f"Student {name} already exists.")


def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
        print(f"Grade {grade} added for {name}.")
    else:
        print(f"Student {name} does not exist.")


def calculate_average(name):
    if name in students:
        grades = students[name]
        if grades:
            average = sum(grades) / len(grades)
            print(f"Average grade for {name} is {average:.2f}.")
            return average
        else:
            print(f"No grades available for {name}.")
            return None
    else:
        print(f"Student {name} does not exist.")
        return None


def display_students():
    if students:
        for name, grades in students.items():
            print(f"Student: {name}, Grades: {grades}")
    else:
        print("No students available.")


def remove_student(name):
    if name in students:
        del students[name]
        print(f"Student {name} removed.")
    else:
        print(f"Student {name} does not exist.")


def update_grade(name, old_grade, new_grade):
    if name in students:
        try:
            index = students[name].index(old_grade)
            students[name][index] = new_grade
            print(f"Grade {old_grade} updated to {new_grade} for {name}.")
        except ValueError:
            print(f"Grade {old_grade} not found for {name}.")
    else:
        print(f"Student {name} does not exist.")


def get_highest_grade(name):
    if name in students:
        grades = students[name]
        if grades:
            highest_grade = max(grades)
            print(f"Highest grade for {name} is {highest_grade}.")
            return highest_grade
        else:
            print(f"No grades available for {name}.")
            return None
    else:
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


# Example usage
add_student("Alice")
add_grade("Alice", 90)
add_grade("Alice", 80)
calculate_average("Alice")
display_students()
remove_student("Alice")
display_students()
