import requests
import sqlite3
import csv
from bs4 import BeautifulSoup


url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
jobs = soup.find_all("div", class_="card-content")


conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    apply_link TEXT,
    UNIQUE(title, company, location)
)
""")


for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    desc = job.find("div", class_="content").text.strip()
    link = job.find("a")["href"]

    data = (title, company, location, desc, link)

    cursor.execute("""
    INSERT OR IGNORE INTO jobs (title, company, location, description, apply_link)
    VALUES (?, ?, ?, ?, ?)
    """, data)

    cursor.execute("""
    UPDATE jobs
    SET description = ?, apply_link = ?
    WHERE title = ? AND company = ? AND location = ?
    """, (desc, link, title, company, location))

conn.commit()


def filter_jobs(by="location", value="Remote"):
    query = f"SELECT title, company, location, description, apply_link FROM jobs WHERE {by} = ?"
    cursor.execute(query, (value,))
    return cursor.fetchall()


def export_to_csv(rows, filename="filtered_jobs.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "Description", "Apply Link"])
        writer.writerows(rows)
    print(f"Exported {len(rows)} jobs to {filename}")


filtered = filter_jobs(by="location", value="Remote") 
export_to_csv(filtered, "remote_jobs.csv")

filtered2 = filter_jobs(by="company", value="Sovran Software")  
export_to_csv(filtered2, "sovran_jobs.csv")

conn.close()
