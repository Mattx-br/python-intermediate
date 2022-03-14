# 8. Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

people_needed = 10

people_data = []

for index in range(people_needed):
    people = []
    height = float(input("Digite sua altura: "))
    age = int(input("Digite sua idade: "))
    people.extend([height, age])
    people_data.insert(0, people)

print(people_data)