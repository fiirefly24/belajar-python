# word = "orange" # Case sensitive
# letter = input("Guess a letter in the secret word: ")
# if letter not in word:
#     print(f"{letter} was not found")
# else:
## set
#     print(f"There is a {letter}")
# students = {"Spongebob", "Patrick", "Squidward"}
# student = input("Enter the name of a student: ")
# if student in students:
#     print(f"{student} found")
# else:
#     print(f"{student} was not found")

# Dictionary
grades = {
    "Spongebob": "C",
    "Sandy": "B",
    "Patrick": "S"
}
student = input("Enter a student name: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")