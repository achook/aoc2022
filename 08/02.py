forest = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        tree_line = []
        for raw_height in line:
            height = int(raw_height)
            tree_line.append(height)
        forest.append(tree_line)

forest_width = len(forest[0])
forest_height = len(forest)

max_score = 0

for target_y in range(1, forest_height-1):
    for target_x in range(1, forest_width-1):
        score = 1
        target_height = forest[target_y][target_x]

        current_score = 0

        # Go to the the left
        for x in range(target_x-1, -1, -1):
            current_score += 1
            if forest[target_y][x] >= target_height:
                break

        score *= current_score
        current_score = 0

        # Go to the right
        for x in range(target_x+1,forest_width):
            current_score += 1
            if forest[target_y][x] >= target_height:
                break

        score *= current_score
        current_score = 0

        # Go to the top
        for y in range(target_y-1, -1, -1):
            current_score += 1
            if forest[y][target_x] >= target_height:
                break

        score *= current_score
        current_score = 0

        # Go to the bottom
        for y in range(target_y+1, forest_height):
            current_score += 1
            if forest[y][target_x] >= target_height:
                break
        
        score *= current_score

        if score > max_score:
            max_score = score

print(max_score)
        