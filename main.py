print "Which script do you want to run? :"
print "1. Enter 1 for Student becomes Teacher."
print "2. Enter 2 for Battleship."
print "3. Enter 3 for Exam Statistics."

choice = int(raw_input("Enter the script number you want to run : "))

if choice==1 :
    #Imports students_to_teacher.py
    import students_to_teacher
elif choice==2 :
    #Imports battleship.py
    import battleship
elif choice==3 :
    #Imports exam_stats.py
    import exam_stats