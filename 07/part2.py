
import itertools

def read_input(input_filename):
    tree = {}
    with open(input_filename, "r") as input_file:
        input_lines = input_file.read().strip().split("\n")

        for line in input_lines:
            my_name = line.split(" ")[0]
            my_weight = int(line.split(" ")[1].split(")")[0][1:])
            if my_name in tree:
                tree[my_name]["weight"] = my_weight
            else:
                tree[my_name] = {"name": my_name, "weight": my_weight}
        
            if len(line.split("->")) > 1:
                children = line.split("->")[1].strip().split(", ")
                tree[my_name]["children"] = []
                for child in children:
                    if child not in tree:
                        tree[child] = {"name": child}
                    tree[my_name]["children"].append(tree[child])

    return tree

def rebalance_tree(tree):
    if is_balanced(tree):
        return 0

    child_weights = []
    for child in tree["children"]:
        child_weights.append(calculate_weight(child))
    for weight in child_weights:
        if child_weights.count(weight) == 1:
            unbalanced_index = child_weights.index(weight)
            if unbalanced_index == 0:
                balanced_index = 1
            else:
                balanced_index = 0
            return rebalance_subtree(tree["children"][unbalanced_index],
                                     tree["children"][balanced_index]["weight"])

def rebalance_subtree(tree, expected_weight):
    if is_balanced(tree):
        if "children" in tree:
            actual_weight = tree["weight"] + sum([calculate_weight(child) for child in tree["children"]])
            return tree["weight"] + (expected_weight - actual_weight)
        else:
            return expected_weight
    else:
        child_weights = []
        for child in tree["children"]:
            child_weights.append(calculate_weight(child))
        for weight in child_weights:
            if child_weights.count(weight) == 1:
                unbalanced_index = child_weights.index(weight)
                if unbalanced_index == 0:
                    balanced_index = 1
                else:
                    balanced_index = 0
                new_weight = rebalance_subtree(tree["children"][unbalanced_index],
                                               calculate_weight(tree["children"][balanced_index])) 
                if new_weight >= 0:
                    return new_weight
        else:
            return -1


def calculate_weight(tree):
    if "children" not in tree:
        return tree["weight"]

    return tree["weight"] + sum([calculate_weight(child) for child in tree["children"]])

def is_balanced(tree):
    if "children" not in tree:
        return True

    child_weights = []
    for child in tree["children"]:
        child_weights.append(calculate_weight(child))

    for pair in itertools.combinations(child_weights, 2):
        if pair[0] != pair[1]:
            return False
    else:
        return True

def print_tree(tree, level=0):
    for _ in range(level):
        print("\t", end="")
    
    print(f"{tree['name']}, w:{tree['weight']}, tw:{calculate_weight(tree)}")
    if "children" in tree:
        for child in tree["children"]:
            print_tree(child, level+1)
    

if __name__ == "__main__":
    INPUT = read_input("07/input.txt")
    print(rebalance_tree(INPUT["veboyvy"]))

