#Mark sheet generator
name= input("Enter your name: ")
roll_number=int(input("Enter your roll number: "))
marks=[]
for i in range(5):
    subject_marks=int(input(f"Enter your marks{i+1}: "))
    marks.append(subject_marks)

    total=sum(marks)
    average=total/5


    if average>=90:
        print("You got an A+!\n Thats amazing!!")
    elif average>=80:
        print("You got an A\n Well done!")
    elif average>=70:
        print("You got a B+\n Good Job!")
    elif average>=60:
        print("You got a B\n Nice work!")
    elif average>=50:
        print("You got a C+\n Can do slightly better!")
    elif average>=40:
        print("You got a C\n You can do more better next time!")
    else:
        print("You have Failed this class!\n Better luck next time!")

    print(f"Your total is : {total}")
    print(f"Your average is : {average}")

    print("-------Mark sheet generator-------")
    print(f"Your name is : {name}")
    print(f"You roll number is : {roll_number}")
    print(f"Your total is : {total}")
    print(f"Your average is : {average}")
    print("-----------------------------------")

    

