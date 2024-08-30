def grade_of_student(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
print(grade_of_student(95)) 
print(grade_of_student(82))  
print(grade_of_student(76))  
print(grade_of_student(61)) 
print(grade_of_student(50))  
