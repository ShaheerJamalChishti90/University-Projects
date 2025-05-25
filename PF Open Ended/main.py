def add_grades(student_name, *grades):
    print(f"\nAdding grades for {student_name}...")
    return list(grades) 

def calculate_average(grades, rounding=True):
    if len(grades) == 0:
        return 0
    avg = sum(grades) / len(grades) 
    if rounding:
        return round(avg, 2)
    return avg


def get_result(average, passing_mark=40): 
    if average >= passing_mark:
        return "Passed"
    else:
        return "Failed"

def display_student_info(**kwargs):
    print("\n--- Student Info ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main():
    print("=== Student Grade Management System ===\n")
    
    name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))
    
    grades = []
    while True:
        try:
            grade_input = input("Enter marks (or type 'done' to finish): ")
            if grade_input.lower() == 'done':
                break
            grade = float(grade_input)
            if 0 <= grade <= 100: #0(fail) < grade(pass) <= 100 
                grades.append(grade)
            else:
                print("Please enter a grade between 0 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    
    student_grades = add_grades(name, *grades)
    average = calculate_average(student_grades)
    result = get_result(average)

    print("\nProcessing Grades...\n")
    print("Raw Grades:", student_grades)
    print("Average Grade:", average)
    print("Result:", result)

    # Nested loop - printing detailed grade breakdown
    print("\nGrade Details:")
    for i in range(len(student_grades)):
        print(f"Subject {i+1}:", end=" ")
        for j in range(int(student_grades[i]) // 10): 
            print("*", end="")
        print(f" ({student_grades[i]})")

    student_data = {
        "Name": name,
        "Roll Number": roll_no,
        "Grades": student_grades,
        "Average": average,
        "Result": result
    }
    display_student_info(**student_data)
    
if __name__ == "__main__":
    main()