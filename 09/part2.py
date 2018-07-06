
def read_input(input_filename):
    with open(input_filename, "r") as input_file:
        return input_file.read().strip()

def remove_garbage(data_stream):

    in_garbage = False
    bang_count = 0
    garbage_count = 0

    for char in data_stream:
        if not in_garbage:
            if char == "<":
                in_garbage = True
        else:
            if char == "!":
                bang_count += 1
            else:
                if bang_count % 2 == 0 and char == ">":
                    in_garbage = False
                if bang_count % 2 == 0 and char != ">":
                    garbage_count += 1
                bang_count = 0

    return garbage_count


if __name__ == "__main__":
    INPUT = read_input("09/input.txt")
    print(remove_garbage(INPUT))