import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS takeoBootcampTable (
    batch_id varchar(5),
    student_id int,
    student_name varchar(255),
    student_qualification varchar(5),
    gender varchar(1),
    email varchar(255),
    mobile varchar(20)
)''')

# Add a sample entry to the table
sample_entry = (
    'B01',
    12345,
    'John Doe',
    'Grad',
    'M',
    'john.doe@example.com',
    '1234567890'
)
cursor.execute('INSERT INTO takeoBootcampTable VALUES (?,?,?,?,?,?,?)', sample_entry)

# Commit the changes and close the connection
conn.commit()
conn.close()
