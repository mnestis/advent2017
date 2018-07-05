
def read_input(input_location):
    with open(input_location, "r") as input_file:
        input_data = input_file.read().strip()
    return input_data

def calculate_captcha(input_data):
    pairs = list(zip(input_data[:-1], input_data[1:])) + [(input_data[0], input_data[-1])]

    return sum([(int(pair[0]) if pair[0] == pair[1] else 0) for pair in pairs])


if __name__ == "__main__":
    INPUT_LOCATION = "input.txt"
    INPUT_DATA = read_input(INPUT_LOCATION)
    print(calculate_captcha(INPUT_DATA))
