# 12. Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

number_of_students = 3
students = []
over_13 = []
height_avg = 0
count = 0

# Getting the age and height of each student and store it into students array
# and also store every student who has over 13 in another array
for i in range(number_of_students):
    student_info = []
    height = float(input("Digite sua altura: "))
    age = float(input("Digite sua idade: "))
    student_info.extend([height, age])
    students.append(student_info)
    if student_info[1] > 13:
        over_13.append(student_info)


# Get the average of the heights
for info in students:
    height_avg += info[0]


height_avg /= number_of_students


# Verifying how many students has over 13 and the height under the average
for student in over_13:
    if student[0] < height_avg:
        count += 1


print('Quantidade de alunos com mais de 13 anos com a altura menor que a média:', count)
