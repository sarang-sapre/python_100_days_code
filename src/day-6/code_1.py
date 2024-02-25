student_height = input("Students height : ").split()

for n in range(0,len(student_height)) :
    student_height[n] = int(student_height[n])

total_height = 0


for i in student_height :
    total_height = total_height + i


print(f"total_height : {total_height}\n")
print(f"number of student : {len(student_height)}\n")
print(f"average Height : {round(total_height/len(student_height),2)}")
