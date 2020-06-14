dictionary = {
    'Edward': 26,
    'Eli': 24,
    'Frederick': 27,
    'Niño desconocido': 8
}

list_comprehension = { key + ', mayor' for key, value in dictionary.items() if value >= 18 }


print('Diccionario original')
print(dictionary)

print('Diccionario luego de list comprehension')
print(list_comprehension)

