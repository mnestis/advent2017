
import numpy as np
import itertools

def read_input(input_filename):
    with open(input_filename, "r") as input_file:
        
        spreadsheet = []

        for line in input_file.readlines():
            line = line.strip()
            row = line.split("\t")
            spreadsheet.append([int(c) for c in row])

    return np.array(spreadsheet)

def calculate_factor(row):
    for perm in itertools.permutations(row, 2):
        if perm[0] // perm[1] == perm[0] / perm[1]:
            return perm[0] // perm[1]

def get_factors(data):
    return sum([calculate_factor(row) for row in data])

if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"
    INPUT_DATA = read_input(INPUT_FILENAME)
    print(get_factors(INPUT_DATA))
