
from pathlib import Path

def group_membership(input_str):
    rows = input_str.split("\n")

    direct_connections = {}
    for row in rows:
        program_id, conns = row.split(" <-> ")
        direct_connections[program_id] = {}
        direct_connections[program_id] = set(conns.split(", "))
        direct_connections[program_id].add(program_id)

    groups = set()

    for pid in direct_connections:
        current_reach = 0
        reachable = direct_connections[pid]
        while True:
            for program_id in list(reachable):
                reachable.update(direct_connections[program_id])

            if len(reachable) == current_reach:
                break
            else:
                current_reach = len(reachable)
    
        groups.add(tuple(sorted(list(reachable))))

    return len(groups)
    
if __name__ == "__main__":
    INPUT_PATH = Path.cwd() / "input.txt"
    assert INPUT_PATH.exists()

    with open(INPUT_PATH, "r") as input_file:
        input_str = input_file.read().strip()

    print(group_membership(input_str))    