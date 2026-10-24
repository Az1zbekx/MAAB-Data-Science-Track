import sqlite3

conn = sqlite3.connect("library.db")

cursor = conn.cursor()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Books(
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
    )
""")

data = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic ")
]

cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES(?, ?, ?, ?)", data)
cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
for row in cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'"):
    print(row)
cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
cursor.execute("ALTER TABLE Books ADD COLUMN Rating FLOAT")
cursor.execute("UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
cursor.execute("UPDATE Books SET Rating = 4.7 WHERE Title = '1984'")
cursor.execute("UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")
for row in cursor.execute('SELECT * FROM Books ORDER BY Year_Published ASC'):
    print(row)

conn.commit()