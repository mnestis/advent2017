
def read_input(input_filename):
    with open(input_filename, "r") as input_file:
        return input_file.read().strip()

def remove_garbage(data_stream):

    in_garbage = False
    bang_count = 0

    output_stream = ""
    for char in data_stream:
        if not in_garbage:
            if char != "<":
                output_stream += char
            else:
                in_garbage = True
        else:
            if char == "!":
                bang_count += 1
            else:
                if bang_count % 2 == 0 and char == ">":
                    in_garbage = False
                bang_count = 0
    return output_stream

def score_stream(data_stream):
    stream = remove_garbage(data_stream)
    score = 0

    assert stream.count("{") == stream.count("}")

    depth = 0
    for char in stream:
        if char == "{":
            depth += 1
        elif char == "}":
            score += depth
            depth -= 1
    return score

if __name__ == "__main__":
    INPUT = read_input("09/input.txt")
    print(score_stream(INPUT))