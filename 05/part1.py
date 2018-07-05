
def read_input(input_filename):

    with open(input_filename, "r") as input_file:
        input_string = input_file.read()
        return [int(s) for s in input_string.strip().split("\n")]

def go_jumping(program):

    counter = 0
    pc = 0

    while True:
        try:
            offset = program[pc]
            program[pc] += 1
            pc += offset
        except IndexError:
            return counter
        counter += 1

if __name__ == "__main__":
    INPUT = read_input("05/input.txt")
    print(go_jumping(INPUT))