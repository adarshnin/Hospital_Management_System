import sqlite3
import json
with open('config.json') as data_file:
    config = json.load(data_file)

conn=sqlite3.connect(config['database'], check_same_thread=False)
conn.execute('pragma foreign_keys=ON')



def dict_factory(cursor, row):
    """This is a function use to format the json when retirve from the  mysql database"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn.row_factory = dict_factory

conn.execute('''CREATE TABLE if not exists patient
(pat_id INTEGER PRIMARY KEY AUTOINCREMENT,
pat_first_name TEXT NOT NULL,
pat_last_name TEXT NOT NULL,
pat_insurance_no TEXT NOT NULL,
pat_ph_no TEXT NOT NULL,
pat_date DATE DEFAULT (datetime('now','localtime')),
pat_address TEXT NOT NULL);''')

conn.execute('''CREATE TABLE if not exists doctor
(doc_id INTEGER PRIMARY KEY AUTOINCREMENT,
doc_first_name TEXT NOT NULL,
doc_last_name TEXT NOT NULL,
doc_ph_no TEXT NOT NULL,
doc_date DATE DEFAULT (datetime('now','localtime')),
doc_address TEXT NOT NULL);''')

conn.execute('''CREATE TABLE if not exists nurse
(nur_id INTEGER PRIMARY KEY AUTOINCREMENT,
nur_first_name TEXT NOT NULL,
nur_last_name TEXT NOT NULL,
nur_ph_no TEXT NOT NULL,
nur_date DATE DEFAULT (datetime('now','localtime')),
nur_address TEXT NOT NULL);''')

conn.execute('''CREATE TABLE if not exists appointment
(app_id INTEGER PRIMARY KEY AUTOINCREMENT,
pat_id INTEGER NOT NULL,
doc_id INTEGER NOT NULL,
appointment_date DATE NOT NULL,
FOREIGN KEY(pat_id) REFERENCES patient(pat_id),
FOREIGN KEY(doc_id) REFERENCES doctor(doc_id));''')

conn.execute('''CREATE TABLE if not exists room
(room_no INTEGER PRIMARY KEY,
room_type TEXT NOT NULL,
available INTEGER NOT NULL);''')

conn.execute('''CREATE TABLE if not exists medication
(code INTEGER PRIMARY KEY,
name TEXT NOT NULL,
brand TEXT NOT NULL,
description TEXT);''')

conn.execute('''CREATE TABLE if not exists department
(department_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
head_id INTEGER NOT NULL,
FOREIGN KEY(head_id) REFERENCES doctor(doc_id));''')

conn.execute('''CREATE TABLE if not exists procedure
(code integer PRIMARY KEY,
name TEXT NOT NULL,
cost INTEGER NOT NULL);''')

conn.execute('''CREATE TABLE if not exists undergoes
(pat_id INTEGER NOT NULL,
proc_code INTEGER NOT NULL,
u_date DATE NOT NULL,
doc_id INTEGER,
nur_id INTEGER,
room_no INTEGER,
PRIMARY KEY(pat_id, proc_code, u_date),
FOREIGN KEY(pat_id) REFERENCES patient(pat_id),
FOREIGN KEY(proc_code) REFERENCES procedure(code),
FOREIGN KEY(doc_id) REFERENCES doctor(doc_id),
FOREIGN KEY(nur_id) REFERENCES nurse(nur_id),
FOREIGN KEY(room_no) REFERENCES room(room_no));''')

conn.execute('''CREATE TABLE if not exists prescribes
(doc_id INTEGER,
pat_id INTEGER,
med_code INTEGER,
p_date DATE NOT NULL,
app_id INTEGER NOT NULL,
dose INTEGER NOT NULL,
PRIMARY KEY(doc_id, pat_id, med_code, p_date),
FOREIGN KEY(doc_id) REFERENCES doctor(doc_id),
FOREIGN KEY(pat_id) REFERENCES patient(pat_id),
FOREIGN KEY(med_code) REFERENCES medication(code),
FOREIGN KEY(app_id) REFERENCES appointment(app_id));''')