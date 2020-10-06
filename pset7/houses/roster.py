from sys import argv
import cs50

if len(argv) != 2:
    print("Usage: python roster.py house_name")
    exit(1)

db = cs50.SQL("sqlite:///students.db")

print (argv[1])
roster = db.execute("SELECT DISTINCT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", argv[1])
for row in roster:
    print(row["first"]+" ", row["middle"]+" " if row["middle"] is not None else "", row["last"]+", ", "born ", row["birth"], sep = "")