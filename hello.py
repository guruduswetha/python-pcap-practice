
## how many students?

print("how many students are in the class?")
number_of_students = input()
print("the number of students are:", number_of_students)
student_collections = []
Counter = 0
##
for i in range(0, int(number_of_students)):
    ##print(i+1)
    print("Enter the student NAME#" ,i+1)
    student_name = input()
    print("Enter the student SCORE#" ,i+1)
    student_score = input()

    student_details = {
        "student_name": student_name,
        "student_score": student_score,
    
    }
    
    student_collections.append(student_details)
##print(student_collections)

for student in student_collections:
    if int(student["student_score"])>=90:
     
     print(student["student_name"] +" has "+ "Grade: A")

    elif int(student["student_score"])>=80:
     
     print(student["student_name"] +" has "+ "Grade: B")

    elif int(student["student_score"])>=70:
     
     print(student["student_name"] +" has "+ "Grade: C")
    
    elif int(student["student_score"])>=60:
     
     print(student["student_name"] +" has "+ "Grade: D")

    elif int(student["student_score"])<=60:
     Counter += 1
     print(student["student_name"] +" has "+ "Grade: F")

     

avg_score = 0
all_scores = []


for student in student_collections:
    
    avg_score=avg_score+int(student["student_score"])
    ##print(avg_score)
    all_scores.append (int(student["student_score"]))

avg_score = avg_score/len(student_collections)
print("The Average score for all the students is", avg_score)
print("The Highest score the students who got it is",max(all_scores))
print("The failed students are ",Counter)


    

 
# Swetha has a grade B
# Kaveesh has a grade A
# Ganesh has a grade C

# print("=============================")
# The average score
# The highest score and the student who got it
# The number of students who passed (score ≥ 60)
# The number of students who failed (score < 60)
    
##For each student, asks for their name and score (0–100).

##stdents = list []

# for *( start with 0 , until reach to input value ):

#     print("enter $i istudent name")
#     name = input()
#     print("You have entered name is :", name )
#     score


#     stidentdetails = {
#         'name': name,
#         'score': score,
#         'id': id,
#     }

#     stdents.append(stidentdetails)




# stdents.count

