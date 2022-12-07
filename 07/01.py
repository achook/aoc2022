from dataclasses import dataclass
from re import search

@dataclass
class TreeElement:
    name = ""
    parent = None
    children = []
    size = 0

    def __str__(self):
        return f"Leaf: {self.name} weights: {size}"

    def __repr__(self):
        return f"Leaf: {self.name} weights: {size}"

root = TreeElement()
root.name = "/"
current_leaf = root

whole_size = 0

def traverse_tree(current_node: TreeElement):
    for child in current_node.children:
        current_node.size += traverse_tree(child)
    return current_node.size

def show_smaller_than(current_node: TreeElement, limit: int):
    for child in current_node.children:
        show_smaller_than(child, limit)

    if current_node.size <= limit:
        global whole_size
        whole_size += current_node.size


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
show_smaller_than(root, 100000)
print(whole_size)
