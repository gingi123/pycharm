
def mat5(students):
    print(f"Matematikából és fizikából 5-os tanulok:")
    for student in students:
        matek = int(student["MATEMATIKA"])
        fizika = int(student["FIZIKA"])
        if matek >= 5 and fizika >= 5:
            printname(student)
def fiz5(students):
    print(f"Fizikából legalább 2 jeggyel jobb mint matematikából:")
    for student in students:
        matek = int(student["MATEMATIKA"])
        fizika = int(student["FIZIKA"])
        if fizika >= matek + 2 and fizika > matek + 2:
            printname(student)

def avgfiz(students):
    fizika_grades = []
    for student in students:
        fizika = int(student["FIZIKA"])
        fizika_grades.append(fizika)
    if len(fizika_grades) > 0:
        avgfizp = sum(fizika_grades)/len(fizika_grades)
        print(f"Évfolyam átlag Fizikából: {avgfizp}")
        #return summarum

def avgmat(students):
    matek_grades = []
    for student in students:
        matek = int(student["MATEMATIKA"])
        matek_grades.append(matek)
    if len(matek_grades) > 0:
        avgmatp = sum(matek_grades)/len(matek_grades)
        print(f"Évfolyam átlag matekból: {avgmatp}")
        #return summarum

def list1(students):
    for student in students:
        printname(student)

def printname(students):
    print(f"{students['TANULO']}")


students = []

with open("osztalyzatok.txt","r",encoding='utf=8') as file:
    file_content = file.read()
    format_lines1 = file_content[:-1].split('\n') #levágtam a végéről az entert
    format_lines2 = format_lines1[1:] # megint levágtam a fejlécet
for lines in format_lines2:
    splitted_line = lines.split("\t")
    students.append({
        "TANULO":splitted_line[0],
        "MATEMATIKA":splitted_line[1],
        "FIZIKA":splitted_line[2],
    })

for item in students:
    name = item["TANULO"]
    matek = int(item["MATEMATIKA"])
    fizika = int(item["FIZIKA"])



mat5(students)
fiz5(students)
avgmat(students)
avgfiz(students)
print(format_lines2)
print(splitted_line)
















