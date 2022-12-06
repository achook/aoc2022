from re import search

ship = []
    
with open("input.txt", "r") as file:
    for line in file:
        if (line[1] == "1"):
            break

        pos = 1
        i = 0
        while pos < len(line):
            if i >= len(ship):
                ship.append([])

            if line[pos] != " ":
                ship[i].append(line[pos])

            pos += 4
            i += 1

    file.readline()

    for i in range(len(ship)):
        ship[i].reverse()

    for line in file:
        result = search(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", line)

        to_move = int(result.group(1))
        move_from = int(result.group(2))-1
        move_to = int(result.group(3))-1
        
        for i in range(to_move):
            ship[move_to].append(ship[move_from].pop())

result = "On top: "

for load in ship:
    result += load.pop()

print(result)