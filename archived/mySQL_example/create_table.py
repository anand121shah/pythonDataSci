import mysql.connector
from datetime import datetime

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='9900',
    user='Ted',
    password='Life',
    database='myDB'
)
cursor = conn.cursor()

# Check if the 'entryDateTime' column already exists
cursor.execute("SHOW COLUMNS FROM takeoBootcampTable LIKE 'entryDateTime'")
column = cursor.fetchone()
if column is None:
    # Add the 'entryDateTime' column if it doesn't exist
    cursor.execute("ALTER TABLE takeoBootcampTable ADD COLUMN entryDateTime DATETIME")

# Prompt the user for input
entry_code = input("Enter the entry code: ")
entry_number = input("Enter the entry number: ")
name = input("Enter the name: ")
designation = input("Enter the designation: ")
gender = input("Enter the gender: ")
email = input("Enter the email: ")
phone = input("Enter the phone number: ")
entry_datetime = datetime.now()

# Insert the entered values into the table
sample_entry = (
    entry_code,
    entry_number,
    name,
    designation,
    gender,
    email,
    phone,
    entry_datetime
)
cursor.execute('INSERT INTO takeoBootcampTable VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', sample_entry)

# Commit the changes and close the connection
conn.commit()
conn.close()
