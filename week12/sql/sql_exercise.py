import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('school.db')
print("Database created and connected successfully.")

# Create a cursor object
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade INTEGER NOT NULL
)
''')
print("Table created successfully.")

# Insert records
cursor.execute("INSERT INTO students (name, grade) VALUES ('Alice', 85)")
cursor.execute("INSERT INTO students (name, grade) VALUES ('Bob', 78)")
cursor.execute("INSERT INTO students (name, grade) VALUES ('Charlie', 90)")
print("Records inserted successfully.")
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()
for row in rows:
    print(row)

# Query to fetch records with grade > 80
cursor.execute("SELECT * FROM students WHERE grade > 80")
rows = cursor.fetchall()

print("Students with grades greater than 80:")
for row in rows:
    print(row)

# Update the grade of a student
cursor.execute("UPDATE students SET grade = 95 WHERE name = 'Alice'")
print("Updated Alice's grade successfully.")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Delete a student
cursor.execute("DELETE FROM students WHERE name = 'Bob'")
print("Deleted Bob successfully.")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
print("Database connection closed.")
