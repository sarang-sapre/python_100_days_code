student_numbers = input("Students numbers : ").split()

for n in range(0,len(student_numbers)) :
    student_numbers[n] = int(student_numbers[n])

max_marks = 0

for i in student_numbers :
    if(max_marks < i):
        max_marks = i

print(f"The highest marks are :{max_marks} ")