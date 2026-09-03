"""

✅ Project 5: Student Grading System
Practice dictionaries, lists, loops, and averages.

Ask the user for at least 3 students.

Each student gets 3 grades.

Store in a dictionary:

students = {
    "Ali": [80, 90, 70],
    "Ayşe": [85, 75, 95],
    "Mehmet": [60, 70, 65]
}
Print each student’s average.

Extra: Show the student with the highest average.

"""

students = {}

for i in range(3):
    isim = input("Öğrenci ismini giriniz\n")
    students[isim] = []
    for j in range(3):
        students[isim].append(int(input("Öğrencinin notunu girin\n")))

highestName = ""
highestAvg = -1

for k, v in students.items():
    avg = sum(v) / len(v)
    print(f"{k}: {avg:.2f}")
    if avg > highestAvg:
        highestAvg = avg
        highestName = k

print(f"\nEn yüksek ortalamaya sahip öğrenci: {highestName} ({highestAvg:.2f})")