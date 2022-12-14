raw_line_pairs = []

CORRECT = 1
WRONG = -1
CONTINUE = 0

def compare_objects(obj1: list, obj2: list):
    idx = 0

    while idx < len(obj1) and idx < len(obj2):
        if isinstance(obj1[idx], int) and isinstance(obj2[idx], int):
            if obj1[idx] != obj2[idx]:
                if obj1[idx] < obj2[idx]:
                    return CORRECT
                if obj1[idx] > obj2[idx]:
                    return WRONG

        if isinstance(obj1[idx], list) and isinstance(obj2[idx], list):
            res = compare_objects(obj1[idx], obj2[idx])
            if res != CONTINUE:
                return res

        if isinstance(obj1[idx], int) and isinstance(obj2[idx], list):
            res = compare_objects([obj1[idx]], obj2[idx])
            if res != CONTINUE:
                return res
        
        if isinstance(obj1[idx], list) and isinstance(obj2[idx], int):
            res = compare_objects(obj1[idx], [obj2[idx]])  
            if res != CONTINUE:
                return res
        
        idx += 1
    
    if len(obj1) < len(obj2):
        return CORRECT
    if len(obj1) == len(obj2):
        return CONTINUE

    return WRONG


with open("input.txt", "r") as file:
    line_idx = 0

    for line in file:
        line = line.strip()

        line_idx %= 3

        if line_idx == 0:
            raw_line_pairs.append([line])

        if line_idx == 1:
            raw_line_pairs[-1].append(line)
        
        line_idx += 1

indices_sum = 0

for idx, raw_pair in enumerate(raw_line_pairs):
    # really bad
    pair1 = None
    pair2 = None
    exec("pair1 = " + raw_pair[0])
    exec("pair2 = " + raw_pair[1])
    
    if compare_objects(pair1, pair2) == CORRECT:
        indices_sum += idx+1

print(indices_sum)