import csv
import sqlite3


def transfer_csv_to_memory():
    con = sqlite3.connect(r"C:\Users\Rahul Dutta\PycharmProjects\coding_callenge_2\data_temp2.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE temp_table (id,timestamp,temperature,duration,last_accessed);")
    with open('task_data.csv', 'rt') as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i['id'], i['timestamp'], i['temperature'], i['duration']) for i in dr]

    cur.executemany("INSERT INTO temp_table (id,timestamp,temperature,duration) VALUES (?, ?, ?, ?);", to_db)
    print("Done")
    con.commit()
    con.close()


if __name__ == "__main__":
    transfer_csv_to_memory()
