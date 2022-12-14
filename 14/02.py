from re import finditer
from math import inf

raw_lines = []

min_x = inf
max_x = -inf
min_y = inf
max_y = -inf

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        
        for res in finditer(r"([0-9]+),([0-9]+)", line):
            x = int(res.group(1))
            y = int(res.group(2))

            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y

        raw_lines.append(line.strip())

cave_map = [[" " for x in range(max_x-min_x+(max_y*2)+1)] for y in range (max_y+3)]

for line in raw_lines:
    raw_vertices = line.split(" -> ")
    vertices = []
    for v in raw_vertices:
        x = int(v.split(",")[0])-min_x+max_y
        y = int(v.split(",")[1])
        vertices.append((x, y))
    
    for idx in range(len(vertices)-1):
        start = vertices[idx]
        end = vertices[idx+1]

        if start[0] == end[0]:
            for y in range(min(start[1],end[1]), max(start[1], end[1])+1):
                cave_map[y][start[0]] = "#"
        elif start[1] == end[1]:
            for x in range(min(start[0],end[0]), max(start[0], end[0])+1):
                cave_map[start[1]][x] = "#"
        else:
            raise RuntimeError

for x in range(0, (max_x-min_x+(max_y*2)+1)):
    cave_map[max_y+2][x] = "#"

#for line in cave_map:
#    print(*line)

should_stop = False
fallen = 0

def fall(start_pos: tuple[int, int]):
    global cave_map
    global min_x, max_x, max_y
    global should_stop
    global fallen

    current_pos = start_pos
    x = current_pos[0]
    y = current_pos[1]

    while not should_stop and y <= max_y+1:
        if cave_map[y+1][x] == " ":
            y += 1
            continue
        
        if cave_map[y+1][x-1] == " ":
            x -= 1
            y += 1
            continue
        
        if cave_map[y+1][x+1] == " ":
            x += 1
            y += 1
            continue
        
        fallen += 1
        cave_map[y][x] = "o"

        if y == 0:
            return False
        else:
            return True


while fall([500-min_x+max_y, 0]) == True:
    pass

#for line in cave_map:
#    print(*line)

print(fallen)
