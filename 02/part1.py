
import numpy as np

def read_input(input_filename):
    with open(input_filename, "r") as input_file:
        
        spreadsheet = []

        for line in input_file.readlines():
            line = line.strip()
            row = line.split("\t")
            spreadsheet.append([int(c) for c in row])

    return np.array(spreadsheet)

def calculate_checksum(data):
    return sum([np.max(row) - np.min(row) for row in data])

if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"
    INPUT_DATA = read_input(INPUT_FILENAME)
    print(calculate_checksum(INPUT_DATA))
