
def read_input(input_filename):
    with open(input_filename, "r") as input_file:
        return [int(x) for x in input_file.read().strip().split(",")]


def run_hash(lengths):

    hash_list = list(range(256))

    cursor = 0
    skip = 0

    for length in lengths:
        hash_list = add_knot(hash_list, cursor, length)
        cursor += length + skip
        cursor %= 256
        skip += 1

    return hash_list[0] * hash_list[1]

def add_knot(hash_list, cursor, length):
    if cursor + length >= 256:
        # We need to wrap

        overflow = (cursor + length) % 256
        rotating_bit = hash_list[cursor:] + hash_list[:overflow]
        assert len(rotating_bit) == length
        rotating_bit.reverse()

        new_list = rotating_bit[-overflow:] + hash_list[overflow:cursor] + rotating_bit[:-overflow]
        assert len(new_list) == len(hash_list)
        return new_list

    else:
        # No wrapping
        return hash_list[:cursor] + list(reversed(hash_list[cursor:cursor+length])) + hash_list[cursor+length:]

if __name__ == "__main__":
    INPUT = read_input("10/input.txt")
    print(run_hash(INPUT))