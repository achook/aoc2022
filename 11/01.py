from re import search
from dataclasses import dataclass

@dataclass
class Monkey:
    index : int
    items : list[int]
    operation: callable
    test_divisible_by: int
    monkey_index_if_true: int
    monkey_index_if_false: int
    inspected_items: int


with open("input.txt", "r") as file:
    raw_lines = "".join(file.readlines())

raw_monkeys = raw_lines.split("\n\n")

monkeys : list[Monkey] = []

for rm in raw_monkeys:
    result = search(r"Monkey ([0-9]+):\n. Starting items: ((?:[0-9]+(?:, )?)+)\n. Operation: (.+)\n  Test: divisible by ([0-9]+)\n.   If true: throw to monkey ([0-9]+)\n.   If false: throw to monkey ([0-9]+)", rm)
    g = result.groups()
    monkey_index = int(g[0])
    monkey_items = [int(v) for v in g[1].split(", ")]
    
    func_tokens = g[2].split(" ")
    func_operation_raw = func_tokens[3]
    func_parameter_raw = func_tokens[4]

    if func_operation_raw == "+":
            if func_parameter_raw == "old":
                def anonymous_add_old(old):
                    return old + old
                monkey_func = anonymous_add_old
            else:
                param1 = int(func_parameter_raw)
                def anonymous_add_param(old, p = param1):
                    return old + p
                monkey_func = anonymous_add_param
    if func_operation_raw == "*":
        if func_parameter_raw == "old":
            def anonymous_mul_old(old):
                return old * old
            monkey_func = anonymous_mul_old
        else:
            param2 = int(func_parameter_raw)
            def anonymous_mul_param(old, p = param2):
                    return old * p
            monkey_func = anonymous_mul_param

    monkey_divisible_by = int(g[3])
    monkey_if_true = int(g[4])
    monkey_if_false = int(g[5])

    m = Monkey(monkey_index, monkey_items, monkey_func, monkey_divisible_by, monkey_if_true, monkey_if_false, 0)
    monkeys.append(m)

for _ in range(20):
    for m in monkeys:

        while len(m.items) > 0:
            m.items[0] = m.operation(m.items[0])
            m.inspected_items += 1
            m.items[0] //= 3
            if m.items[0] % m.test_divisible_by == 0:
                monkeys[m.monkey_index_if_true].items.append(m.items.pop(0))
            else:
                monkeys[m.monkey_index_if_false].items.append(m.items.pop(0))


monkeys = sorted(monkeys, key=lambda m : m.inspected_items, reverse=True)

print(monkeys[0].inspected_items * monkeys[1].inspected_items)