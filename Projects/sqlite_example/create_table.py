import sqlite3
from datetime import datetime

# Connect to the SQLite database file
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a new table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS takeoBootcampTable (
        "User ID Number" INTEGER,
        "Name" TEXT,
        "Cell Phone Number" TEXT,
        "Email" TEXT,
        "Address" TEXT,
        entry_datetime DATETIME
    )
''')

print('')
# Prompt the user to input values for the sample entry
user_id = int(input("Enter User ID Number: "))
name = input("Enter Name: ")
phone = input("Enter Cell Phone Number: ")
email = input("Enter Email: ")
address = input("Enter Address: ")
entry_datetime = datetime.now()
print('')

# Create a tuple with the input values
sample_entry = (
    user_id,
    name,
    phone,
    email,
    address,
    entry_datetime
)

# Insert the sample entry into the table
cursor.execute('INSERT INTO takeoBootcampTable ("User ID Number", "Name", "Cell Phone Number", "Email", "Address", entry_datetime) VALUES (?,?,?,?,?,?)', sample_entry)

# Commit the changes and close the connection
conn.commit()
conn.close()
