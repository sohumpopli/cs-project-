def teacher_dashboard(con, teacher_id):

    while True:

        print("\n========================================")
        print("             TEACHER DASHBOARD")
        print("========================================")
        print("1. View My Profile")
        print("2. View All Students")
        print("3. Logout")
        print("========================================")

        choice = input("Enter your choice: ")

        # ==================================
        # 1. VIEW OWN TEACHER PROFILE
        # ==================================

        if choice == "1":

            cursor = con.cursor()

            query = """
            SELECT teacher_id, name, subject, class, email,
                   phone_number, dob, qualification
            FROM teachers
            WHERE teacher_id = %s
            """

            cursor.execute(query, (teacher_id,))
            teacher = cursor.fetchone()

            cursor.close()

            if teacher:

                print("\n========== MY PROFILE ==========")
                print("Teacher ID   :", teacher[0])
                print("Name         :", teacher[1])
                print("Subject      :", teacher[2])
                print("Class        :", teacher[3])
                print("Email        :", teacher[4])
                print("Phone Number :", teacher[5])
                print("DOB          :", teacher[6])
                print("Qualification:", teacher[7])
                print("================================")


        elif choice == "2":

            cursor = con.cursor()

            query = """
            SELECT student_id, name, attendance, transport
            FROM students"""

            cursor.execute(query)
            students = cursor.fetchall()

            cursor.close()

            print("\n========== STUDENT RECORDS ==========")

            if students:

                for student in students:

                    print("\nStudent ID :", student[0])
                    print("Name       :", student[1])
                    print("Attendance :", student[2], "%")
                    print("Transport  :", student[3])
                    print("------------------------------------")

            else:

                print("No student records found.")

        elif choice == "3":

            print("\nLogging out of Teacher Dashboard...")
            break

        else:

            print("\nInvalid choice. Please try again.")
