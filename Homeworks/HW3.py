# HW 4 - Class Grade Application
print("******* Passing Grade Calculator *******")


list =[]
for i in range(1,6):
    student= input("Please enter name of the student: ")
    mt, project, final = [float(x) for x in input("Please enter corresponding student's mt, project and final grades: ").split()]
    grade= float(mt*0.3 + project*0.3 + final*0.4)
    dict = {"Name" : student ,
            "Midterm": mt,
            "Project": project,
            "Final": final,
            "Grade": grade}
    list.append(dict)
def get_grade(student):     # to select the Grade from the dictionary
    return student.get("Grade")
list.sort(key = get_grade, reverse = True ) # sort the list in descending order

print(list)


