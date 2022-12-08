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

visible_trees = 2*forest_height + 2*(forest_width-2)

for target_y in range(1, forest_height-1):
    for target_x in range(1, forest_width-1):
        target_height = forest[target_y][target_x]

        is_visible_at_all = False

        # Go from the left
        is_visible_right_now = True
        for x in range(0, target_x):
            if forest[target_y][x] >= target_height:
                is_visible_right_now = False
                break

        if is_visible_right_now:
            is_visible_at_all = True

        # Go from the right
        is_visible_right_now = True
        if not is_visible_at_all:
            for x in range(forest_width-1, target_x, -1):
                if forest[target_y][x] >= target_height:
                    is_visible_right_now = False
                    break

        if is_visible_right_now:
            is_visible_at_all = True

        # Go from the top
        is_visible_right_now = True
        if not is_visible_at_all:
            for y in range(0, target_y):
                if forest[y][target_x] >= target_height:
                    is_visible_right_now = False
                    break

        if is_visible_right_now:
            is_visible_at_all = True

        # Go from the bottom
        is_visible_right_now = True
        if not is_visible_at_all:
            for y in range(forest_height-1, target_y, -1):
                if forest[y][target_x] >= target_height:
                    is_visible_right_now = False
                    break

        if is_visible_right_now:
            is_visible_at_all = True
        
        if is_visible_at_all:
            visible_trees += 1

print(visible_trees)
        