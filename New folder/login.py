
from connect import connect_database
from student_dashboard import student_dashboard
from teachers_dashboard import teacher_dashboard


def student_login(con):

    print("\n========== STUDENT LOGIN ==========")

    student_id = input("Enter Student ID: ")
    password = input("Enter Password: ")

    cursor = con.cursor()

    query = """
    SELECT student_id, name
    FROM students
    WHERE student_id = %s AND password = %s
    """

    cursor.execute(query, (student_id, password))
    student = cursor.fetchone()

    cursor.close()

    if student:

        print("\nLogin Successful!")
        print("Welcome", student[1])

        student_dashboard(con, student[0])

    else:

        print("\nInvalid Student ID or Password.")


def teacher_login(con):

    print("\n========== TEACHER LOGIN ==========")

    teacher_id = input("Enter Teacher ID: ")
    password = input("Enter Password: ")

    cursor = con.cursor()

    query = """
    SELECT teacher_id, name
    FROM teachers
    WHERE teacher_id = %s AND password = %s
    """

    cursor.execute(query, (teacher_id, password))
    teacher = cursor.fetchone()

    cursor.close()

    if teacher:

        print("\nLogin Successful!")
        print("Welcome", teacher[1])

        teacher_dashboard(con, teacher[0])

    else:

        print("\nInvalid Teacher ID or Password.")


def main():

    con = connect_database()

    if con is None:
        return

    while True:

        print("\n========================================")
        print("     SCHOOL DATABASE MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Student Login")
        print("2. Teacher Login")
        print("3. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            student_login(con)

        elif choice == "2":

            teacher_login(con)

        elif choice == "3":

            print("\nThank you for using the system!")
            break

        else:

            print("\nInvalid choice. Please try again.")

    con.close()


main()
