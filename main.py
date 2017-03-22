# A menu-driven main.py file accepting the module name and displaying it
pmName = raw_input("Enter module name:\n 1:Enter battleship for 'battleship.py'\n 2:Enter student_to_teacher for 'students_to_teacher.py'\n 3:Enter exam_stats for 'exam_stats.py'\n")
__import__(pmName)
