from collections import defaultdict
from math import inf

height_map = []

def is_valid(pos):
    global height_map
    return 0 <= pos[0] < len(height_map) and 0 <= pos[1] < len(height_map[0])

def is_in_range(current_pos, next_pos):
    current_height = height_map[current_pos[0]][current_pos[1]]
    next_height = height_map[next_pos[0]][next_pos[1]]

    return next_height <= current_height + 1

start_points = []

with open("input.txt", "r") as file:
    for row_idx, line in enumerate(file):
        map_row = []
        for col_idx, char in enumerate(line.strip()):
            if char == "S" or char == "a":
                start_points.append((row_idx, col_idx))
                map_row.append(0)
            elif char == "E":
                end_point = (row_idx, col_idx)
                map_row.append(ord("z") - ord("a"))
            else:
                map_row.append(ord(char)-ord("a"))
        height_map.append(map_row)

row_len = len(height_map[0])
col_len = len(height_map)

def return_zero():
    return 0

def return_inf():
    return inf

def return_none():
    return None

neighbours = defaultdict(list)

for row_idx in range(col_len):
    for col_idx in range(row_len):

        top = (row_idx-1, col_idx)
        bottom = (row_idx+1, col_idx)
        left = (row_idx, col_idx-1)
        right = (row_idx, col_idx+1)

        if is_valid(top) and is_in_range((row_idx, col_idx), top):
            neighbours[(row_idx, col_idx)].append(top)
        
        if is_valid(bottom) and is_in_range((row_idx, col_idx), bottom):
            neighbours[(row_idx, col_idx)].append(bottom)
        
        if  is_valid(left) and is_in_range((row_idx, col_idx), left):
            neighbours[(row_idx, col_idx)].append(left)
        
        if is_valid(right) and is_in_range((row_idx, col_idx), right) :
            neighbours[(row_idx, col_idx)].append(right)


min_distance = inf

for start_point in start_points:
    colors = defaultdict(return_zero)
    distance = defaultdict(return_inf)
    parents = defaultdict(return_none)
    queue = []

    colors[start_point] = 1
    distance[start_point] = 0
    parents[start_point] = None
    queue.append(start_point)

    while len(queue) > 0:
        u = queue.pop(0)
        for v in neighbours[u]:
            if colors[v] == 0:
                colors[v] = 1
                distance[v] = distance[u] + 1
                parents[v] = u
                queue.append(v)

        colors[u] = 2

    if distance[end_point] < min_distance:
        min_distance = distance[end_point]

print(min_distance)