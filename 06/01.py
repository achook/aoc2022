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
pos = 4
last_4 = data[:pos]

while pos < length and has_repetitions(last_4):

    pos += 1
    last_4 = data[pos-4:pos]

print(pos)


file.close()