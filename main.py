# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
print(len(students))

print(students[0]["Combo,Name"])
print(students[0]["Email"][0])
print(students[0]["Email"][1])
print(students[0]["CPSID"])

print(students[1]["Combo,Name"])
print(students[1]["Email"][1])
print(students[1]["CPSID"])

print(students[2]["Combo,Name"])
print(students[2]["Email"][1])
print(students[2]["CPSID"])

#forloops allow us to iterate thwe data and perform some functions
for students in students:
  print(students["Combo,Name"])
  print(students["Email"][0])
  print(students["Email"][1])
  print(students["CPSID"])
  
  print("_" * 25)

