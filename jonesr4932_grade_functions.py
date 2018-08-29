## Reginald Jones
## Jonesr4932_Grader
## 08/29/2018
## This Program runs the functions for the average
##

#Get the input from the user
def get_input():
    num = int(input("How many grades do you want to input? "))
    return num

#Function call and Return average
def get_average(num):
    total = 0
    for x in range (num):
        grade = float(input("Enter a grade "))
        total = grade + total
        
    average = total / num
    return average

#Get the letter grade from the average    
def get_letter_grade(ave):

    if ave >= 90:
        grade = "A"
    elif ave >= 80:
        grade = "B"
    elif ave >= 70:
        grade = "C"
    elif ave >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

#Display Average and letter grade
def display_grade(ave,grade):
    
    print("Your average is ", ave, " which is a letter grade of ", grade)

if __name__ == "__main__":
    main()
