def has_repetitions(arr):
    checked = []

    for el in arr:
        if el in checked:
            return True
        checked.append(el)

    return False

file = open("input.txt", "r")
data = file.readline()

length = len(data)
pos = 14
last_14 = data[:pos]

while pos < length and has_repetitions(last_14):

    pos += 1
    last_14 = data[pos-14:pos]

print(pos)


file.close()