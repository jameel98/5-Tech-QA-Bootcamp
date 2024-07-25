import sqlite3


def create_tables():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Company (
            id INTEGER PRIMARY KEY,
            name TEXT,
            industry TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Job (
            id INTEGER PRIMARY KEY,
            title TEXT,
            company_id INTEGER,
            description TEXT,
            FOREIGN KEY (company_id) REFERENCES Company (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Post (
            id INTEGER PRIMARY KEY,
            text TEXT,
            user_id INTEGER,
            created_at TEXT,
            FOREIGN KEY (user_id) REFERENCES User (id)
        )
    ''')

    conn.commit()
    conn.close()

    def insert_data():
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # Example data insertion for Users
        users = [
            (1, 'john_doe', 'John', 'Doe'),
            (2, 'jane_smith', 'Jane', 'Smith')
        ]
        cursor.executemany('''
            INSERT INTO User (id, username, first_name, last_name)
            VALUES (?, ?, ?, ?)
        ''', users)

        # Insert data for Companies
        companies = [
            (1, 'TechCorp', 'Technology'),
            (2, 'HealthInc', 'Healthcare')
        ]
        cursor.executemany('''
            INSERT INTO Company (id, name, industry)
            VALUES (?, ?, ?)
        ''', companies)

        # Insert data for Jobs
        jobs = [
            (1, 'Software Engineer', 1, 'Develop software solutions.'),
            (2, 'Data Scientist', 2, 'Analyze healthcare data.')
        ]
        cursor.executemany('''
            INSERT INTO Job (id, title, company_id, description)
            VALUES (?, ?, ?, ?)
        ''', jobs)

        # Insert data for Posts
        posts = [
            (1, 'Working on a new project!', 1, '2024-07-24'),
            (2, 'Excited to join TechCorp!', 2, '2024-07-25')
        ]
        cursor.executemany('''
            INSERT INTO Post (id, text, user_id, created_at)
            VALUES (?, ?, ?, ?)
        ''', posts)

        conn.commit()
        conn.close()

    def retrieve_combined_data():
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT User.username, Post.text, Post.created_at
            FROM User
            JOIN Post ON User.id = Post.user_id
        ''')

        combined_data = cursor.fetchall()
        for row in combined_data:
            print(f"User: {row[0]}, Post: {row[1]}, Created At: {row[2]}")

        conn.close()

    retrieve_combined_data()
