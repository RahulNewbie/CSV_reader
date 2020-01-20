import sqlite3
from sqlite3 import Error
from datetime import datetime


def connect_to_database():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param: None
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(r"C:\Users\Rahul Dutta\PycharmProjects"
                               r"\coding_callenge_2\data_temp5.db")
    except Error as e:
        print(e)
    return conn


def select_all_data_from_table():
    """
    Query all rows in the tasks table
    :param: None
    :return: ALl rows of the table
    """
    conn = connect_to_database()
    cur = conn.cursor()
    # Select All the records from the Database
    cur.execute("SELECT * FROM temp_table")
    rows = cur.fetchall()
    return rows


def select_data_by_id(id):
    """
    Query all rows in the tasks table
    :param conn: ID of the respective row
    :return: Single row corresponding to the ID
    """
    conn = connect_to_database()
    cur = conn.cursor()
    # Update the timestamp into the database
    accessed_time = datetime.now()
    cur.execute("UPDATE temp_table SET last_accessed = ? WHERE id = ?",
                (accessed_time, id,))
    # Get the row corresponding to the id
    cur.execute("SELECT * FROM temp_table WHERE id = ?", (id,))
    row = cur.fetchall()
    return row

