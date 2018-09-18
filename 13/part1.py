
from os import system
from pathlib import Path

from time import sleep

def print_packet(packet_pos):
    if packet_pos > 0:
        print((" " * packet_pos) + "*")
    else:
        print("*")

def print_scanner(scanner_pos, layer=0):
    print("".join([("X" if val == layer else " ") for val in scanner_pos]))

def print_whole_scanner(packet_pos, scanner_pos):
    system("clear")
    print_packet(packet_pos)
    for layer in range(1 + max([s for s in scanner_pos if s is not None])):
        print_scanner(scanner_pos, layer = layer)


def run_firewall(firewall_config):
    firewall_depth = max(firewall_config.keys())
    scanner_pos = [(0 if x in firewall_config else None) for x in range(firewall_depth + 1)]
    packet_pos = 0
    current_score = 0
    while packet_pos <= firewall_depth:
        if scanner_pos[packet_pos] == 0:
            penalty = packet_pos * firewall_config[packet_pos]
            current_score += penalty

        print_whole_scanner(packet_pos, scanner_pos)
        sleep(0.1)

        for scanner_depth, scanner_cur_range in enumerate(scanner_pos):
            if scanner_cur_range is not None:
                scanner_pos[scanner_depth] += 1
                scanner_pos[scanner_depth] %= firewall_config[scanner_depth] + 1

        packet_pos += 1

    return current_score

if __name__ == "__main__":
    INPUT_PATH = Path.cwd() / "input.txt"
    assert INPUT_PATH.exists()

    with open(INPUT_PATH, "r") as input_file:
        input_str = input_file.read().strip()
        rows = [row.split(": ") for row in input_str.split("\n")]
        firewall_config = {int(val[0]): int(val[1]) for val in rows}
        print(run_firewall(firewall_config))