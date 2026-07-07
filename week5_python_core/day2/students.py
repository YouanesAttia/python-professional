import csv
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(',')
        student = {"name": name, "house": house}
        students.append(student)



for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})


name = input("What's your name? ")
home = input("Where's yout home? ")
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})