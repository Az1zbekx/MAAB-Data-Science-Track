import sqlite3

conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Roster(
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
"""
)

data = [
    ("Benjamin Sisko", "Human", 340),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29),
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

cursor.execute(
    """
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
"""
)
for row in cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'"):
    print(row)

cursor.execute("DELETE FROM Roster WHERE Age > 100")
cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
cursor.execute("UPDATE Roster SET Rank = 'Kapitan' WHERE Name = 'Benjamin Sisko'")
cursor.execute("UPDATE Roster SET Rank = 'Leytenant' WHERE Name = 'Ezri Dax'")
cursor.execute("UPDATE Roster SET Rank = 'Asosiy' WHERE Name = 'Kira Nerys'")

conn.commit()
conn.close()
