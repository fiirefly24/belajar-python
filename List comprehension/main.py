grades = []
for grade in range(1,11):
    grades.append(grade)
print(grades)

grades = [x+x for x in range(1,11)]
print(grades)

grades = [23,45,67,97,45,23,12,45]
passGrade = [grade for grade in grades if grade >= 50]
print(passGrade)