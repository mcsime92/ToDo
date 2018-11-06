# TO DO program. Task, deadline, category, status
# Add GUI and format to make a package
import sqlite3

database_name = 'todo_list.db'
connection = sqlite3.connect(database_name)
cursor = connection.cursor()


def database_creation():
    sql_command = ('CREATE TABLE IF NOT EXISTS todolist (\n'
                   '                    rowID INTEGER PRIMARY KEY,\n'
                   '                    task_name TEXT,\n'
                   '                    task_category TEXT,\n'
                   '                    deadline DATETIME,\n'
                   '                    status);')
    cursor.execute(sql_command)


def enter_new_entry():
    input_task_name = input('> Task name ')
    input_task_category = input('> Task category ')
    input_task_deadline = input('> Task deadline, if any (DD/MM/YYYY) ')
    input_task_status = "Not started"

    sql_command = 'INSERT INTO todolist VALUES (NULL, ?, ?, ?, ?);'
    cursor.execute(sql_command,
                   (input_task_name, input_task_category, input_task_deadline, input_task_status))
    connection.commit()

def print_test():
    print('test')

def delete_table():
    sql_command = 'DELETE FROM todolist;'
    cursor.execute(sql_command)
    connection.commit()


def drop_table():
    sql_command = 'DROP TABLE todolist;'
    cursor.execute(sql_command)
    connection.commit()


def print_db():
    cursor.execute('SELECT * FROM todolist')
    ans = cursor.fetchall()
    for i in ans:
        print(i)


database_creation()
#enter_new_entry()
cursor.close()
