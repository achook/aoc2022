from re import search


def are_tail_and_head_touching(tail_position: list[int], head_position: list[int]) -> bool:
    return abs(tail_position[0] - head_position[0]) <= 1 \
       and abs(tail_position[1] - head_position[1]) <= 1


def calculate_new_tail_position(tail_position: list[int], head_position: list[int]) -> list[int]: 
    if are_tail_and_head_touching(tail_position, head_position):
        return tail_position

    y_delta = head_position[0] - tail_position[0]
    x_delta = head_position[1] - tail_position[1]

    if y_delta > 0:
        y_move = 1
    elif y_delta < 0:
        y_move = -1
    else:
        y_move = 0

    if x_delta > 0:
        x_move = 1
    elif x_delta < 0:
        x_move = -1
    else:
        x_move = 0

    return [tail_position[0]+y_move, tail_position[1]+x_move]


with open("input.txt", "r") as file:
    head_position = [0, 0]
    tail_position = [0, 0]
    visited_locations = [[0, 0]]

    for line in file:
        result = search(r"([LRUD]) ([0-9]+)", line)
        direction = result.group(1)
        steps_number = int(result.group(2))

        for _ in range(steps_number):
            if direction == "R":
                head_position[1] += 1
            elif direction == "L":
                head_position[1] -= 1
            elif direction == "U":
                head_position[0] += 1
            elif direction == "D":
                head_position[0] -= 1
            
            tail_position = calculate_new_tail_position(tail_position, head_position)
            
            if tail_position not in visited_locations:
                visited_locations.append(tail_position)

    print(len(visited_locations))