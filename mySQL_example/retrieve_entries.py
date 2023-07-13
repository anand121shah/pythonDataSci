import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Retrieve all entries from the table
cursor.execute('SELECT * FROM takeoBootcampTable')
entries = cursor.fetchall()

# Display the entries in the terminal
for entry in entries:
    print(entry)

# Close the connection
conn.close()