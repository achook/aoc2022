from functools import cmp_to_key

raw_lines = []


def compare_objects(obj1: list, obj2: list):
    idx = 0

    while idx < len(obj1) and idx < len(obj2):
        if isinstance(obj1[idx], int) and isinstance(obj2[idx], int):
            if obj1[idx] != obj2[idx]:
                if obj1[idx] < obj2[idx]:
                    return -1
                if obj1[idx] > obj2[idx]:
                    return 1

        if isinstance(obj1[idx], list) and isinstance(obj2[idx], list):
            res = compare_objects(obj1[idx], obj2[idx])
            if res != 0:
                return res

        if isinstance(obj1[idx], int) and isinstance(obj2[idx], list):
            res = compare_objects([obj1[idx]], obj2[idx])
            if res != 0:
                return res
        
        if isinstance(obj1[idx], list) and isinstance(obj2[idx], int):
            res = compare_objects(obj1[idx], [obj2[idx]])  
            if res != 0:
                return res
        
        idx += 1
    
    if len(obj1) < len(obj2):
        return -1
    if len(obj1) == len(obj2):
        return 0

    return 1


with open("input.txt", "r") as file:
    line_idx = 0

    for line in file:
        line = line.strip()
        if len(line) > 0:
            raw_lines.append(line)

raw_lines.append("[[2]]")
raw_lines.append("[[6]]")

executed_lines = []
for raw_line in raw_lines:
    d = None
    exec("d = " + raw_line)
    
    executed_lines.append(d)
    
executed_lines = sorted(executed_lines, key=cmp_to_key(compare_objects))

line_mul = 1

for idx, e in enumerate(executed_lines):
    if e == [[2]] or e == [[6]]:
        line_mul *= idx+1

print(line_mul)