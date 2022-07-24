word = 'tomato'
dictionary = {}

for i in word:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1
print(dictionary)

word = 'tomato'
result = {}

for i in word:
    result[i] = result.get(i, 0) + 1
print(result)

for i in result:
    print(i, result[i])

