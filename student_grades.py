# David Wylie
# PA 8
# This program allows a user to search a dictionary by name or grade and get a result.

# This is the base dictionary.
student_dict = {
    "Dylan Sprouse": "D",
    "Abigail Spencer": "C",
    "Daniel Kim": "B",
    "Lauren Tom": "A",
    "Michael DeLuise": "F",
    "Pedro Pascal": "B",
    "Paulina Garcia": "A",
    "Paulina Gaitan": "C",
    "Gemma Chan": "C",
    "Carmen Soo": "B"
}

# An empty list to store student names for grade search
grade_list = []

# Creating our search variables
search_option = ""
student_search = ""
grade_search = ""

# A list for valid search options.
valid_options = ["N", "G"]  # No error checking for case. Only N or G can be entered.

# Get user's search choice, guides to a valid response with while loop
while search_option not in valid_options:
    search_option = str(input("Would you like to search by name (N) or grade (G): "))
    if search_option not in valid_options:  # This is to check for bogus input.
        print("You must enter an N or G.")

# Code to execute the name search part.
if search_option == "N":  # Condition check for name search
    student_search = str(input("Enter the students name to search for: ").title())  # Title function to match dictionary
    if student_search in student_dict:  # Check the student dictionary for the input and display grade.
        for student, grade in student_dict.items():
            if student_search == student:
                print(f"\n{student}'s grade is {grade}.")
    else:
        print("The student's name entered does not exist.")

# Code to execute the grade search part.
else:  # While loop prevents anything other than N or G to be entered.
    grade_search = str(input("Enter the grade to search for (A,B,C,D,F): "))  # No error checking per assignment
    for student_name, student_grade in student_dict.items():  # Find students with the given grade
        if student_grade == grade_search:  # If they have the grade, populate name on grade list.
            grade_list.append(student_name)
    if grade_list:  # Check if there are names entered into grade set list, empty list catches odd input.
        print(
            f"\nThe following students received a grade of {grade_search}:")  # Display students with the searched grade.
        for student_name in grade_list:
            print(student_name)
        print(f"\n{len(grade_list)} students received the grade entered.")
    else:
        print("No students received the grade entered.")
