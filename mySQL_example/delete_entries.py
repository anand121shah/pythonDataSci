import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Display confirmation message
confirmation = input("Caution! Are you sure you want to delete all the entries from the database? This action cannot be undone. "
                     "If you wish to proceed, press 'Y'. Otherwise, press any key to cancel this action.")

if confirmation.lower() == 'y':
    # Delete all entries from the table
    cursor.execute('DELETE FROM takeoBootcampTable')

    # Commit the changes
    conn.commit()
    print("All entries have been deleted.")
else:
    print("Action canceled. No entries were deleted.")

# Close the connection
conn.close()
