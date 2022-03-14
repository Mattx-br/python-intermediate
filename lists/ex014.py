# 14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

questions = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?"]

answers = []

classification = ''

# get the answer
print('[1] para sim, Enter para não')
for question in questions:
    answer = bool(input(f'{question} '))
    if answer:
        answers.append(answer)

# Classifying the person depending on how many questions were true
if len(answers) == 2:
    classification = 'Suspeita'
elif 3 <= len(answers) <= 4:
    classification = 'Cúmplice'
elif len(answers) == 5:
    classification = 'Assassino'
else:
    classification = 'Inocente'


print(classification)

