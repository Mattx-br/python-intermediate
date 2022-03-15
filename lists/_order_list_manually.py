"""
Ordenar array manualmente | Sort array manually
"""

array = [3, 1, 2, 5, 1]
print(array)

for index in range(1, len(array)):
    value = array[index]
    i = index - 1
    # Comparing value to the left element, if it's smaller, shift then
    while i >= 0 and value < array[i]:
            array[i + 1] = array[i]  # shift the actual element with the left element
            array[i] = value  # value is the actual element
            i = i - 1


print(array)
