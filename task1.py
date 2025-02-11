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

conn = sqlite3.connect('sigma.db')

cur = conn.cursor()

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS clinic (
    name TEXT,
    email TEXT UNIQUE,
    phone_number INTEGER UNIQUE,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    adress TEXT,
    balance INTEGER
    );
''')

cur.execute(
    '''
    INSERT OR IGNORE INTO clinic 
    (name, email, phone_number, id, adress, balance) VALUES (?, ?, ?, ?, ?, ?)
    ''',
    ('Joe Smith', 'joe@gmail.com', 7783341111, 101, '1234 Sesame Street', 0)
)

cur.execute(
    '''
    INSERT OR IGNORE INTO clinic 
    (name, email, phone_number, id, adress, balance) VALUES (?, ?, ?, ?, ?, ?)
    ''',
    ('Fred Jones', 'fred@city.com', 6045553434, 102, '75 57 Street', 0)
)

cur.execute(
    '''
    INSERT OR IGNORE INTO clinic 
    (name, email, phone_number, id, adress, balance) VALUES (?, ?, ?, ?, ?, ?)
    ''',
    ('Leroy Jenkins', 'leroy@wow.ca', 2342222323, 103, '65 Blizzard Ave', 100)
)

cur.execute(
    '''
    INSERT OR IGNORE INTO clinic 
    (name, email, phone_number, id, adress, balance) VALUES (?, ?, ?, ?, ?, ?)
    ''',
    ('Jen Mezei', 'jen@shaw.ca', 6042231134, 104, '891 Cullen Cresc', 0)
)

conn.commit()

cur.execute("SELECT * FROM clinic")
print(cur.fetchall())

# Close the connection
conn.close()