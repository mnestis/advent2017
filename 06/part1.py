import numpy as np

def read_input(filename):
    with open(filename, "r") as input_file:
        return tuple([int(i) for i in input_file.read().strip().split("\t")])

def balance_stacks(starting_configuration):

    counter = 0
    current_stacks = list(starting_configuration)
    previous_stacks = set()
    previous_stacks.add(starting_configuration)

    while True:
        counter += 1
        bin_index = np.argmax(current_stacks)
        hopper = current_stacks[bin_index]
        current_stacks[bin_index] = 0

        while hopper:
            bin_index += 1
            if bin_index == len(current_stacks):
                bin_index = 0
            current_stacks[bin_index] += 1
            hopper -= 1
        
        if tuple(current_stacks) in previous_stacks:
            return counter
        previous_stacks.add(tuple(current_stacks))

if __name__ == "__main__":
    INPUT = read_input("06/input.txt")
    print(balance_stacks(INPUT))