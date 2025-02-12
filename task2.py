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

conn = sqlite3.connect('veterinarian.db')
cursor = conn.cursor()

#set up relationship between customers and pet
cursor.execute('''
CREATE TABLE IF NOT EXISTS pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    species TEXT,
    breed TEXT,
    age INTEGER,
    gender TEXT,
    spayed_neutered BOOLEAN,
    owner_id INTEGER UNIQUE,
    FOREIGN KEY (owner_id) REFERENCES customers (owner_customer_id)
)
''')

cursor.executemany('''
INSERT OR IGNORE INTO pets (name, species, breed, age, gender, spayed_neutered, owner_id)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    ("Fluffy", "dog", "Pomeranian", 5, "m", True, 101),
    ("Benjamin", "cat", "Siberian", 8, "m", True, 103),
    ("Casey", "cat", "Siberian", 8, "m", True, 103),
    ("Friend", "cat", "Domestic", 4, "m", False, 102),
    ("Copper", "dog", "Beagle", 12, "m", True, 104)
])

conn.commit()

cursor.execute("SELECT * FROM pets")
print(cursor.fetchall())


####extra for fun
#print owner pet relation 
cursor.execute('''
SELECT customers.owner_name, pets.name FROM customers
JOIN pets ON customers.owner_customer_id = pets.owner_id
''')
data = cursor.fetchall()

print("\n\nOwner, Pet name")
for i in data:
    print(i)

conn.close()