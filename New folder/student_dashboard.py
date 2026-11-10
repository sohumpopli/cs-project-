def student_dashboard(con, student_id):

    while True:

        print("\n========================================")
        print("             STUDENT DASHBOARD")
        print("========================================")
        print("1. View My Profile")
        print("2. My Grades")
        print("3. Logout")
        
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            cursor = con.cursor()

            query = """
            SELECT student_id, name, attendance , transport
            FROM students
            WHERE student_id = %s
            """

            cursor.execute(query, (student_id,))
            student = cursor.fetchone()

            cursor.close()

            if student:

                print("\n========== MY PROFILE ==========")
                print("Student ID :", student[0])
                print("Name       :", student[1])
                print("Attendance :", str(student[2]) + "%")
                print("Transport  :", student[3])
                print("================================")
        

        elif choice == "2":
            cursor = con.cursor()

            query = """
    SELECT subject, marks, maximum_marks
    FROM grades
    WHERE student_id = %s
    """

            cursor.execute(query, (student_id,))
            grades = cursor.fetchall()

            print("\n========== MY GRADES ==========")

            if grades:

                total_marks = 0
                total_maximum = 0

                for grade in grades:

                    print("\nSubject:", grade[0])
                    print("Marks:", grade[1], "/", grade[2])

                    total_marks += grade[1]
                    total_maximum += grade[2]

                percentage = (total_marks / total_maximum) * 100

                print("\n-------------------------------")
                print("Total Marks:", total_marks, "/", total_maximum)
                print("Percentage:", round(percentage, 2), "%")
                print("================================")

            else:
                print("No grades available.")
            cursor.close()
        
        elif choice == "3":

            print("\nLogging out...")
            break

        else:

            print("\nInvalid choice. Please try again.")
    