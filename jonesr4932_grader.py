## Reginald Jones
## Jonesr4932_Grader
## 08/29/2018
## This Program runs the import statements
##

import jonesr4932_grade_functions as grade
# main function that will do all of the functions calls
def main():
# function call and return # of grades to enter
    num = grade.get_input()
# function call and return average
    average = grade.get_average(num)
# function call and return letter grade
    letter_grade = grade.get_letter_grade(average)
# function call to print letter grade
    grade.display_grade(average,letter_grade)

# main function call; basically where program starts

if __name__ == "__main__":
    main()
