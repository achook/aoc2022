from dataclasses import dataclass
from re import search

@dataclass
class TreeElement:
    name = ""
    parent = None
    children = []
    size = 0

    def __str__(self):
        return f"Leaf: {self.name} weights: {self.size}"

    def __repr__(self):
        return f"Leaf: {self.name} weights: {self.size}"

root = TreeElement()
root.name = "/"
current_leaf = root
smallest_possible = root

def traverse_tree(current_node: TreeElement):
    for child in current_node.children:
        current_node.size += traverse_tree(child)
    return current_node.size


def find_minimal_dir(current_node: TreeElement, limit: int):
    global smallest_possible

    for child in current_node.children:
        find_minimal_dir(child, limit)

    if current_node.size < smallest_possible.size and current_node.size >= limit:
        smallest_possible = current_node


with open("input.txt", "r") as file:
    is_ls = False

    for line in file:

        line = line.strip()

        if "$ cd" in line:
            is_ls = False
            new_dir = line[5:].strip()
            if "/" in new_dir:
                current_leaf = root

            elif ".." in new_dir:
                current_leaf = current_leaf.parent

            else:
                for child in current_leaf.children:
                    if child.name == new_dir:
                        current_leaf = child
                        break
        if is_ls:
            result = search(r"([0-9]+) ([A-z\.]+)", line)
            if result is not None:
                groups = result.groups()
                size = int(groups[0])
                name = groups[1].strip()
                current_leaf.size += size
                continue

            result = search(r"dir ([A-z\.]+)", line)
            groups = result.groups()
            name = groups[0].strip()

            new_leaf = TreeElement()
            new_leaf.children = []
            new_leaf.name = name
            new_leaf.parent = current_leaf

            current_leaf.children.append(new_leaf)


        if "$ ls" in line:
            is_ls = True

traverse_tree(root)

needed_space = 30000000 - (70000000 - root.size)
find_minimal_dir(root, needed_space)
print(smallest_possible.size)
