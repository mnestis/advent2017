

def read_input(input_filename):
    with open(input_filename, "r") as input_file:
        return [line.strip().split(" ") for line in input_file.readlines()]

def validate_passphrase(phrase):
    already_parsed = set()
    for word in phrase:
        if word in already_parsed:
            return False
        already_parsed.add(word)
    return True

if __name__ == "__main__":
    INPUT = read_input("input.txt")
    valid_count = 0
    for phrase in INPUT:
        valid_count += 1 if validate_passphrase(phrase) else 0
    print(valid_count)
