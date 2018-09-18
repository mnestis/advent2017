
from pathlib import Path

from tqdm import tqdm

def perform_dance(dance_steps):
    
    dancers = [chr(i) for i in range(ord("a"), ord("q"))]

    for step in dance_steps:
        if step.startswith("s"):
            offset = int(step[1:])
            dancers = dancers[-offset:] + dancers[:-offset]
        elif step.startswith("x"):
            pos_a, pos_b = [int(x) for x in step[1:].split("/")]
            dancers[pos_a], dancers[pos_b] = dancers[pos_b], dancers[pos_a]
        elif step.startswith("p"):
            dancer_a, dancer_b = step[1:].split("/")
            pos_a, pos_b = dancers.index(dancer_a), dancers.index(dancer_b)
            dancers[pos_a], dancers[pos_b] = dancers[pos_b], dancers[pos_a]

    return "".join(dancers)

if __name__ == "__main__":
    INPUT_PATH = Path.cwd() / "input.txt"
    assert INPUT_PATH.exists()

    with open(INPUT_PATH, "r") as input_file:
        input_str = input_file.read().strip()
        dance_steps = input_str.split(",")
        print(perform_dance(dance_steps))
