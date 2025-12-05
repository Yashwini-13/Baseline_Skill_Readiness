#  Functions

def calculate_grade(score):
    if score >= 90:
        return "A Grade"
    elif score >= 80:
        return "B Grade"
    elif score >= 70:
        return "C Grade"
    else:
        return "Needs Improvement"


student_score = 85
result = calculate_grade(student_score)# Calling the function

print(f"Student Score: {student_score}")
print(f"Result: {result}")
 