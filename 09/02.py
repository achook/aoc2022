from re import search

KNOT_COUNT = 9


def are_knots_touching(knot1_position: list[int], knot2_position: list[int]) -> bool:
    return abs(knot1_position[0] - knot2_position[0]) <= 1 \
       and abs(knot1_position[1] - knot2_position[1]) <= 1


def calculate_new_knot_position(knot_position: list[int], predecessor_position: list[int]) -> list[int]: 
    if are_knots_touching(knot_position, predecessor_position):
        return knot_position

    y_delta = predecessor_position[0] - knot_position[0]
    x_delta = predecessor_position[1] - knot_position[1]

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

    return [knot_position[0]+y_move, knot_position[1]+x_move]


with open("input.txt", "r") as file:
    head_position = [0, 0]
    knot_positions = [[0, 0] for _ in range(KNOT_COUNT)]
    visited_positions = [[0,0]]

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

            knot_positions[0] = calculate_new_knot_position(knot_positions[0], head_position)
            
            for knot_idx in range(1, 9):
                knot_positions[knot_idx] = calculate_new_knot_position(knot_positions[knot_idx], knot_positions[knot_idx-1])
            
            if knot_positions[8] not in visited_positions:
                visited_positions.append(knot_positions[8])

    print(len(visited_positions))