import csv
import sqlite3


def transfer_csv_to_memory():
    """
    Read the CSV file and insert records in Database
    """
    con = sqlite3.connect(r"C:\Users\Rahul Dutta\PycharmProjects"
                          r"\coding_callenge_2\data_temp5.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE temp_table (id,timestamp,temperature,"
                "duration,last_accessed);")
    with open('task_data.csv', 'rt') as fin:
        # csv.DictReader read line by line
        dr = csv.DictReader(fin)
        to_db = [(i['id'], i['timestamp'], i['temperature'],
                  i['duration']) for i in dr]

    cur.executemany("INSERT INTO temp_table "
                    "(id,timestamp,temperature,duration) "
                    "VALUES (?, ?, ?, ?);", to_db)
    print("database insertion finished")
    con.commit()
    con.close()


if __name__ == "__main__":
    transfer_csv_to_memory()
