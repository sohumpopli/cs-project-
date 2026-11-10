import mysql.connector


def connect_database():

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2009",
            database="school"
        )

        return con

    except mysql.connector.Error as e:

        print("Unable to connect to MySQL.")
        print("Error:", e)

        return None
connect_database()