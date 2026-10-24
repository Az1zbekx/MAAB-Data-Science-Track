import csv

sub = {}

with open("grades.csv", newline="") as f:
    r = csv.DictReader(f)
    for t in r:
        subject = t['Subject']
        grade = int(t['Grade'])
        if subject not in sub:
            sub[subject] = [] 
        sub[subject].append(grade)
for a, b in sub.items():
    sub[a] = round((sum(b) / len(b)), 1)

with open("average_grades.csv", "w", newline="") as f:
    fieldnames = ["Subject", "Average Grade"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for subject, avg in sub.items():
        writer.writerow({"Subject": subject, "Average Grade": avg})




