userName = (input("Enter your name: "))
score = 0
allSubject = {}


while True:
    subject = input("Enter the subject (press q to quit): ").lower()
    
    if subject == "q":
        break
        
    grade = input("Enter the grade (press q to quit): ").lower()
    if grade == "q":
         break

    if grade == "" or subject == "":
        print("Invalid")
    else:
        allSubject[subject] = grade
print(f"Your Name is {userName}")
print("All of your Subject and grade")
for subject, grade in allSubject.items():
    print(f"{subject.capitalize()}: {grade.upper()}")



