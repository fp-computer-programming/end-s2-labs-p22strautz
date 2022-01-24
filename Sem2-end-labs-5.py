# Author: SCT (AMDG) 1/24/12
# "Student's Final Grade"

def final_grade(exam, projects): # Defining function
  if exam > 90 or  projects > 10: return 100 # if exam is greater than 90 and project greater than 10 final score is 100
  if exam > 75 and projects >= 5: return 90 # if exam is greater than 75 and project greater than 5 final score is 90
  if exam > 50 and projects >= 2: return 75 # if exam is greater than 50 and project greater than 2 final score is 75
  return 0

# Test Cases
print(final_grade(100, 12))
print(final_grade(90, 8))
print(final_grade(75, 6))