import sqlite3
from tabulate import tabulate

def retrieve_entries():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Check if the table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='takeoBootcampTable'")
    table_exists = cursor.fetchone()

    if table_exists:
        # Retrieve all entries from the table
        cursor.execute('SELECT * FROM takeoBootcampTable')
        entries = cursor.fetchall()

        if entries:
            # Create a list of records
            records = []
            for entry in entries:
                user_id = entry[0]
                name = entry[1]
                cell_phone = entry[2]
                email = entry[3]
                address = entry[4]
                entry_datetime = entry[5]

                # Add each record as a list of values
                record = [user_id, name, cell_phone, email, address, entry_datetime]
                records.append(record)

            # Define the headers for the table
            headers = ["User ID Number", "Name", "Cell Phone Number", "Email", "Address", "Entry Datetime"]

            # Print the table using tabulate
            print(tabulate(records, headers=headers, tablefmt="grid"))
        else:
            print("Table is empty.")
    else:
        print("Database or table does not exist.")

    conn.close()

# Call the function to retrieve entries
retrieve_entries()
