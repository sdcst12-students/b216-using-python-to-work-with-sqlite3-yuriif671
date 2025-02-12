#!python

"""
Create a query to create a table to store customers information into a database for a veterinarian
Each record needs to have the following information:
id unique integer identifier
owner name
owner email
owner phone number
owner customer identification number
owner address
owner balance owing

choose appropriate variable types for each field
create the database and add the following information. Make sure you commit the information to save it:
name            email           phone number    ID      address                 balance
Joe Smith       joe@gmail.com   7783341111      101     1234 Sesame Street      0
Fred Jones      fred@city.com   6045553434      102     75 57 Street            0
Leroy Jenkins   leroy@wow.ca    2342222323      103     65 Blizzard Ave         100     
Jen Mezei       jen@shaw.ca     6042231134      104     891 Cullen Cresc        0
"""

import sqlite3

conn = sqlite3.connect("veterinarian.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    owner_name TEXT,
    owner_email TEXT UNIQUE,
    owner_phone TEXT,
    owner_customer_id INTEGER UNIQUE,
    owner_address TEXT,
    owner_balance REAL
)
''')

#put it all in one go with executemany
cursor.executemany('''
INSERT OR IGNORE INTO customers (owner_name, owner_email, owner_phone, owner_customer_id, owner_address, owner_balance)
VALUES (?, ?, ?, ?, ?, ?)
''', [
    ("Joe Smith", "joe@gmail.com", "7783341111", 101, "1234 Sesame Street", 0),
    ("Fred Jones", "fred@city.com", "6045553434", 102, "75 57 Street", 0),
    ("Leroy Jenkins", "leroy@wow.ca", "2342222323", 103, "65 Blizzard Ave", 100),
    ("Jen Mezei", "jen@shaw.ca", "6042231134", 104, "891 Cullen Cresc", 0)
])

conn.commit()

cursor.execute("SELECT * FROM customers")
print(cursor.fetchall())

conn.close()