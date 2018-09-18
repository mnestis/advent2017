"""
Day 11, Part 1
"""

from collections import Counter
from pathlib import Path

from tqdm import tqdm

def calculate_shortest_distance(path_list):
    moves = Counter()
    for move in path_list:
        moves[move] += 1

    while True:
        if moves["n"] and moves["s"]:
            moves["n"] -= 1
            moves["s"] -= 1
            continue
        if moves["nw"] and moves["se"]:
            moves["nw"] -= 1
            moves["se"] -= 1
            continue
        if moves["ne"] and moves["sw"]:
            moves["ne"] -= 1
            moves["sw"] -= 1
            continue
        if moves["n"] and moves["se"]:
            moves["n"] -= 1
            moves["se"] -= 1
            moves["ne"] +=1
            continue
        if moves["n"] and moves["sw"]:
            moves["n"] -= 1
            moves["sw"] -= 1
            moves["nw"] += 1
            continue
        if moves["s"] and moves["ne"]:
            moves["s"] -= 1
            moves["ne"] -= 1
            moves["se"] += 1
            continue
        if moves["s"] and moves["nw"]:
            moves["s"] -= 1
            moves["nw"] -= 1
            moves["ne"] += 1
            continue
        if moves["ne"] and moves["nw"]:
            moves["ne"] -= 1
            moves["nw"] -= 1
            moves["n"] += 1
            continue
        if moves["se"] and moves["sw"]:
            moves["se"] -= 1
            moves["sw"] -= 1
            moves["s"] += 1
            continue

        break

    return sum(moves.values())

def calculate_furthest_extent(path):
    dists = []
    for cutoff in tqdm(range(1, 1 + len(path))):
        dists.append(calculate_shortest_distance(path[:cutoff]))
    return max(dists)

if __name__ == "__main__":
    INPUT_PATH = Path.cwd() / "input.txt"
    assert INPUT_PATH.exists()
    with open(INPUT_PATH, "r") as input_file:
        input_str = input_file.read().strip()
        input_list = input_str.split(",")
        print(calculate_furthest_extent(input_list))