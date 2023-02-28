# sql-язык структур. данных
# субд - система управлениями баз данных
# CRUD - create reed update delete
# noSQL


import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def reed_student(conn):
    try:
        sql=''' SELECT * FROM student'''
        cursor=conn.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()
        # print(rows)
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def create_student(conn, student):
    sql = '''INSERT INTO student(fullname,mark,hobby,is_married)
     VALUES (?,?,?,?)
     '''
    try:
        cursor=conn.cursor()
        cursor.execute(sql,student)
        conn.commit()
    except Error as e:
        print(e)


database = r'tesla.db'

sql_create_student_table = '''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR (54) NOT NULL,
mark DOUBLE (5,2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
is_married BOOLEAN DEFAULT FALSE
);                                                                                                                    
'''

def sql_delete_query(conn):
    cursor = conn.cursor()
    cursor.execute(
        """DELETE from student where id = 4"""
    )
    conn.commit()

def sql_change_query(conn):
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE student SET fullname = 'Begaiym' WHERE id  = 1"""
    )
    conn.commit()



connection = create_connection(database)
if connection is not None:
    # create_table(connection,sql_create_student_table)
    # create_student(connection,('Beka',0,'пишу стихи',0))
    # create_student(connection,('ЭЭрик',110,'барабанщик',1))
    reed_student(connection)
    sql_delete_query(connection)
    sql_change_query(connection)

    print('мы молодцы')
