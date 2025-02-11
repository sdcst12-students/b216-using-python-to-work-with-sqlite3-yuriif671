#!python

"""
Create a query to create a table to store pets information into a database for a veterinarian
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (dog, cat)
pet breed (collie, beagle, persian, etc)
pet age
pet gender
pet neutered or spayed
owner ID

choose appropriate variable types for each field
create the database and add the following information. Make sure you commit the information to save it:
name            species         breed           age  gender     spayed/neutered?    ownerID
Fluffy          dog             Pomeraniam      5    m          true                101
Benjamin        cat             Siberian        8    m          true                103
Casey           cat             Siberian        8    m          true                103
Friend          cat             Domestic        4    m          false               102
Copper          dog             Beagle          12   m          true                104
"""

import sqlite3

conn = sqlite3.connect('sigma.db')

cur = conn.cursor()

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS pets (
    name TEXT,
    species TEXT,
    breed TEXT,
    age INTEGER,
    gender TEXT,
    neutered BOOL,
    ownerID INTEGER
    );
''')

cur.execute(
    '''
    INSERT OR IGNORE INTO pets 
    (name, species, breed, age, gender, neutered, ownerID) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''',
    ('Fluffy', 'dog', 'Pomeraniam', 5, 'm', True, 101)
)

cur.execute(
    '''
    INSERT OR IGNORE INTO pets 
    (name, species, breed, age, gender, neutered, ownerID) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''',
    ('Benjamin', 'cat', 'Siberian', 8, 'm', True, 103)
)

cur.execute(
    '''
    INSERT OR IGNORE INTO pets 
    (name, species, breed, age, gender, neutered, ownerID) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''',
    ('Casey', 'cat', 'Siberian', 8, 'm', True, 103)
)

cur.execute(
    '''
    INSERT OR IGNORE INTO pets 
    (name, species, breed, age, gender, neutered, ownerID) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''',
    ('Friend', 'cat', 'Domestic', 4, 'm', False, 102)
)

conn.commit()

cur.execute("SELECT * FROM pets")
print(cur.fetchall())

# Close the connection
conn.close()