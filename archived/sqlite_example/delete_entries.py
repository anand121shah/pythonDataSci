import sqlite3

def delete_entries():
    # Confirmation prompt
    confirmation = input("Caution! Are you sure you want to delete all the entries from the database? This action cannot be undone. "
                         "If you wish to proceed, press 'Y'. Otherwise, press any key to cancel this action.")

    if confirmation.lower() == 'y':
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Delete all entries from the table
        cursor.execute('DELETE FROM takeoBootcampTable')

        conn.commit()
        conn.close()

        print("All entries have been deleted from the database.")
    else:
        print("Deletion canceled. No entries were deleted.")

# Call the function to delete entries
delete_entries()
