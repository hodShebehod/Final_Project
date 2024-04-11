def main():
    # import the module
    import sqlite3
    print(sqlite3.version)
    try:
        # make a  connection object
        connection_obj = sqlite3.connect('project.db')

        # make a cursor object
        cursor_obj = connection_obj.cursor()

        # creating tables if it doesn't exit
        students_table = """ CREATE TABLE if not exists STUDENTS
                            (StudentID identity primary key,
                            FirstName varchar(20),
                            LastName varchar(30));"""
        grades_table = """ CREATE TABLE  if not exists GRADES 
                            (StudentID integer primary key,
                            Midterm number,
                            Final number,
                            HomeworkAverage number,
                            FOREIGN KEY (StudentID) REFERENCES students(studentid));"""
        cursor_obj.execute(students_table)
        cursor_obj.execute(grades_table)
    except Exception as e:
        print(e.message)
    '''this is the place to call the methods if the buttons are pressed'''
    # close the object at the end
    connection_obj.close()

def create():
    '''execute code to create a new record in the student table and also grades table'''
    # create a new student into student table
    create_new_student = """ INSERT INTO students values(, [Enter first name], [Enter last name])"""
    cursor_obj.execute(create_new_student)

def read():
    '''execute code to show table of students and names and grades and average'''
    # show a list of students and their average grades
    read_tables = """ SELECT * FROM students and average FROM grades"""
    cursor_obj.execute(read_tables)

def update():
    '''execute code to enable editing to students grade'''

def update():
    '''execute code to delete a record'''

if __name__ == "__main__":
    main()
