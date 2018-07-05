
import re

def read_input(input_filename):
    global_children = set()
    global_parents = set()
    with open(input_filename, "r") as input_file:
        input_lines = input_file.read().strip().split("\n")
        for line in input_lines:
            components = line.split("->")
            parent = components[0].split(" ")[0]
            global_parents.add(parent)
            try:
                children = components[1].strip().split(", ")
                for child in children:
                    global_children.add(child)
            except IndexError:
                pass
    return list(global_parents - global_children)[0]

if __name__ == "__main__":
    INPUT = read_input("07/input.txt")
    print(INPUT)