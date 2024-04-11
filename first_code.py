def main():
    # import the module
    import sqlite3
    try:
        # make a  connection object
        connection_obj = sqlite3.connect('project.db')

        # make a cursor object
        cursor_obj = connection_obj.cursor()

        # creating tables if it doesn't exit
        students_table = """ CREATE TABLE STUDENTS
                            (StudentID AUTOINCREMENT primary key,
                            FirstName varchar(20),
                            LastName varchar(30)) if not exists ;"""
        grades_table = """ CREATE TABLE GRADES 
                            (StudentID foreign key,
                            Midterm number,
                            Final number,
                            HomeworkAverage number) if not exists ;"""
        cursor_obj.execute(students_table)
        cursor_obj.execute(grades_table)
    except Exception as e:
        print(e.message)

    connection_obj.close()

if __name__ == "__main__":
    main()
